# 2.1
file = open('dane/symbole_przyklad.txt', 'r')
linie = file.read().splitlines()

for linia in linie:
    if linia[::-1] == linia:
        print(linia)


# 2.2
for i in range(2, len(linie)):
    for j in range(2, 12):
        if (linie[i][j] == linie[i][j - 1] == linie[i][j - 2] ==
                linie[i - 1][j] == linie[i - 1][j - 1] == linie[i - 1][j - 2] ==
                linie[i - 2][j] == linie[i - 2][j - 1] == linie[i - 2][j - 2]):
            print(i, j)

# 2.3
maxCiag = ""
maxDziesietna = 0

for linia in linie:
    # Zamiana ciągu na kod 0 1 2
    trojkowyCiag = ""
    for znak in linia:
        if znak == "o":
            trojkowyCiag += "0"
        elif znak == "+":
            trojkowyCiag += "1"
        elif znak == "*":
            trojkowyCiag += "2"

    # Zamiana z systemu trojkowego na dziesietny
    potega = len(trojkowyCiag) - 1
    trojkowaCyfra = 0
    for znakTrojkowy in trojkowyCiag:
        trojkowaCyfra += int(znakTrojkowy) * (3 ** potega)
        potega -= 1

    # Porownywanie maxa
    if trojkowaCyfra > maxDziesietna:
        maxDziesietna = trojkowaCyfra
        maxCiag = linia

    trojkowyCiag = ""

print(maxDziesietna, maxCiag)


# 2.4
suma = 0

for linia in linie:
    trojkowyCiag = ""
    for znak in linia:
        if znak == "o":
            trojkowyCiag += "0"
        elif znak == "+":
            trojkowyCiag += "1"
        elif znak == "*":
            trojkowyCiag += "2"

    # Zamiana z systemu trojkowego na dziesietny
    potega = len(trojkowyCiag) - 1
    trojkowaCyfra = 0
    for znakTrojkowy in trojkowyCiag:
        trojkowaCyfra += int(znakTrojkowy) * (3 ** potega)
        potega -= 1

    suma += trojkowaCyfra


trojkowaSuma = ""
trojkowyCiagSumy = ""
sumaDuplikat = suma
while suma > 0:
    calosciDzielenia = suma // 3
    resztaDzielenia = suma % 3
    suma //= 3

    trojkowaSuma = str(resztaDzielenia) + trojkowaSuma

for znak in trojkowaSuma:
    if znak == "0":
        trojkowyCiagSumy += "o"
    elif znak == "1":
        trojkowyCiagSumy += "+"
    elif znak == "2":
        trojkowyCiagSumy += "*"


print(sumaDuplikat, trojkowyCiagSumy)
