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

cursor.execute("""CREATE TABLE flytype (
                    navn TEXT PRIMARY KEY,
                    antallseter INTEGER,
                    førsteProduksjonsår INTEGER,
                    sistProduksjonsår INTEGER,
                    produsent TEXT,
                    FOREIGN KEY (produsent) REFERENCES flyprodusent(navn))""")

# Create flyrute with TEXT flyrutenummer
cursor.execute("""CREATE TABLE flyrute (
                    flyrutenummer TEXT PRIMARY KEY,
                    ukedagskode INTEGER,
                    oppstartsdato TEXT,
                    sluttdato TEXT,
                    planlagt_avreisetid TEXT,
                    planlagt_ankomsttid TEXT,
                    startflyplass TEXT,
                    endeflyplass TEXT,
                    FOREIGN KEY (startflyplass) REFERENCES flyplass(flyplasskode),
                    FOREIGN KEY (endeflyplass) REFERENCES flyplass(flyplasskode))""")

# Create remaining tables with TEXT flyrutenummer
cursor.execute("""CREATE TABLE flyvning (
                    flyrutenummer TEXT,
                    løpenummer INTEGER,
                    avgangtid TEXT,
                    ankomsttid TEXT,
                    status TEXT,
                    PRIMARY KEY (flyrutenummer, løpenummer),
                    FOREIGN KEY (flyrutenummer) REFERENCES flyrute(flyrutenummer))""")

cursor.execute("""CREATE TABLE OpereresAv (
                    navn TEXT,
                    flyselskapkode TEXT,
                    flyrutenummer TEXT,
                    PRIMARY KEY (navn, flyselskapkode, flyrutenummer),
                    FOREIGN KEY (navn) REFERENCES flytype(navn),
                    FOREIGN KEY (flyselskapkode) REFERENCES flyselskap(flyselskapkode),
                    FOREIGN KEY (flyrutenummer) REFERENCES flyrute(flyrutenummer))""")

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
                    flyrutenummer TEXT,
                    flyplasskode TEXT,
                    FOREIGN KEY (flyrutenummer) REFERENCES flyrute(flyrutenummer),
                    FOREIGN KEY (flyplasskode) REFERENCES flyplass(flyplasskode))""")

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

cursor.execute("""CREATE TABLE billettype (
                    flyrutenummer TEXT,
                    billetttype TEXT,
                    pris INTEGER,
                    PRIMARY KEY (flyrutenummer, billetttype),
                    FOREIGN KEY (flyrutenummer) REFERENCES flyrute(flyrutenummer))""")

cursor.execute("""CREATE TABLE billetter (
                    referansenr INTEGER,
                    nummer INTEGER,
                    billetttype TEXT,
                    flyrutenummer TEXT,
                    løpenummer INTEGER,
                    DRID INTEGER,
                    PRIMARY KEY (referansenr, nummer),
                    FOREIGN KEY (referansenr) REFERENCES total_bestilling(referansenr),
                    FOREIGN KEY (flyrutenummer, billetttype) REFERENCES billettype(flyrutenummer, billetttype),
                    FOREIGN KEY (flyrutenummer, løpenummer) REFERENCES flyvning(flyrutenummer, løpenummer))""")

cursor.execute("""CREATE TABLE delreise (
                    DRID INTEGER PRIMARY KEY,
                    valgtsete TEXT,
                    referansenr INTEGER,
                    nummer INTEGER,
                    FOREIGN KEY (referansenr, nummer) REFERENCES billetter(referansenr, nummer))""")

cursor.execute("""CREATE TABLE harDelReise (
                    DRID INTEGER,
                    flyrutenummer TEXT,
                    PRIMARY KEY (DRID, flyrutenummer),
                    FOREIGN KEY (DRID) REFERENCES delreise(DRID),
                    FOREIGN KEY (flyrutenummer) REFERENCES flyrute(flyrutenummer))""")

cursor.execute("""CREATE TABLE flyselskapharflytype (
                    flyselskapkode TEXT,
                    navn TEXT,
                    PRIMARY KEY (flyselskapkode, navn),
                    FOREIGN KEY (flyselskapkode) REFERENCES flyselskap(flyselskapkode),
                    FOREIGN KEY (navn) REFERENCES flytype(navn))""")              

cursor.execute("""CREATE TABLE innsjekket_bagasje (
                    DRID INTEGER,
                    regnr TEXT,
                    vekt REAL,
                    innleveringstidspunkt TEXT,
                    kundenummer INTEGER,
                    PRIMARY KEY (DRID, regnr),
                    FOREIGN KEY (DRID) REFERENCES delreise(DRID),
                    FOREIGN KEY (kundenummer) REFERENCES kunde(kundenummer))""")

cursor.execute("""CREATE TABLE fordelsprogram (
                    flyselskapkode TEXT,
                    referanse TEXT,
                    kundenummer INTEGER,
                    PRIMARY KEY (flyselskapkode, kundenummer),
                    FOREIGN KEY (flyselskapkode) REFERENCES flyselskap(flyselskapkode),
                    FOREIGN KEY (kundenummer) REFERENCES kunde(kundenummer))""")

cursor.execute("""CREATE TABLE harflyvning (
                    flyrutenummer TEXT,
                    løpenummer INTEGER,
                    referansenr INTEGER,
                    PRIMARY KEY (flyrutenummer, løpenummer, referansenr),
                    FOREIGN KEY (flyrutenummer, løpenummer) REFERENCES flyvning(flyrutenummer, løpenummer),
                    FOREIGN KEY (referansenr) REFERENCES total_bestilling(referansenr))""")

conn.commit()
conn.close()