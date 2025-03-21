# Oppgave 5

import sqlite3
conn = sqlite3.connect('fly.sqlite')
print("Connection successful")
cursor = conn.cursor()

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

results = cursor.fetchall()

column_names = [description[0] for description in cursor.description]

print("\nQuery Results:")
print("-" * 50)
print(f"{column_names[0]:<15} {column_names[1]:<20} {column_names[2]:<10}")
print("-" * 50)

for row in results:
    print(f"{row[0]:<15} {row[1]:<20} {row[2]:<10}")

print("-" * 50)
print(f"Total results: {len(results)}")

conn.close()