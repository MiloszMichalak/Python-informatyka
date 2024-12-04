# Zadanie 3.2
print("Zadanie 3.2")

odpowiedzi = open("wyniki3.txt", "a")

tab = [0] * 100

file = open("pi.txt", "r")
ciag = list(map(str, file.read().split()))
file.close()

for i in range(1, len(ciag)):
    doSprawdzenia = int(ciag[i - 1] + ciag[i])
    tab[doSprawdzenia] += 1
    
maks = max(tab)
indeksMaks = tab.index(maks)

mini = min(tab)
indeksMin = tab.index(mini)

odpowiedzi.write("\n" + str(mini) + " " + str(indeksMin) + "\n" + str(maks) + " " + str(indeksMaks))

odpowiedzi.close()