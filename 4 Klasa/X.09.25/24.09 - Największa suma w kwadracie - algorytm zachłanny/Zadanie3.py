import random

n = 5
maciorka = [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]

suma = maciorka[0][0]
i = 0
j = 0
while i < n - 1 or j < n - 1:
    if i == n - 1:
        j += 1
    elif j == n - 1:
        i += 1
    elif maciorka[i + 1][j] > maciorka[i][j + 1]:
        i += 1
    else:
        j += 1
    suma += maciorka[i][j]

print("Macierz:")
for wiersz in maciorka:
    for wartosc in wiersz:
        print(wartosc, end="\t")
    print()

print("Maksymalna suma:", suma)

