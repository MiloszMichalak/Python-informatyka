def maksik(tablica):
    maks = tablica[0]
    for i in tablica:
        if i > maks:
            maks = i
    return maks


def minik(tablica):
    minik = tablica[0]
    for i in tablica:
        if i < minik:
            minik = i
    return minik


def dec2Bin(dec):
    out = ""
    while dec > 0:
        out = str(dec % 2) + out
        dec = dec // 2
    return out

def lenik(tab):
    ile = 0
    for i in tab:
        ile += 1
    return ile

def bin2Dec(bin):
    dec = 0
    potega = 0
    for i in range(lenik(bin) - 1, -1, -1):
        if bin[i] == '1':
            dec += 2 ** potega
        potega += 1
    return dec

zegar = []
temperatury = []
zegarDec = []
temperaturyDec = []

with open("dane_systemy1.txt") as f:
    for line in f:
        T = line.split(" ")
        zegar.append(T[0])
        temperatury.append(int(T[1]))

for i in zegar:
    zegarDec.append(bin2Dec(i))

for i in temperatury:
    temperaturyDec.append(bin2Dec(str(i)))

# zadanie 1
print("Zadanie 1")
print(maksik(temperatury))
print(minik(temperatury))


# zadanie 2
print("Zadanie 2")
godzina = 12
ile = 0
for i in zegarDec:
    if i != godzina:
        ile += 1
    godzina += 24
print(ile)

# zadanie 3
daty = []
pobicia = []
pobiciaCzas = []
skok = 0
tempMaks = 1
print("Zadanie 3")
for i in range(lenik(temperatury)):
    if temperatury[i] > tempMaks:
        daty.append(zegar[i])
        tempMaks = temperatury[i]
        temp = skok
        skok = bin2Dec(str(tempMaks)) - skok
        if skok >= temp:
            pobicia.append(skok)
            pobiciaCzas.append(zegar[i])

print("Pobic bylo", lenik(daty), end=" ")
print()
for i in range (lenik(pobicia)):
    maks = maksik(pobicia)
    if pobicia[i] == maks:
        print("Najwiekszy skok:", maks, ", O godzinie:", pobiciaCzas[i], end=" ")
        
# zadanie 4
print("Zadanie 4")
# no nie wyszlo