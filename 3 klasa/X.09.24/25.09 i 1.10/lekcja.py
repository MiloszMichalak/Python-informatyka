# zadanie 1

n = int(input("Podaj n: "))
def sito(n):
    czy_pierwsza = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if czy_pierwsza[p]:
            for i in range(p * p, n + 1, p):
                czy_pierwsza[i] = False
        p += 1
    return czy_pierwsza
        
czy_pierwsza = sito(n)
    
for i in range(2, len(czy_pierwsza)):
    if czy_pierwsza[i]:
        print(i)

# zadanie 2
print("Zadanie 2")
ile = 0
suma = 0
for i in range(2, len(czy_pierwsza)):
    if czy_pierwsza[i] and i <= n:
        suma += i
        ile += 1
        
print(ile)
print(suma)

# zadanie 3
print("Zadanie 3")
def sitoZPetlaDopoki():
    czy_pierwsza = [True] * (n + 1)
    p = 2
    temp = p * p
    while p * p <= n:
        if czy_pierwsza[p]:
            while temp <= n:
                czy_pierwsza[i] = False
            temp += n + 1
        p += 1

# czy_pierwsza[0] ← fałsz
# czy_pierwsza[1] ← fałsz
# dla i=2,3,...,n wykonuj
#   czy_pierwsza[i] ← prawda

# p ← 2
# temp <- p * p
# dopóki p * p ⩽ n wykonuj
#   jeżeli czy_pierwsza[p] = prawda
#       dopoki temp <= n 
#           czy_pierwsza[i] ← fałsz
#       temp = temp + n + 1
#    p ← p + 1

        
# zadanie 4
# czesc 1
print("Zadane 4 czesc 1")
n = 1000
czy_pierwsza = sito(n)

for i in range(2, len(czy_pierwsza)):
    if czy_pierwsza[i]:
        print(i)
        
# czesc 2

print("Zadanie 4 czesc 2")
ile = 0
file = open("liczby.txt", "r")
for line in file:
    if czy_pierwsza[int(line)]:
        ile += 1
print(ile)
file.close()

# zadanie 5
print("Zadanie 5")
a = int(input("Podaj liczbe a: "))
b = int(input("Podaj liczbe b: "))

ile = 0
suma = 0
czy_pierwsza = sito(b)

for i in range(a, b + 1):
    if czy_pierwsza[i]:
        print(i)
        suma += i
        ile += 1
        
print(f"Ile: {ile}")
print(f"Suma: {suma}")

# zadanie 6
print("Zadanie 6")
file = open("ciag.txt", "r")
numbers = []
ilePierwszych = 0
numbers = list(map(int, file.readline().split()))
ileLiczb = len(numbers)

czy_pierwsza = sito(1000)

for number in numbers:
    if czy_pierwsza[number]:
        ilePierwszych += 1
        
print(f"Ile: {ileLiczb}")
print(f"Pierwszych: {ilePierwszych}")
print(f"Procent pierwszych = {round((ilePierwszych/ileLiczb) * 100, 2)}%")


    


