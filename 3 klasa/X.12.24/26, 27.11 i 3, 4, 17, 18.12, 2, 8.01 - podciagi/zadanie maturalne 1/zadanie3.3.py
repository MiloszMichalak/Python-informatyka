print("Zadanie 3.3")

def czy_rosnaco_malejacy(ciag):
    polDlugosci = len(ciag) // 2
    dlugosc = len(ciag)
    
    if dlugosc < 4:
        return
    
    i = 1
    for k in range(1, polDlugosci):
        if ciag[k] >= ciag[k - 1]:
            i += 1
        
    for j in range(polDlugosci, dlugosc):
        if ciag[j] <= ciag[j - 1]:
            i += 1
            
    return i == dlugosc
    
file = open("pi.txt", "r")
ciag = list(map(int, file.read().split()))
file.close()


for i in range(len(ciag) - 5):
    if czy_rosnaco_malejacy(ciag[i:i + 6]):
        print(ciag[i:i + 6])
