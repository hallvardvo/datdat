# Oppgave 1, 2, 3, 4, og 7

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

# Insert setekonfigurasjoner
cursor.execute("""INSERT INTO setekonfigurasjon (ID, antallseter, antallrader)
                VALUES (1, 186, 31)""")
cursor.execute("""INSERT INTO setekonfigurasjon (ID, antallseter, antallrader)
                VALUES (2, 180, 30)""")
cursor.execute("""INSERT INTO setekonfigurasjon (ID, antallseter, antallrader)
                VALUES (3, 38, 10)""")

# Insert setekonf_rad for Boeing 737 800
for row in range(1, 32):
    erNødutgang = (row == 13)
    cursor.execute("""INSERT INTO setekonf_rad (setekonfigurasjonID, radnummer, antallseter, vedNødutgang)
                    VALUES (1, ?, ?, ?)""", (row, 6, erNødutgang))

# Insert setekonf_rad for Airbus a320neo
for row in range(1, 31):
    erNødutgang = (row == 11 or row == 12)
    cursor.execute("""INSERT INTO setekonf_rad (setekonfigurasjonID, radnummer, antallseter, vedNødutgang)
                    VALUES (2, ?, ?, ?)""", (row, 6, erNødutgang))

# Insert setekonf_rad for Dash-8 100
cursor.execute("""INSERT INTO setekonf_rad (setekonfigurasjonID, radnummer, antallseter, vedNødutgang)
                    VALUES (3, ?, ?, ?)""", (1, 4, False))
for row in range(2, 11):
    erNødutgang = (row == 5)
    cursor.execute("""INSERT INTO setekonf_rad (setekonfigurasjonID, radnummer, antallseter, vedNødutgang)
                    VALUES (3, ?, ?, ?)""", (row, 4, erNødutgang))

# Insert flytyper
cursor.execute("""INSERT INTO flytype (navn, setekonfigurasjonID, førsteProduksjonsår, sistProduksjonsår, produsent)
                  VALUES ('Boeing 737 800', 1, 1997, 2020, 'The Boeing Company')""")
cursor.execute("""INSERT INTO flytype (navn, setekonfigurasjonID, førsteProduksjonsår, sistProduksjonsår, produsent)
                  VALUES ('Airbus a320neo', 2, 2016, NULL, 'Airbus Group')""")
cursor.execute("""INSERT INTO flytype (navn, setekonfigurasjonID, førsteProduksjonsår, sistProduksjonsår, produsent)
                  VALUES ('Dash-8 100', 3, 1984, 2005, 'De Havilland Canada')""")
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
cursor.execute("INSERT INTO flyselskap (flyselskapkode, navn) VALUES ('SK', 'SAS')")
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

# Insert flyruter
routes = [
    {
        'route_num': 'WF1311',
        'weekday_code': '12345',
        'start_airport': 'TRD',
        'end_airport': 'BOO',
        'departure_time': '15:15',
        'arrival_time': '16:20',
        'aircraft_type': 'Dash-8 100',
        'airline_code': 'WF',
        'prices': [
            ('premium', 2018),
            ('økonomi', 899),
            ('budsjett', 599)
        ],
        'has_stopover': False
    },
    {
        'route_num': 'WF1302',
        'weekday_code': '12345',
        'start_airport': 'BOO',
        'end_airport': 'TRD',
        'departure_time': '07:35',
        'arrival_time': '08:40',
        'aircraft_type': 'Dash-8 100',
        'airline_code': 'WF',
        'prices': [
            ('premium', 2018),
            ('økonomi', 899),
            ('budsjett', 599)
        ],
        'has_stopover': False
    },
    {
        'route_num': 'DY753',
        'weekday_code': '1234567',
        'start_airport': 'TRD',
        'end_airport': 'OSL',
        'departure_time': '10:20',
        'arrival_time': '11:15',
        'aircraft_type': 'Boeing 737 800',
        'airline_code': 'DY',
        'prices': [
            ('premium', 1500),
            ('økonomi', 1000),
            ('budsjett', 500)
        ],
        'has_stopover': False
    },
    {
        'route_num': 'SK332',
        'weekday_code': '1234567',
        'start_airport': 'OSL',
        'end_airport': 'TRD',
        'departure_time': '08:00',
        'arrival_time': '09:05',
        'aircraft_type': 'Airbus a320neo',
        'airline_code': 'SK',
        'prices': [
            ('premium', 1500),
            ('økonomi', 1000),
            ('budsjett', 500)
        ],
        'has_stopover': False
    },
    {
        'route_num': 'SK888',
        'weekday_code': '12345',
        'start_airport': 'TRD',
        'end_airport': 'SVG',
        'departure_time': '10:00',
        'arrival_time': '12:10',
        'aircraft_type': 'Airbus a320neo',
        'airline_code': 'SK',
        'prices': [
            ('premium', 2200),
            ('økonomi', 1700),
            ('budsjett', 1000)
        ],
        'has_stopover': True,
        'stopover': {
            'airport': 'BGO',
            'arrival': '11:10',
            'departure': '11:40',
            'segments': {
                'TRD-BGO': [
                    ('premium', 2000),
                    ('økonomi', 1500),
                    ('budsjett', 800)
                ],
                'BGO-SVG': [
                    ('premium', 1000),
                    ('økonomi', 700),
                    ('budsjett', 350)
                ]
            }
        }
    }
]

# Insert each route
for route in routes:
    try:
        # Insert the flight route
        cursor.execute("""
            INSERT INTO flyrute (
                flyrutenummer, ukedagskode, oppstartsdato, sluttdato, 
                planlagt_avreisetid, planlagt_ankomsttid, startflyplass, endeflyplass
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            route['route_num'],
            route['weekday_code'],
            '2024-03-01',
            '2025-12-31', 
            route['departure_time'],
            route['arrival_time'],
            route['start_airport'],
            route['end_airport']
        ))
        
        # Insert price categories
        for price_type, price in route['prices']:
            cursor.execute("""
                INSERT INTO billettype (flyrutenummer, billetttype, pris)
                VALUES (?, ?, ?)
            """, (route['route_num'], price_type, price))
        
        # Link the route to aircraft type and airline
        cursor.execute("""
            INSERT INTO OpereresAv (navn, flyselskapkode, flyrutenummer)
            VALUES (?, ?, ?)
        """, (route['aircraft_type'], route['airline_code'], route['route_num']))
        
        # Handle stopover if present
        if route['has_stopover']:
            cursor.execute("""
                INSERT INTO mellomlanding (
                    avgangstid, ankomsttid, flyrutenummer, flyplasskode
                ) VALUES (?, ?, ?, ?)
            """, (
                route['stopover']['departure'],
                route['stopover']['arrival'],
                route['route_num'],
                route['stopover']['airport']
            ))
            
            

# 4)
cursor.execute("""INSERT INTO flyvning (flyrutenummer, løpenummer, avgangtid, ankomsttid, status)
VALUES (
    'SK888',
    1,
    '2025-04-01 12:00',
    '2025-04-01 14:20',
    'SCHEDULED'
);""")


cursor.execute("""INSERT INTO flyvning (flyrutenummer, løpenummer, avgangtid, ankomsttid, status)
VALUES (
    'WF1302',
    1,
    '2025-04-01 07:35',
    '2025-04-01 08:40',
    'SCHEDULED'
);""")

cursor.execute("""INSERT INTO flyvning (flyrutenummer, løpenummer, avgangtid, ankomsttid, status)
VALUES (
    'DY753',
    1,
    '2025-04-01 10:20',
    '2025-04-01 11:15',
    'SCHEDULED'
);""")

# 7)
cursor.execute("""INSERT INTO kunde (kundenummer, navn, tlf, epost, nasjonalitet)
VALUES 
(1337, 'Hallvard Vatnar Olsen', '97790743', 'hallvvo@stud.ntnu.no', 'Norsk');""")

cursor.execute("""INSERT INTO total_bestilling (referansenr, dato, totalpris, kundenummer)
VALUES
 (2001, '2025-03-20', 899, 1337),
 (2002, '2025-03-20', 899, 1337),
 (2003, '2025-03-20', 899, 1337),
 (2004, '2025-03-20', 899, 1337),
 (2005, '2025-03-20', 899, 1337),
 (2006, '2025-03-20', 899, 1337),
 (2007, '2025-03-20', 899, 1337),
 (2008, '2025-03-20', 899, 1337),
 (2009, '2025-03-20', 899, 1337),
 (2010, '2025-03-20', 899, 1337);""")

cursor.execute("""INSERT INTO billetter (
    referansenr, 
    nummer, 
    billetttype, 
    flyrutenummer, 
    løpenummer, 
    DRID
)
VALUES
 (2001, 1, 'økonomi', 'WF1302', 1, 2001),
 (2002, 1, 'økonomi', 'WF1302', 1, 2002),
 (2003, 1, 'økonomi', 'WF1302', 1, 2003),
 (2004, 1, 'økonomi', 'WF1302', 1, 2004),
 (2005, 1, 'økonomi', 'WF1302', 1, 2005),
 (2006, 1, 'økonomi', 'WF1302', 1, 2006),
 (2007, 1, 'økonomi', 'WF1302', 1, 2007),
 (2008, 1, 'økonomi', 'WF1302', 1, 2008),
 (2009, 1, 'økonomi', 'WF1302', 1, 2009),
 (2010, 1, 'økonomi', 'WF1302', 1, 2010);""")


cursor.execute("""INSERT INTO delreise (DRID, valgtsete, referansenr, nummer)
VALUES
 (2001, '4A', 2001, 1),
 (2002, '4B', 2002, 1),
 (2003, '5A', 2003, 1),
 (2004, '5B', 2004, 1),
 (2005, '6A', 2005, 1),
 (2006, '6B', 2006, 1),
 (2007, '7A', 2007, 1),
 (2008, '7B', 2008, 1),
 (2009, '8A', 2009, 1),
 (2010, '8B', 2010, 1);
""")

# Add entries to harDelReise to link journey segments to flight routes
cursor.execute("""
INSERT INTO harDelReise (DRID, flyrutenummer)
VALUES
 (2001, 'WF1302'),
 (2002, 'WF1302'),
 (2003, 'WF1302'),
 (2004, 'WF1302'),
 (2005, 'WF1302'),
 (2006, 'WF1302'),
 (2007, 'WF1302'),
 (2008, 'WF1302'),
 (2009, 'WF1302'),
 (2010, 'WF1302');
""")

conn.commit()
conn.close()
print("\n✅ All routes and aircraft data inserted successfully")