def znajdzMax(liczba):
    maksik = int(liczba[0])
    for number in liczba:
        if int(number) > maksik:
            maksik = int(number)
    return maksik

def sumaCyfr(liczba):
    suma = 0
    for number in liczba:
        suma += int(number)

    return suma

file = open("dane6przyklad.txt")
lista = []
for liczba in file:
    lista.append(liczba.strip())

cyfry = [0] * 11
cyfryWypisane = [0] * 11

for line in lista:
    system = znajdzMax(line) + 1
    obecnaLiczba = cyfry[system]
    sumaCyfer = sumaCyfr(line)
    if sumaCyfer > obecnaLiczba:
        cyfry[system] = sumaCyfer
        cyfryWypisane[system] = line


for i in range(2, 11):
    print(i, "\t", cyfryWypisane[i])