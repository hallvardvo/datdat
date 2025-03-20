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
