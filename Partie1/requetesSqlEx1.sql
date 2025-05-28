-- Afficher la liste des réservations avec le nom du client et la ville de l’hôtel réservé. 

SELECT R.Id_Reservation, C.Nom_complet, H.Ville
FROM Reservation R
JOIN Client C ON R.Id_Client = C.Id_Client
JOIN Chambre CH ON CH.Id_Chambre = R.Id_Reservation
JOIN Hotel H ON CH.Id_Hotel = H.Id_Hotel;

--Afficher les clients qui habitent à Paris.

SELECT * FROM Client WHERE Ville = 'Paris';

-- Calculer le nombre de réservations faites par chaque client.

SELECT C.Nom_complet, COUNT(*) AS Nombre_Reservations
FROM Reservation R
JOIN Client C ON R.Id_Client = C.Id_Client
GROUP BY C.Id_Client;

-- Donner le nombre de chambres pour chaque type de chambre.

SELECT TC.Type, COUNT(*) AS Nombre_Chambres
FROM Chambre C
JOIN Type_Chambre TC ON C.Id_Type = TC.Id_Type
GROUP BY TC.Type;

--Afficher la liste des chambres qui ne sont pas réservées pour une période donnée (entre deux dates saisies par l’utilisateur). 

SELECT *
FROM Chambre
WHERE Id_Chambre NOT IN (
    SELECT Id_Reservation
    FROM Reservation
    WHERE (Date_arrivee < @dateFin AND Date_depart > @dateDebut)
);