# Zadanie 1
from random import randint

print("Zadanie 1")

liczby = [randint(1, 1000) for i in range(100)]

mini = maks = liczby[0]
porownania = 0

for liczba in liczby:
    porownania += 1
    if liczba < mini:
        mini = liczba
    porownania += 1
    if liczba > maks:
        maks = liczba
        
print(f"Min: {mini}, Max: {maks}, Porownania: {porownania}")

# Zadanie 2
print("Zadanie 2")
# 1+((n-2)/2)*3 = 1+(3/2)*(n-2) = 1+(3/2)n-3 = (3/2)n-2

# Zadanie 3
print("\nZadanie 3")

def optimizedFinding(liczby):
    porownania = 0
    porownania += 1
    if liczby[0] < liczby[1]:
        mini = liczby[0]
        maks = liczby[1]
    else:
        mini = liczby[1]
        maks = liczby[0]
        
    for i in range(2, len(liczby) - 2, 2):
        porownania += 1
        if liczby[i] < liczby[i + 1]:
            porownania += 1
            if liczby[i] < mini:
                mini = liczby[i]
            porownania += 1
            if liczby[i + 1] > maks:
                maks = liczby[i + 1]
        else:
            porownania += 1
            if liczby[i + 1] < mini:
                mini = liczby[i + 1]
            porownania += 1
            if liczby[i] > maks:
                maks = liczby[i]

    print(f"Min: {mini}, Max: {maks}, Porownania: {porownania}")

optimizedFinding(liczby)

# Zadanie 4
print("Zadanie 4")

def oddFinding(ciag):
    porownania = 0
    mini = maks = ciag[0]

    for i in range(1, len(liczby) - 2, 2):
        porownania += 1
        if liczby[i] < liczby[i + 1]:
            porownania += 1
            if liczby[i] < mini:
                mini = liczby[i]
            porownania += 1
            if liczby[i + 1] > maks:
                maks = liczby[i + 1]
        else:
            porownania += 1
            if liczby[i + 1] < mini:
                mini = liczby[i + 1]
            porownania += 1
            if liczby[i] > maks:
                maks = liczby[i]

    print(f"Min: {mini}, Max: {maks}, Porownania: {porownania}")
    
oddFinding(liczby)
    



