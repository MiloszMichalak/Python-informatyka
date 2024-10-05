from operator import index, imatmul


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
def SzukanieBinarneReku(T, a, n):
    left = 0
    right = n - 1
    while left < right:
        middle = (left + right) // 2
        if T[middle] < a:
            left = middle + 1
        else:
            right = middle
    return T[left] == a


print("Zadanie 3")
file = open("ciagi.txt")
k = 1
for line in file:
    numbers = list(map(int, line.split()))
    if SzukanieBinarneReku(numbers, 10, len(numbers)):
        print(f"{k}: {numbers}" )
    k += 1
    
file.close()

print("Zadanie 4")
with open("ciagi.txt") as f:
    a = 10
    n = int(file.readline())
    index = 1
    numbers = list(map(int, file.readline().split()))
    if SzukanieBinarne(numbers, a, n):
        print(f"{index}: {numbers}" )
        index += 1
    

# zadanie 5
print("Zadanie 5")
