# Zadanie 4.1
# Podaj minimalną i maksymalną liczbę operacji dominujących w algorytmie SortW dla
# zadanego n.
# Min: 0
# Max: n*(n-1)/2

# Zadanie 4.2
# Kwadratowa

# Zadanie 4.3
# W pliku dane4.txt zapisano ciąg x złożony z 2023 różnych liczb całkowitych x1, x2, …,
# x2023 z przedziału [1, 2023], po jednej liczbie w wierszu – w wierszu i-tym liczbę xi.
# Podaj takie i, dla którego liczba par (xi, xj) takich, że xi > xj oraz i > j jest największa.

with open("dane4.txt", "r") as file:
    x = [int(line) for line in file]

n = len(x)
max_pairs = -1
best_i = -1

for i in range(n):
    count = 0
    for j in range(i):
        if x[i] > x[j]:
            count += 1
    if count > max_pairs:
        max_pairs = count
        best_i = i + 1

print(best_i)