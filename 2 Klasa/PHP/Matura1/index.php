<?php

$user = "root";
$password = "";
$server = "localhost";
$baza = "taryfikator";

$connection = new mysqli($server, $user, $password, $baza);

$zapytanie = "";

if ($wynik = $connection -> query($zapytanie)) {
    while ($row = $wynik -> fetch_array()) {
        echo $row["kierowcy_txt"];
    }
} else {
    echo $connection -> error." ".$connection -> errno;
}

$connection->close();
