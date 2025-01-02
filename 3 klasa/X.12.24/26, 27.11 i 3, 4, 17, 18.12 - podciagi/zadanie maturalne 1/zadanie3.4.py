print("Zadanie 3.4")

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


file = open("pi_przyklad.txt")  
ciag = list(map(int, file.read().split()))
file.close()

czy_rosnie = True
fragment = [ciag[0]]
najdluzszy = []
maxDlugosc = 0

for i in range(1, len(ciag)):
    if ciag[i] >= ciag[i - 1]:
        fragment.append(ciag[i - 1])
    else:
        czy_rosnie = False
    if not czy_rosnie:
        if ciag[i] < ciag[i - 1]:
            fragment.append(ciag[i - 1])
        else:
            if czy_rosnaco_malejacy(fragment):
                dlugosc = len(fragment)
                if dlugosc > maxDlugosc:
                    maxDlugosc = dlugosc
                    najdluzszy = fragment
            fragment = [ciag[i - 1]]
            czy_rosnie = True
            
print(najdluzszy)
