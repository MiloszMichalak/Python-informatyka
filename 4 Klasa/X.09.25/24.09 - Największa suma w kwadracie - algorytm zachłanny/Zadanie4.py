# Napisz program, który wczyta macierz M z pliku macierz.txt i wypisze maksymalną sumę oraz indeksy wybieranych
# komórek w osobnych wierszach rozdzielone spacjami.

file = open("macierz.txt", "r")
maciorka = []
n = 0
for line in file:
    maciorka.append(list(map(int, line.split())))
file.close()

indeksy = {}

suma = maciorka[0][0]
i = 0
j = 0
while i < n - 1 or j < n - 1:
    if i == n - 1:
        j += 1
        indeksy.update({i: j})
    elif j == n - 1:
        i += 1
        indeksy.update({i: j})
    elif maciorka[i + 1][j] > maciorka[i][j + 1]:
        i += 1
        indeksy.update({i: j})
    else:
        j += 1
        indeksy.update({i: j})
    suma += maciorka[i][j]

for wiersz in maciorka:
    for wartosc in wiersz:
        print(wartosc, end="\t")
    print()

print("Maksymalna suma:", suma)
for key, value in indeksy.items():
    print(key, value)
