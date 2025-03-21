import sqlite3

def main():
    conn = sqlite3.connect("fly.sqlite")
    cursor = conn.cursor()

    flyrutenummer = input("Oppgi flyrutenummer |WF1302|SK888|SK332|WF1311|DY753|: ").strip().upper()
    lopnummer    = input("Oppgi løpenummer: ").strip()

    flytype_navn, setekonfig_id = hent_flytype_for_rute(cursor, flyrutenummer)
    if not flytype_navn:
        print("Fant ingen flytype for rute", flyrutenummer)
        return

    radinfo = hent_radinfo(cursor, setekonfig_id)
    if not radinfo:
        print("Ingen seter i denne konfigurasjonen.")
        return

    # Finn maks radnummer for å vite hvor mange siffer vi trenger:
    max_row = max(r[0] for r in radinfo)
    max_digits = len(str(max_row))

    opptatte_seter = hent_opptatte_seter(cursor, flyrutenummer, lopnummer)
    
    antall_ledige = 0
    for (radnummer, antall_seter_i_rad, vedNodutgang) in radinfo:
        antall_ledige += skriv_oppstilling_for_rad(
            radnummer, 
            antall_seter_i_rad, 
            opptatte_seter, 
            max_digits
        )

    print(f"\nAntall opptatte seter: {len(opptatte_seter)}")
    print(f"Antall ledige seter:  {antall_ledige}")

    conn.close()




# ----------------- Ting for å gjøre at radene ser penere ut -----------------
def skriv_oppstilling_for_rad(radnummer, antall_seter_i_rad, opptatte, max_digits):
    # Generer bokstaver
    letters = generer_setebokstaver(antall_seter_i_rad)

    # Del i to blokker
    half = antall_seter_i_rad // 2
    left_letters = letters[:half]
    right_letters = letters[half:]

    left_side = []
    right_side = []

    for letter in left_letters:
        seat_raw = f"{radnummer}{letter}"
        left_side.append( formater_sete(radnummer, letter, max_digits, seat_raw in opptatte) )

    for letter in right_letters:
        seat_raw = f"{radnummer}{letter}"
        right_side.append( formater_sete(radnummer, letter, max_digits, seat_raw in opptatte) )

    # Sett sammen 
    rad_tekst = "".join(left_side) + "    " + "".join(right_side)
    print(rad_tekst)

    # Tell hvor mange som er opptatt her:
    opptatt_i_rad = 0
    for letter in letters:
        if f"{radnummer}{letter}" in opptatte:
            opptatt_i_rad += 1

    return antall_seter_i_rad - opptatt_i_rad


def formater_sete(radnummer, letter, max_digits, er_opptatt):
    """
    Formaterer seteinformasjonen til en string som kan print
    """
    seat_str = f"{radnummer:>{max_digits}}{letter}"  
    if er_opptatt:
        seat_str = " " * len(seat_str)
    return f"[{seat_str}]"
# ------------------------------------------------------------------------------




def hent_flytype_for_rute(cursor, flyrutenummer):
    sql = """
    SELECT ft.navn, ft.setekonfigurasjonID
    FROM OpereresAv oa
    JOIN flytype ft ON oa.navn = ft.navn
    WHERE oa.flyrutenummer = ?
    """
    cursor.execute(sql, (flyrutenummer,))
    row = cursor.fetchone()
    if row:
        return row[0], row[1]
    return None, None


def hent_radinfo(cursor, setekonfig_id):
    sql = """
    SELECT radnummer, antallseter, vedNødutgang
    FROM setekonf_rad
    WHERE setekonfigurasjonID = ?
    ORDER BY radnummer
    """
    cursor.execute(sql, (setekonfig_id,))
    return cursor.fetchall()


def hent_opptatte_seter(cursor, flyrutenummer, lopnummer):
    sql = """
    SELECT d.valgtsete
    FROM billetter b
    JOIN delreise d ON (b.referansenr = d.referansenr AND b.nummer = d.nummer)
    WHERE b.flyrutenummer = ?
        AND b.løpenummer = ?
        AND d.valgtsete IS NOT NULL
    """
    cursor.execute(sql, (flyrutenummer, lopnummer))
    rows = cursor.fetchall()
    return {r[0] for r in rows if r[0]}


def generer_setebokstaver(antall_seter_i_rad):
    import string
    return list(string.ascii_uppercase[:antall_seter_i_rad])


if __name__ == "__main__":
    main()
