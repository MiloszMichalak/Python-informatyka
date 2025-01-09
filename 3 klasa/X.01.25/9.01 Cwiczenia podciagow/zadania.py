# Zadanie 1
print("Zadanie 1")
file = open("ciag.txt", "r")
ciag = list(map(int, file.readline().split()))
file.close()

maks = 0

for i in range(len(ciag) - 2):
    suma = sum(ciag[i:i+3])
    if suma > maks:
        maks = suma

print(maks)
    
# Zadanie 2
print("\nZadanie 2")
file = open("ciag.txt", "r")
ciag = list(map(int, file.readline().split()))
file.close()

maksPodciag = []
maks = 0

for i in range(len(ciag) - 2):
    podciag = ciag[i:i+3]
    suma = sum(podciag)
    if suma > maks:
        maks = suma
        maksPodciag = podciag
        
print(maks)
print(maksPodciag)

# Zadanie 3
print("\nZadanie 3")
maks = 0
maksPodciag = []

for i in range(2, len(ciag)):
    for j in range(len(ciag)):
        podciag = ciag[i:j]
        suma = sum(podciag)
        if suma > maks:
            maks = suma
            maksPodciag = podciag

print(maks)
print(maksPodciag)


# Zadanie 4
print("\nZadanie 4")

