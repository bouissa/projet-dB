import streamlit as st 
import sqlite3
from datetime import datetime

# Connexion à la base
conn = sqlite3.connect("hotel.db")
cursor = conn.cursor()

st.title("🏨 Gestion des réservations d’hôtel")

menu = st.sidebar.selectbox("Menu", [
    "Liste des réservations",
    "Liste des clients",
    "Chambres disponibles",
    "Ajouter un client",
    "Ajouter une réservation"
])

# 1. Liste des réservations
if menu == "Liste des réservations":
    st.header("📋 Liste des réservations")
    query = """
    SELECT R.Id_Reservation, R.Date_arrivee, R.Date_depart,
           C.Nom || ' ' || C.Prenom AS Client,
           CH.Numero AS Chambre
    FROM Reservation R
    JOIN Client C ON R.Id_Client = C.Id_Client
    JOIN Chambre CH ON R.Id_Chambre = CH.Id_Chambre
    """
    result = cursor.execute(query).fetchall()
    st.table(result)

# 2. Liste des clients
elif menu == "Liste des clients":
    st.header("👤 Liste des clients")
    result = cursor.execute("SELECT * FROM Client").fetchall()
    st.table(result)

# 3. Chambres disponibles
elif menu == "Chambres disponibles":
    st.header("🏘️ Chambres disponibles")
    date_debut = st.date_input("Date d'arrivée")
    date_fin = st.date_input("Date de départ")

    if date_debut < date_fin:
        query = """
        SELECT * FROM Chambre
        WHERE Id_Chambre NOT IN (
            SELECT Id_Chambre FROM Reservation
            WHERE NOT (Date_depart <= ? OR Date_arrivee >= ?)
        )
        """
        result = cursor.execute(query, (date_debut, date_fin)).fetchall()
        st.table(result)
    else:
        st.warning("La date d'arrivée doit être avant la date de départ.")

# 4. Ajouter un client
elif menu == "Ajouter un client":
    st.header("➕ Ajouter un client")
    nom = st.text_input("Nom")
    prenom = st.text_input("Prénom")
    email = st.text_input("Email")
    telephone = st.text_input("Téléphone")

    if st.button("Ajouter"):
        cursor.execute("INSERT INTO Client (Nom, Prenom, Email, Telephone) VALUES (?, ?, ?, ?)",
                       (nom, prenom, email, telephone))
        conn.commit()
        st.success("Client ajouté avec succès !")

# 5. Ajouter une réservation
elif menu == "Ajouter une réservation":
    st.header("📝 Ajouter une réservation")

    clients = cursor.execute("SELECT Id_Client, Nom || ' ' || Prenom FROM Client").fetchall()
    chambres = cursor.execute("SELECT Id_Chambre, Numero FROM Chambre").fetchall()

    client = st.selectbox("Client", clients, format_func=lambda x: x[1])
    chambre = st.selectbox("Chambre", chambres, format_func=lambda x: x[1])
    date_arrivee = st.date_input("Date d'arrivée")
    date_depart = st.date_input("Date de départ")

    if st.button("Réserver"):
        if date_arrivee >= date_depart:
            st.error("Date d'arrivée doit être avant la date de départ.")
        else:
            # Vérification de disponibilité
            query = """
            SELECT * FROM Reservation
            WHERE Id_Chambre = ? AND NOT (Date_depart <= ? OR Date_arrivee >= ?)
            """
            conflicts = cursor.execute(query, (chambre[0], date_arrivee, date_depart)).fetchall()

            if conflicts:
                st.error("Cette chambre est déjà réservée pour cette période.")
            else:
                cursor.execute(
                    "INSERT INTO Reservation (Date_arrivee, Date_depart, Id_Client, Id_Chambre) VALUES (?, ?, ?, ?)",
                    (date_arrivee, date_depart, client[0], chambre[0])
                )
                conn.commit()
                st.success("Réservation enregistrée !")
