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
            
            # Print segment prices for documentation
            print(f"\n📝 Segment prices for {route['route_num']} (not directly stored in database):")
            print(f"  {route['start_airport']}-{route['stopover']['airport']} segment:")
            for price_type, price in route['stopover']['segments'][f"{route['start_airport']}-{route['stopover']['airport']}"]:
                print(f"    - {price_type}: {price} NOK")
            
            print(f"  {route['stopover']['airport']}-{route['end_airport']} segment:")
            for price_type, price in route['stopover']['segments'][f"{route['stopover']['airport']}-{route['end_airport']}"]:
                print(f"    - {price_type}: {price} NOK")
        
        print(f"✅ Route {route['route_num']} inserted successfully")
        
    except sqlite3.Error as e:
        print(f"❌ Error inserting route {route['route_num']}: {e}")

conn.commit()
conn.close()
print("\n✅ All routes and aircraft data inserted successfully")