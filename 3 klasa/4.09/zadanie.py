from math import sqrt

#zadanie 1
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
def czyPierwsza(a):
    for i in range(1, sqrt(n) + 1):
        if a % i == 0:
            return false
    return true

n = int(input("Podaj liczbe: "))
for i in range(1, n + 1):
    if n % i == 0:
        if czyPierwsza(i):
            print(i)

#zadanie 6
a = int(input("Podaj liczbe a:"))
b = int(input("Podaj liczbe b:"))

if czyPierwsza(a) and czyPierwsza(b) and a - b == 2:
    print("TAK")
else: print("NIE")
