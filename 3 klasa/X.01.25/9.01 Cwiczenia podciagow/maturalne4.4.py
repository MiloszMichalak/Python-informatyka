# Zadanie 4
print("Zadanie 4")

# todo co najmniej 50 elementow i najwieksza srednia arytmetyczna, pierwszy znajdz
# wypisz: srednia, liczba elementow, pierwszy element

file = open("liczby_przyklad.txt", "r")
ciag = list(map(int, file.readline().split()))

maksSrednia = 0
dlugosc = 0
pierwszyElement = 0

def sumaCiag(ciag):
    suma = 0
    for i in ciag:
        suma += int(i)
    return suma

def dlugoscCiag(ciag):
    dlugosc = 0
    for i in ciag:
        dlugosc += 1
    return dlugosc

for i in range(len(ciag)):
    for j in range(i + 50, len(ciag) + 1):
        podciag = ciag[i:j]
        dlugosc = dlugoscCiag(podciag)
        srednia = sumaCiag(podciag) / dlugosc
        if srednia > maksSrednia:
            maksSrednia = srednia
            maksPodciag = podciag
            pierwszyElement = ciag[i]
            dlugosc = dlugosc
            
print(f"srednia: {maksSrednia}, liczba elementow: {dlugosc}, pierwszy element: {pierwszyElement}")
