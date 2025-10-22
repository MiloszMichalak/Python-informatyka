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
    
    
file = open("nominaly.txt", "r")
nominaly = list(map(int, file.readline().split()))
print(nominaly)
file.close()

k = int(input("Podaj kwote do wydania: "))
print(minimalnaLiczbaNominalow(nominaly, k, len(nominaly)))

    