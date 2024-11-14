from random import randint
from token import LEFTSHIFT


def scal(tab, lewy, srodek, prawy):
    i = lewy
    j = srodek + 1
    k = lewy
    while i <= srodek and j <= prawy:
        if tab[i] < tab[j]:
            pom[k] = tab[i]
            i += 1
        else:
            pom[k] = tab[j]
            j += 1
        k += 1

    while i <= srodek:
        pom[k] = tab[i]
        i += 1
        k += 1

    while j <= prawy:
        pom[k] = tab[j]
        j += 1
        k += 1

    for i in range(lewy, prawy + 1):
        tab[i] = pom[i]


def sortuj(tab, lewy, prawy):
    if lewy < prawy:
        srodek = (lewy + prawy) // 2
        sortuj(tab, lewy, srodek)
        sortuj(tab, srodek + 1, prawy)
        scal(tab, lewy, srodek, prawy)


def scalPython(t1, t2):
    i = 0
    j = 0
    n1 = len(t1)
    n2 = len(t2)
    wynik = []
    while i < n1 and j < n2:
        if t1[i] < t2[j]:
            wynik.append(t1[i])
            i += 1
        else:
            wynik.append(t2[j])
            j += 1
    
    wynik.extend(t1[i:])
    wynik.extend(t2[j:])
    return wynik
    
def sortujPython(t):
    n = len(t)
    if n > 1:
        srodek = (n - 1) // 2
        left = sortujPython(t[:srodek + 1])
        right = sortujPython(t[srodek + 1:])
        return scalPython(left, right)
    else:
        return t

odpowiedzi_folder = "odpowiedzi/"

# zadanie 1
print("Zadanie 1")

ciag = list(map(int, input().split()))
ciag = sortujPython(ciag)
print(*ciag)

# Zadanie 2
print("Zadanie 2")
file = open("ciagi.txt", "r")
ciag = list(map(int, file.read().split()))
pom = [0] * len(ciag)
file.close()

file = open(odpowiedzi_folder + "winiki_2.txt", "w")
sortuj(ciag, 0, len(ciag) - 1)

file.write(' '.join(map(str, ciag)))
file.close()

# zadanie 3
print("Zadanie 3")

file = open(odpowiedzi_folder + "wyniki_3.txt", "w")
ciag = [randint(1, 1_000_000) for _ in range(1_000_000)]
pom = [0] * len(ciag)
sortuj(ciag, 0, len(ciag) - 1)
file.write('\n'.join(map(str, ciag)))

file.close()

# zadanie 4
print("Zadanie 4")

