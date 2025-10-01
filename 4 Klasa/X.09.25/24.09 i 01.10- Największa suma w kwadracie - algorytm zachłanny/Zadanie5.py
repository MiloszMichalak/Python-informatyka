# Napisz program, który zapyta użytkownika o podanie liczby całkowitej n, a następnie wygeneruje macierz o n wierszach i n kolumnach 
# z liczbami losowymi z zakresu 1-10, a następnie wyświetli tą macierz oraz największą sumę wyznaczoną algorytmem zachłannym opisanym powyżej.
from random import randint

n = int(input("Podaj liczbe calkowita n: "))

maciorka = [[randint(1, 10) for _ in range(n)] for _ in range(n)]
for row in maciorka:
    for value in row:
        print(value, end="\t")
    print()
    
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
    
print(f"Suma: {suma}")


