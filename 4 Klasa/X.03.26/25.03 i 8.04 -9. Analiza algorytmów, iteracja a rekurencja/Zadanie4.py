# Zadanie 4.1
# Podaj minimalną i maksymalną liczbę operacji dominujących w algorytmie SortW dla
# zadanego n.
# Min: 0
# Max: n*(n-1)/2

# Zadanie 4.2
# Kwadratowa

# Zadanie 4.3
plik = open("dane4.txt", "r")
x = [int(linia) for linia in plik]
plik.close()

liczba = 0
maxi = 0

for i in range(1, len(x)):
    par = 0
    for j in range(i):
        if x[i] > x[j]:
            par += 1

    if par >= liczba:
        liczba = par
        maxi = i

print(maxi + 1)