# 🏨 Projet de Gestion de Réservations d’Hôtel
Ce projet est une application web développée avec **Python**, **SQLite** et **Streamlit**, permettant de gérer les réservations d’un hôtel.
---

## 🚀 Fonctionnalités
1. 🗓️ Consulter la liste des réservations  
2. 👤 Consulter la liste des clients  
3. 🛏️ Consulter les chambres disponibles sur une période donnée  
4. ➕ Ajouter un client  
5. 📅 Ajouter une réservation  

---

## 🛠️ Technologies
- **Python** 🐍  
- **SQLite** 🗃️ pour la base de données  
- **Streamlit** 🌐 pour l’interface web
  
---

## ▶️ Lancer le projet
🎥 **Vidéo explicative du projet**  
👉 [Voir la démo ici](https://youtu.be/LUmNO7VfF9E)
---

## 📂 Structure du projet

```text
projet-DB/
│
├── Partie1/                         # Création de la base de données
│   ├── database.sql                 # Script de création des tables
│   ├── jeuDEnregistrement.sql      # Jeu d’insertion de données
│   ├── requetesSqlEx1.sql          # Requêtes SQL d'exploitation
│   └── requetesEnalgeberelationnelle.pdf  # Modélisation PDF
│
├── Partie2/                         # Interface Streamlit
│   ├── app.py                       # Interface graphique avec Streamlit
│   └── init_db.py                   # Initialisation de la base de données SQLite
│
├── README.md                        # Documentation du projet
└── .idea/                           # Fichiers de configuration IDE (à ignorer)




### 1. Installer les dépendances :
```bash
pip install streamlit
streamlit run app.py``` 
