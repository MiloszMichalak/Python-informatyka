def NWD(a, b):
    if b == 0: return a

    while a != b:
        if a > b:
            a -= b
        else:
            b -= a

    return a


file = open("dane/dron_przyklad.txt", "r")

poziom = []
pion = []

for linia in file:
    liniaSplit = linia.split(" ")
    poziom.append(int(liniaSplit[0]))
    pion.append(int(liniaSplit[1]))

# 3 . 1
liczbaPar = 0
for i in range(len(poziom)):
    najwiekszyDzielnik = NWD(poziom[i], abs(pion[i]))
    if najwiekszyDzielnik > 1:
        liczbaPar += 1

print(liczbaPar)

# 3. 2 a
dystans = 0
wysokosc = 0
ilosc = 0
for i in range(len(poziom)):
    dystans += poziom[i]
    wysokosc += pion[i]
    if 0 < dystans < 5000 and 0 < wysokosc < 5000:
        ilosc += 1

    # Nadpisywanie wartosci do czesci B
    poziom[i] = dystans
    pion[i] = wysokosc

print(ilosc)

# 3 . 2 b
# (a1 + a2)/2 = srodek x   ==   a1 + a2 = 2 srodki x
def czy_srodek(i, j, k):
    if (poziom[i] + poziom[k] == 2 * poziom[j]
            and pion[i] + pion[k] == 2 * pion[j]):
        print((poziom[i], pion[i]), (poziom[j], pion[j]), (poziom[k], pion[k]))

dystans = 0
wysokosc = 0
for i in range(len(poziom)):
    for j in range(i + 1, len(poziom)):
        for k in range(j + 1, len(poziom)):
            czy_srodek(i, j, k)
            czy_srodek(j, i, k)
            czy_srodek(i, k, j)
