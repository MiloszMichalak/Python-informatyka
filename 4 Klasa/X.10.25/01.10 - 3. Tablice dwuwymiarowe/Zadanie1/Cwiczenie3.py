# Dana jest tablica o wymiarach . Napisz program, który wypisze zawartość jedynie tych wierszy tablicy, 
# w których wszystkie elementy są większe od liczby 2.

# Działanie swojego programu przetestuj dla tablicy wypełnionej wartościami w następujący sposób: 
# każda komórka tablicy przyjmuje wartość sumy obu jej indeksów, czyli  tablica[i][j] = i + j. Rozwiązanie sprawdź dla n = 5.

n = 5
tablica = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        tablica[i][j] = i + j

for row in tablica:
    flaga = True
    for value in row:
        if value <= 2:
            flaga = False
            break
    if flaga:
        print(row)
