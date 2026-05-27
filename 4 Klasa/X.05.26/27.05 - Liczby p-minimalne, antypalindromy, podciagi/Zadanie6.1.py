def znajdzMax(liczba):
    maksik = int(liczba[0])
    for number in liczba:
        if int(number) > maksik:
            maksik = int(number)
    return maksik

file = open("dane6.txt")
lista = []
for liczba in file:
    lista.append(liczba.strip())

listaP = [0] * 11

for line in lista:
    listaP[znajdzMax(line) + 1] += 1

for i in range(2, 11):
    print(i, "\t", listaP[i])
