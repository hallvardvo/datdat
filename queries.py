import sqlite3
conn = sqlite3.connect('fly.sqlite')
print("Connection successful")
cursor = conn.cursor()


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





# 5)
cursor.execute("""SELECT
    flyselskap.navn AS Flyselskap,
    flytype.navn AS Flytype,
    COUNT(fly.flyregnr) AS "Antall Fly"
FROM fly
JOIN flyselskap 
    ON fly.flyselskapkode = flyselskap.flyselskapkode
JOIN flytype
    ON fly.flytypekode = flytype.navn
GROUP BY
    flyselskap.navn,
    flytype.navn
ORDER BY
    flyselskap.navn,
    flytype.navn;
    """)


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


