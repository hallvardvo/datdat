import sqlite3
conn = sqlite3.connect('fly.sqlite')
print("Connection successful")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE flyplass (
                    flyplasskode TEXT PRIMARY KEY,
                    flyplassnavn TEXT)""")
cursor.execute("""CREATE TABLE flyselskap (
                    flyselskapkode TEXT PRIMARY KEY,
                    navn TEXT)""")
cursor.execute("""CREATE TABLE flyprodusent (
                    navn TEXT PRIMARY KEY,
                    nasjonalitet TEXT,
                    stiftelsesår INTEGER)""")
cursor.execute("""CREATE TABLE flyvning (
                    flyrutenummer INTEGER,
                    løpenummer INTEGER,
                    avgangtid TEXT,
                    ankomsttid TEXT,
                    status TEXT,
                    PRIMARY KEY (flyrutenummer, løpenummer),
                    FOREIGN KEY (flyrutenummer) REFERENCES flyrute(flyrutenummer))""")
cursor.execute("""CREATE TABLE OpereresAv (
                    navn TEXT,
                    flyselskapkode TEXT,
                    flyrutenummer INTEGER,
                    PRIMARY KEY (navn, flyselskapkode, flyrutenummer),
                    FOREIGN KEY (navn) REFERENCES flytype(navn),
                    FOREIGN KEY (flyselskapkode) REFERENCES flyselskap(flyselskapkode),
                    FOREIGN KEY (flyrutenummer) REFERENCES flyrute(flyrutenummer))""")
cursor.execute("""CREATE TABLE flyrute (
                    flyrutenummer INTEGER PRIMARY KEY,
                    ukedagskode INTEGER,
                    oppstartsdato TEXT,
                    sluttdato TEXT,
                    planlagt_avreisetid TEXT,
                    planlagt_ankomsttid TEXT,
                    startflyplass INTEGER,
                    endeflyplass INTEGER,
                    FOREIGN KEY (startflyplass) REFERENCES flyplass(flyplasskode),
                    FOREIGN KEY (endeflyplass) REFERENCES flyplass(flyplasskode))""")
cursor.execute("""CREATE TABLE fly (
                    flyregnr TEXT PRIMARY KEY,
                    serienummer TEXT,
                    flynavn TEXT,
                    driftsår INTEGER,
                    flytypekode TEXT,
                    flyselskapkode TEXT,
                    FOREIGN KEY (flytypekode) REFERENCES flytype(navn),
                    FOREIGN KEY (flyselskapkode) REFERENCES flyselskap(flyselskapkode))""")
cursor.execute("""CREATE TABLE mellomlanding (
                    MID INTEGER PRIMARY KEY,
                    avgangstid TEXT,
                    ankomsttid TEXT,
                    flyrutenummer INTEGER,
                    flyplasskode INTEGER,
                    FOREIGN KEY (flyrutenummer) REFERENCES flyrute(flyrutenummer),
                    FOREIGN KEY (flyplasskode) REFERENCES flyplass(flyplasskode))""")
cursor.execute("""CREATE TABLE flytype (
                    navn TEXT PRIMARY KEY,
                    antallseter INTEGER,
                    førsteProduksjonsår INTEGER,
                    sistProduksjonsår INTEGER,
                    produsent TEXT,
                    FOREIGN KEY (produsent) REFERENCES flyprodusent(navn))""")


cursor.execute("""CREATE TABLE kunde (
                    kundenummer INTEGER PRIMARY KEY,
                    navn TEXT,
                    tlf INTEGER,
                    epost TEXT,
                    nasjonalitet TEXT)""")
cursor.execute("""CREATE TABLE total_bestilling (
                    referansenr INTEGER PRIMARY KEY,
                    dato TEXT,
                    totalpris INTEGER,
                    kundenummer INTEGER,
                    FOREIGN KEY (kundenummer) REFERENCES kunde(kundenummer))""")


conn.commit()
conn.close()