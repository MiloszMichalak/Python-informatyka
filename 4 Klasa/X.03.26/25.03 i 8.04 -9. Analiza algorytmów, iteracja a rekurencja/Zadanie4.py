# Zadanie 4.1
# Podaj minimalną i maksymalną liczbę operacji dominujących w algorytmie SortW dla
# zadanego n.
# Min: 0
# Max: n*(n-1)/2

# Zadanie 4.2
# Kwadratowa

# Zadanie 4.3
with open('dane4.txt', 'r', encoding='utf-8') as f:
    x = [int(line.strip()) for line in f if line.strip()]
    
max_par = -1
szukane_i = -1


for i in range(len(x)):
    liczba_par = 0

    for j in range(i):
        if x[i] > x[j]:
            liczba_par += 1

    if liczba_par > max_par:
        max_par = liczba_par
        szukane_i = i + 1

print(f"Szukane i (numer wiersza z pliku): {szukane_i}")
