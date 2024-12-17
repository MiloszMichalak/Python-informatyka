print("Zadanie 3.3")

def czy_rosnaco_malejacy(ciag):
    n = len(ciag) // 2
    n2 = len(ciag)
    
    i = 0
    for k in range(1, n):
        if ciag[k] >= ciag[k - 1]:
            i += 1
        
    for j in range(n, n2):
        if ciag[j] <= ciag[j - 1]:
            i += 1
            
    return i == n2 - 1
    
file = open("pi.txt", "r")
ciag = list(map(int, file.read().split()))
file.close()


for i in range(len(ciag) - 5):
    if czy_rosnaco_malejacy(ciag[i:i + 6]):
        print(ciag[i:i + 6])
