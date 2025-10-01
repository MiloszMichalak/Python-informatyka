file = open("macierz.txt", "r")
maciorka = []
for line in file:
    maciorka.append(list(map(int, line.split())))
file.close()
n = len(maciorka)

indeksy = []

suma = maciorka[0][0]
i = 0
j = 0
while i < n - 1 or j < n - 1:
    indeksy.append([i, j])
    if i == n - 1:
        j += 1
    elif j == n - 1:
        i += 1
    elif maciorka[i + 1][j] > maciorka[i][j + 1]:
        i += 1
    else:
        j += 1
    suma += maciorka[i][j]
indeksy.append([i, j])

for wiersz in maciorka:
    for wartosc in wiersz:
        print(wartosc, end="\t")
    print()
    
print(suma)

for row in indeksy:
    print(row[0], row[1])