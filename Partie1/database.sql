CREATE DATABASE HotelDB;

USE HotelDB;

CREATE TABLE Hotel (
    Id_Hotel INT PRIMARY KEY,
    Ville VARCHAR(50),
    Pays VARCHAR(50),
    Code_postal INT
);

CREATE TABLE Client (
    Id_Client INT PRIMARY KEY,
    Adresse VARCHAR(100),
    Ville VARCHAR(50),
    Code_postal INT,
    Email VARCHAR(100),
    Numero_telephone VARCHAR(20),
    Nom_complet VARCHAR(100)
);

CREATE TABLE Prestation (
    Id_Prestation INT PRIMARY KEY,
    Prix DECIMAL(10,2),
    Description TEXT
);

CREATE TABLE Type_Chambre (
    Id_Type INT PRIMARY KEY,
    Type VARCHAR(50),
    Tarif DECIMAL(10,2)
);

CREATE TABLE Chambre (
    Id_Chambre INT PRIMARY KEY,
    Numero INT,
    Etage INT,
    Fumeurs BOOLEAN,
    Id_Type INT,
    Id_Hotel INT,
    FOREIGN KEY (Id_Type) REFERENCES Type_Chambre(Id_Type),
    FOREIGN KEY (Id_Hotel) REFERENCES Hotel(Id_Hotel)
);

CREATE TABLE Reservation (
    Id_Reservation INT PRIMARY KEY,
    Date_arrivee DATE,
    Date_depart DATE,
    Id_Client INT,
    FOREIGN KEY (Id_Client) REFERENCES Client(Id_Client)
);

CREATE TABLE Evaluation (
    Id_Evaluation INT PRIMARY KEY,
    Date_arrivee DATE,
    La_note INT,
    Texte_descriptif TEXT,
    Id_Client INT,
    FOREIGN KEY (Id_Client) REFERENCES Client(Id_Client)
);
