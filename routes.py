import sqlite3

def main():
    conn = sqlite3.connect('fly.sqlite')
    cursor = conn.cursor()

    # ----------------- Spørsmål i Terminalen -----------------
    airport = input("Hvilken flyplasskode ønsker du? (f.eks. TRD): ").strip().upper()
    day_of_week = input("Hvilken ukedag (tall 1=mandag ... 7=søndag)? ").strip()
    direction = input("Ønsker du avganger (D) eller ankomster (A)? ").strip().upper()

    # Spør databasen om avganger eller ankomster
    # ukdag = 1234567, flyplass = XXX, avgang/ankomst = D/A
    if direction == 'D':
        # Avganger: finn alle ruter der 'airport' er startflyplass ELLER en mellomlanding,
        # flyrute.planlagt_avreisetid hvis airport er start eller flyrute.avgangstid hvis airport er mellomlanding.
        sql = """
        SELECT r.flyrutenummer,
                CASE 
                    WHEN r.startflyplass = :airport THEN r.planlagt_avreisetid
                    ELSE m.avgangstid
                END AS departure_time
        FROM flyrute r
        LEFT JOIN mellomlanding m
            ON r.flyrutenummer = m.flyrutenummer
                AND m.flyplasskode = :airport
        WHERE r.ukedagskode LIKE '%' || :day || '%'
            AND (r.startflyplass = :airport OR m.flyplasskode = :airport)
        ORDER BY departure_time
        """
    else:
        # Arrivals: ca samme logikk, men vi ser på ankomsttider heller.
        sql = """
        SELECT r.flyrutenummer,
                CASE 
                    WHEN r.endeflyplass = :airport THEN r.planlagt_ankomsttid
                    ELSE m.ankomsttid
                END AS arrival_time
        FROM flyrute r
        LEFT JOIN mellomlanding m
            ON r.flyrutenummer = m.flyrutenummer
                AND m.flyplasskode = :airport
        WHERE r.ukedagskode LIKE '%' || :day || '%'
            AND (r.endeflyplass = :airport OR m.flyplasskode = :airport)
        ORDER BY arrival_time
        """

    # Kjør
    cursor.execute(sql, {"airport": airport, "day": day_of_week})
    rows = cursor.fetchall()

    for row in rows:
        flyrutenummer = row[0]
        tid = row[1]  # departure_time/arrival_time
        airports_list = hent_alle_flyplasser_for_rute(cursor, flyrutenummer)
        airports_str = " - ".join(airports_list)

        if direction == 'D':
            print(f"Rute {flyrutenummer} har avgang kl {tid} fra {airport}, besøker: {airports_str}")
        else:
            print(f"Rute {flyrutenummer} ankommer kl {tid} til {airport}, besøker: {airports_str}")

    conn.close()


def hent_alle_flyplasser_for_rute(cursor, flyrutenummer):
    """
    Henter alle flyplasser i rekkefølge for gitt rute.
    1) startflyplass fra flyrute
    2) eventuelle mellomlandinger (sortert på MID)
    3) endeflyplass fra flyrute
    Returnerer en liste, f.eks. ['TRD', 'BGO', 'SVG'].
    """
    # startfylpass og endeflyplass
    cursor.execute("""
        SELECT startflyplass, endeflyplass
        FROM flyrute
        WHERE flyrutenummer = ?
    """, (flyrutenummer,))
    row = cursor.fetchone()
    if not row:
        return []
    start = row[0]
    end   = row[1]

    # mellomlandinger
    cursor.execute("""
        SELECT flyplasskode
        FROM mellomlanding
        WHERE flyrutenummer = ?
        ORDER BY MID
    """, (flyrutenummer,))
    mids = cursor.fetchall()  
    mellom = [m[0] for m in mids]  

    return [start] + mellom + [end]


if __name__ == "__main__":
    main()