import sqlite3
conn = sqlite3.connect('fly.sqlite')
print("Connection successful")
cursor = conn.cursor()

# Insert flyplasser
cursor.execute("INSERT INTO flyplass VALUES ('BOO', 'Bodø Lufthavn')")
cursor.execute("INSERT INTO flyplass VALUES ('BGO', 'Bergen lufthavn, Flesland')")
cursor.execute("INSERT INTO flyplass VALUES ('OSL', 'Oslo lufthavn, Gardermoen')")
cursor.execute("INSERT INTO flyplass VALUES ('SVG', 'Stavanger lufthavn, Sola')")
cursor.execute("INSERT INTO flyplass VALUES ('TRD', 'Trondheim lufthavn, Værnes')")

#Insert flyprodusenter
cursor.execute("""INSERT INTO flyprodusent (navn, nasjonalitet, stiftelsesår) 
                VALUES ('The Boeing Company', 'Amerikansk', 1916)""")
cursor.execute("""INSERT INTO flyprodusent (navn, nasjonalitet, stiftelsesår) 
                VALUES ('Airbus Group', 'Fransk/Tysk/Spansk/Britisk', 1970)""")
cursor.execute("""INSERT INTO flyprodusent (navn, nasjonalitet, stiftelsesår) 
                VALUES ('De Havilland Canada', 'Kanadisk', 1928)""")

# Insert flytyper
cursor.execute("""INSERT INTO flytype (navn, antallseter, førsteProduksjonsår, sistProduksjonsår, produsent)
                  VALUES ('Boeing 737 800', 189, 1997, 2020, 'The Boeing Company')""")
cursor.execute("""INSERT INTO flytype (navn, antallseter, førsteProduksjonsår, sistProduksjonsår, produsent)
                  VALUES ('Airbus a320neo', 180, 2016, NULL, 'Airbus Group')""")
cursor.execute("""INSERT INTO flytype (navn, antallseter, førsteProduksjonsår, sistProduksjonsår, produsent)
                  VALUES ('Dash-8 100', 39, 1984, 2005, 'De Havilland Canada')""")
cursor.execute("INSERT INTO flyselskap (flyselskapkode, navn) VALUES ('DY', 'Norwegian')")

# Insert the four Boeing 737 800 aircraft operated by Norwegian
aircraft_data = [
    ('LN-ENU', '42069', None, 2015, 'Boeing 737 800', 'DY'),
    ('LN-ENR', '42093', 'Jan Bålsrud', 2018, 'Boeing 737 800', 'DY'),
    ('LN-NIQ', '39403', 'Max Manus', 2011, 'Boeing 737 800', 'DY'),
    ('LN-ENS', '42281', None, 2017, 'Boeing 737 800', 'DY')
]

for aircraft in aircraft_data:
    try:
        cursor.execute("""INSERT INTO fly 
                        (flyregnr, serienummer, flynavn, driftsår, flytypekode, flyselskapkode) 
                        VALUES (?, ?, ?, ?, ?, ?)""", aircraft)
    except sqlite3.Error as e:
        print(f"Error inserting aircraft {aircraft[0]}: {e}")

#Insert Sas aircrafts
sas_aircraft_data = [
    ('SE-RUB', '9518', 'Birger Viking', 2020, 'Airbus a320neo', 'SK'),
    ('SE-DIR', '11421', 'Nora Viking', 2023, 'Airbus a320neo', 'SK'),
    ('SE-RUP', '12066', 'Ragnhild Viking', 2024, 'Airbus a320neo', 'SK'),
    ('SE-RZE', '12166', 'Ebbe Viking', 2024, 'Airbus a320neo', 'SK')
]

for aircraft in sas_aircraft_data:
    try:
        cursor.execute("""INSERT INTO fly 
                        (flyregnr, serienummer, flynavn, driftsår, flytypekode, flyselskapkode) 
                        VALUES (?, ?, ?, ?, ?, ?)""", aircraft)
    except sqlite3.Error as e:
        print(f"Error inserting aircraft {aircraft[0]}: {e}")
cursor.execute("INSERT INTO flyselskap (flyselskapkode, navn) VALUES ('WF', 'Widerøe')")

# Insert Widerøe aircrafts
wideroe_aircraft_data = [
    ('LN-WIH', '383', 'Oslo', 1994, 'Dash-8 100', 'WF'),
    ('LN-WIA', '359', 'Nordland', 1993, 'Dash-8 100', 'WF'),
    ('LN-WIL', '298', 'Narvik', 1995, 'Dash-8 100', 'WF')
]

for aircraft in wideroe_aircraft_data:
    try:
        cursor.execute("""INSERT INTO fly 
                        (flyregnr, serienummer, flynavn, driftsår, flytypekode, flyselskapkode) 
                        VALUES (?, ?, ?, ?, ?, ?)""", aircraft)
    except sqlite3.Error as e:
        print(f"Error inserting aircraft {aircraft[0]}: {e}")
conn.commit()
conn.close()