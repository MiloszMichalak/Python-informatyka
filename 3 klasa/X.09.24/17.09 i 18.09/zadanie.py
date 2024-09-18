from math import sqrt

def czyPierwsza(a):
    for i in range(2, int(sqrt(a) + 1)):
        if a % i == 0:
            return False
    return True

def sumaCzynnikow(n):
    suma = 0
    czynnik = 2
    while n > 1:
        while n % czynnik == 0:
            suma += czynnik
            n //= czynnik
        czynnik += 1
    return suma

# Zadanie 1
file = open("liczby1.txt", "r")
temp = 0
for line in file:
    if czyPierwsza(int(line)):
        temp += 1
    
print(temp)

file.close()

# Zadanie 2
file = open("liczby2.txt", "r")
numbers = file.readline().split()
for number in numbers:
    print(number)
    
# Zadanie 3
suma = 0
for number in numbers:
    for i in range(1, int(number)):
        if int(number) % i == 0:
            suma += 1
print(suma)

# zadanie 4
maks = 0
suma = 0
liczba = 0
for number in numbers:
    suma = 0
    for i in range(1, int(number)):
        if int(number) % i == 0 and czyPierwsza(i):
            suma += i
    if suma > maks:
        maks = suma
        liczba = number
print(liczba)

# zadanie 5
mini = 100
liczba = 0
liczby = []
for number in numbers:
    if sumaCzynnikow(int(number)) <= mini:
        mini = sumaCzynnikow(int(number))
        liczby.append(number)
print(liczby)

# zadanie 6
liczby = []
for number in numbers:
    czynnik = 2
    czynniki = []
    liczba = int(number)
    while liczba > 1:
        while liczba % czynnik == 0:
            liczba //= czynnik
            if czynnik not in czynniki:
                czynniki.append(czynnik)
        czynnik += 1
    if len(czynniki) >= 2:
        liczby.append(number)
for liczba in liczby:
    print(liczba)

# zadanie 7
mini = 100
liczba = 0
for number in numbers:
    suma = sumaCzynnikow(int(number))
    sumaLiczb = 0
    while suma > 1:
        sumaLiczb += suma % 10
        suma //= 10
    if sumaLiczb < mini:
        mini = sumaLiczb
        liczba = number
print(liczba)   
        
    
        
    