def minimalnaLiczbaNominalow(nominaly, k, n):
    maksi = k + 1
    liczbaNominalow = [maksi] * maksi
    liczbaNominalow[0] = 0
    for i in range(1, k + 1):
        for j in range(n):
            nominal = nominaly[j]
            if i >= nominal:
                if liczbaNominalow[i - nominal] + 1 < liczbaNominalow[i]:
                    liczbaNominalow[i] = liczbaNominalow[i - nominal] + 1
    
    return liczbaNominalow[k] if liczbaNominalow[k] != maksi else -1


def minimalnaLiczbaNominalowKrotsza(nominaly, kwota):
    maksi = kwota + 1
    liczbaNominalow = [maksi] * maksi
    liczbaNominalow[0] = 0
    for i in range(1, maksi):
        for nominal in nominaly:
            if i >= nominal:
                liczbaNominalow[i] = min(liczbaNominalow[i], liczbaNominalow[i - nominal] + 1)
            
    return liczbaNominalow[kwota] if liczbaNominalow[kwota] != maksi else -1

def minimalnaLiczbaNominalowKombinacja(nominaly, kwota):
    maksi = kwota + 1
    liczbaNominalow = [maksi] * maksi
    liczbaNominalow[0] = 0

    kombinacja = [0] * maksi
    kombinacja[0] = {}

    for i in range(1, maksi):
        for nominal in nominaly:
            if i >= nominal and liczbaNominalow[i] > liczbaNominalow[i - nominal] + 1:
                liczbaNominalow[i] = liczbaNominalow[i - nominal] + 1
                kombinacja[i] = kombinacja[i - nominal].copy()
                kombinacja[i][nominal] = kombinacja[i].get(nominal, 0) + 1
                
    print(kombinacja)

    return kombinacja[kwota] if liczbaNominalow[kwota] != maksi else -1

    
    
file = open("nominaly.txt", "r")
nominaly = list(map(int, file.readline().split()))
print(nominaly)
file.close()

k = int(input("Podaj kwote do wydania: "))
print(minimalnaLiczbaNominalow(nominaly, k, len(nominaly)))
print(minimalnaLiczbaNominalowKrotsza(nominaly, k))
print(minimalnaLiczbaNominalowKombinacja(nominaly, k))

    