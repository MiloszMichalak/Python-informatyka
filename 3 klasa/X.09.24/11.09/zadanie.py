# wczytaj(n)
# czynnik ← 2
# dopóki n>1 wykonuj
# dopóki n mod czynnik = 0 wykonuj
# wypisz(czynnik)
# n ← n / czynnik
# czynnik ← czynnik + 1
import math



# Zadanie 1
def rozkladNaCzynnikiPierwsze(n):
    czynnik = 2
    while n > 1:
        while n % czynnik == 0:
            print(n, czynnik)
            n //= czynnik
        czynnik += 1

n = int(input("Podaj liczbe: "))
print(rozkladNaCzynnikiPierwsze(100))

# Zadanie 2
def rozkladNaCzynnikiPierwszeSuma(n):
    suma = 0
    czynnik = 2
    while n > 1:
        while n % czynnik == 0:
            suma += czynnik
            n //= czynnik
        czynnik += 1
        
        
n = int(input("Podaj liczbe: "))
suma = rozkladNaCzynnikiPierwszeSuma(n)
print(suma)


# Zadanie 3
from math import sqrt
def czyPierwsza(a):
    for i in range(2, int(math.sqrt(a) + 1)):
        if a % i == 0:
            return False
    return True

n = int(input("Podaj liczbe: "))
suma = rozkladNaCzynnikiPierwszeSuma(n)

if czyPierwsza(suma):
    print("Tak")
else: 
    print("Nie")
    
# Zadanie 4
n = int(input("Podaj liczbe: "))
listaCzynnikow = []
czynnik = 2
while n > 1:
    while n % czynnik == 0:
        if czynnik not in listaCzynnikow:
            listaCzynnikow.append(czynnik)
        n //= czynnik
    czynnik += 1
    
print(len(listaCzynnikow))

# Zadanie 5
sumaCyfr = 0
n = int(input("Podaj liczbe: "))
suma = rozkladNaCzynnikiPierwszeSuma(n)
while n > 0:
    sumaCyfr += n % 10
    n //= 10
if suma == sumaCyfr:
    print(n)


