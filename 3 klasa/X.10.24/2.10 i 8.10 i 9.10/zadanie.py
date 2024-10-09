from random import randint

def SzukanieBinarne(T, a, n):
    left = 0
    right = n - 1
    while left < right:
        middle = (left + right) // 2
        if T[middle] < a:
            left = middle + 1
        else:
            right = middle
    return T[left] == a

def czyNieMalejacy(T):
    for i in range(len(T) - 1):
        if not T[i]<= T[i+1]:
            return False

# Zadanie 1
print("Zadanie 1")
numbers = list(map(int, input("Podaj 10 cyfr rozdzielone spacja: ").split()))

a = int(input("Podaj a: "))
if czyNieMalejacy(numbers):
    print("Ciag musi byc uporzadkowany malejaco")
else:
    if SzukanieBinarne(numbers, a, len(numbers)):
        print("Tak")
    else:
        print("Nie")

print("Zadanie 2")
def SzukanieBinarneReku(T, a, left, right):
    while left < right:
        middle = (left + right) // 2
        if T[middle] < a:
            return SzukanieBinarneReku(T, a, middle+1, right)
        else:
            return SzukanieBinarneReku(T, a, left, middle)
    return T[left] == a


print("Zadanie 3")
file = open("ciagi.txt", "r")
k = 1
for line in file:
    numbers = list(map(int, line.split()))
    if SzukanieBinarneReku(numbers, 10, 0, len(numbers) - 1):
        print(f"{k}: {numbers}" )
    k += 1
    
file.close()

print("Zadanie 4")
file = open("ciagi2.txt", "r")
n = int(file.readline().rstrip())
for i in range(n):
    n = int(file.readline().rstrip())
    numbers = list(map(int, file.readline().split()))
    if SzukanieBinarne(numbers, 10, n):
        print(f"{i + 1}: {numbers}" )
        
file.close()

# zadanie 5
print("Zadanie 5")
# pseudokod


# zadanie 6
print("Zadanie 6")
numbers = []
n = randint(1, 10)
numbers.append(n)
for i in range(1_000_000):
    n += randint(1, 3)
    numbers.append(n)
    
file = open("zadanie4.txt", "w")
if SzukanieBinarne(numbers, 1_500_000, len(numbers)):
    file.write("TAK")
else:
    file.write("NIE")
file.close()

# zadanie7 - maturalne
print("Zadanie 7 - maturalne")

