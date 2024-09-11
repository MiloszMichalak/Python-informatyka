from math import sqrt


# zadanie 1
def czyPodzielnaPrzez2(a):
    return a % 2 == 0

n = int(input("Podaj liczbe: "))
if czyPodzielnaPrzez2(n):
    print("TAK")
else: print("NIE")

#zadanie 2
n = int(input("Podaj liczbe: "))
for i in range(1, n + 1):
    if n % i == 0:
        print(i)

#zadanie 2v2
n = int(input("Podaj n: "))
i = 1
while i*i<n:
    if n % i == 0:
        print(i)
        print(i // 2)
    i += 1
if i * i == n:
    print(i)

#zadanie 3
suma = 0
n = int(input("Podaj liczbe: "))
for i in range(1, n + 1):
    if n % i == 0:
        suma += i
print(suma)

#zadanie 4
ile = 0
n = int(input("Podaj liczbe: "))
for i in range(1, n + 1):
    if n % i == 0:
        ile += 1
print(ile)

#zadanie 5
def czyPierwsza(n):
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

n = int(input("Podaj liczbe: "))
for i in range(1, n + 1):
    if n % i == 0 and czyPierwsza(i):
        print(i)

#zadanie 6
a = int(input("Podaj liczbe a: "))
b = int(input("Podaj liczbe b: "))

if czyPierwsza(a) == True and czyPierwsza(b) == True and abs(a - b) == 2 or abs(b - a) == 2:
    print("TAK")
else: print("NIE")

def sumaDzielnikowWlasciwych(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma

# Zadanie 7
n = int(input("Podaj liczbe: "))
suma = sumaDzielnikowWlasciwych(n)

if suma == n:
    print("TAK")
else: 
    print("NIE")

# Zadanie 8
a = int(input("Podaj liczbe a: "))
b = int(input("Podaj liczbe b: "))

if a != b and sumaDzielnikowWlasciwych(a) == b and sumaDzielnikowWlasciwych(b) == a:
    print("TAK")
else:
    print("NIE")
    
# Wszystkie liczby blizniacze w zakresie od 1 do 1000
for i in range(1, 100):
    for j in range(1, 100):
        if czyPierwsza(i) == True and czyPierwsza(j) == True and abs(i - j) == 2:
            print(i,j)
