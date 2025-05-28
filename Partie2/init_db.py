import sqlite3

# Connexion / création de la base
conn = sqlite3.connect("hotel.db")
cursor = conn.cursor()

# Création des tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS Client (
    Id_Client INTEGER PRIMARY KEY AUTOINCREMENT,
    Nom TEXT NOT NULL,
    Prenom TEXT NOT NULL,
    Email TEXT,
    Telephone TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Chambre (
    Id_Chambre INTEGER PRIMARY KEY AUTOINCREMENT,
    Numero TEXT NOT NULL,
    Type TEXT,
    Prix REAL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Reservation (
    Id_Reservation INTEGER PRIMARY KEY AUTOINCREMENT,
    Date_arrivee DATE NOT NULL,
    Date_depart DATE NOT NULL,
    Id_Client INTEGER,
    Id_Chambre INTEGER,
    FOREIGN KEY (Id_Client) REFERENCES Client(Id_Client),
    FOREIGN KEY (Id_Chambre) REFERENCES Chambre(Id_Chambre)
);
""")

# Exemple de données
cursor.execute("INSERT INTO Chambre (Numero, Type, Prix) VALUES ('101', 'Simple', 50.0)")
cursor.execute("INSERT INTO Chambre (Numero, Type, Prix) VALUES ('102', 'Double', 75.0)")
cursor.execute("INSERT INTO Chambre (Numero, Type, Prix) VALUES ('201', 'Suite', 120.0)")

conn.commit()
conn.close()
