<?php

$user = "root";
$password = "";
$server = "localhost";
$baza = "taryfikator";

$connection = new mysqli($server, $user, $password, $baza);

$wynik = $connection->query("SELECT kierowcy_txt.Imie, kierowcy_txt.Nazwisko, SUM(taryfikator_txt.Kwota) as Suma
FROM kierowcy_txt 
INNER JOIN rejestr_txt ON kierowcy_txt.IdOsoby = rejestr_txt.IdOsoby
INNER JOIN taryfikator_txt ON taryfikator_txt.IdWykroczenia = rejestr_txt.IdWykroczenia
GROUP BY kierowcy_txt.IdOsoby ORDER BY Suma DESC LIMIT 1");

echo "Zadanie1"."<br>";
while ($row = $wynik -> fetch_array()) {
    echo $row["Imie"]." ".$row["Nazwisko"]." ".$row["Suma"]."<br>";
}

$wynik = $connection->query("SELECT MONTH(rejestr_txt.Data) as Miesiac, Sum(taryfikator_txt.Punkty) as Punkty
FROM rejestr_txt 
INNER JOIN taryfikator_txt ON rejestr_txt.IdWykroczenia = taryfikator_txt.IdWykroczenia AND taryfikator_txt.IdWykroczenia BETWEEN 3 AND 6
GROUP BY Miesiac 
ORDER BY Punkty DESC
LIMIT 1;");

echo "Zadanie2"."<br>";
while ($row = $wynik -> fetch_array()) {
    echo $row["Miesiac"]." ".$row["Punkty"]."<br>";
}

$connection->close();
