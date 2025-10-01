# Napisz program wypisujący kwadrat sumy wartości znajdujących się na obu przekątnych tablicy o wymiarach  (wartości wspólne mogą się powtarzać).
 
# Działanie swojego programu przetestuj dla tablicy wypełnionej wartościami w następujący sposób: 
# każda komórka tablicy przyjmuje wartość sumy obu jej indeksów, czyli  tablica[i][j] = i + j. Rozwiązanie sprawdź dla n = 5.

n = 5
tablica = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        tablica[i][j] = i + j
        
suma = 0
for i in range(n):
    suma += tablica[i][i]
    suma += tablica[i][n - i - 1]
    
print(suma ** 2)