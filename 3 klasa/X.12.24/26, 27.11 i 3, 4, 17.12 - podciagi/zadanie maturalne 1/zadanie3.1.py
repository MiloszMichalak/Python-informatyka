# Zadanie 1
print("Zadanie 1")

file = open("wyniki3.txt", "w")

pi_przyklad = open("pi.txt", "r")
ciag = list(map(str, pi_przyklad.read().split()))
print(ciag)

ile = 0
for i in range(1, len(ciag)):
    doSprawdzenia = int(ciag[i - 1] + ciag[i])
    if doSprawdzenia > 90:
        ile += 1

file.write(str(ile))
file.close()




        