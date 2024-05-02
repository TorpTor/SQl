import csv
import hashlib
import sqlite3

# Definerer en funksjon for å opprette en ny database
def opprett_database():
    # Oppretter en kobling til databasen
    conn = sqlite3.connect('random.csv')

    # Oppretter en kursort for å kjøre SQL-kommandoer
    c = conn.cursor()

    # Oppretter tabellen "brukere"
    c.execute('''
        CREATE TABLE IF NOT EXISTS brukere (
            id INTEGER PRIMARY KEY,
            fornavn TEXT NOT NULL,
            etternavn TEXT NOT NULL,
            epost TEXT NOT NULL UNIQUE,
            passord TEXT NOT NULL
        )
    ''')

    # Lagrer endringene
    conn.commit()

    # Lukker koblingen
    conn.close()

# Definerer en funksjon for å laste inn data fra en CSV-fil
def last_inn_csv(filnavn):
    # Oppretter en kobling til databasen
    conn = sqlite3.connect('random.csv')

    # Oppretter en kursort for å kjøre SQL-kommandoer
    c = conn.cursor()

    # Åpner CSV-filen
    with open(filnavn, 'r') as f:
        # Leser inn filen linje for linje
        for linje in f:
            # Deler linjen opp i felt
            felt = linje.strip().split(',')

            # Henter verdiene fra felt
            fornavn = felt[0]
            etternavn = felt[1]
            epost = felt[2]
            passord = felt[3]

            # Krypterer passordet
            kryptert_passord = hashlib.sha256(passord.encode()).hexdigest()

            # Legger til brukeren i databasen
            c.execute('''
                INSERT INTO brukere (fornavn, etternavn, epost, passord)
                VALUES (?, ?, ?, ?)
            ''', (fornavn, etternavn, epost, kryptert_passord))

    # Lagrer endringene
    conn.commit()

    # Lukker koblingen
    conn.close()

# Definerer en funksjon for å slette alle brukere i databasen
def slett_alle_brukere():
    # Oppretter en kobling til databasen
    conn = sqlite3.connect('database.db')

    # Oppretter en kursort for å kjøre SQL-kommandoer
    c = conn.cursor()

    # Sletter alle brukere i tabellen "brukere"
    c.execute('DELETE FROM brukere')

    # Lagrer endringene
    conn.commit()

    # Lukker koblingen
    conn.close()

# Definerer en funksjon for å starte på nytt
def start_pa():
    # Oppretter en kobling til databasen
    conn = sqlite3.connect('database.db')

    # Oppretter en kursort for å kjøre SQL-kommandoer
    c = conn.cursor()

    # Sletter tabellen "brukere"
    c.execute('DROP TABLE IF EXISTS brukere')

    # Lagrer endringene
    conn.commit()

    # Lukker koblingen
    conn.close()
