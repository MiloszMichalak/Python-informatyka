file = open("dane.txt", "r")
nominaly = list(map(int, file.readline().split()))
kwoty = [int(file.readline()) for i in range(10)]
file.close()

iloscNominalow = []

for kwota in kwoty:
    ilosc = 0
    for nominal in nominaly:
        ile = kwota // nominal
        kwota -= ile * nominal
        # lub kwota = kwota % nominal
        if ile > 0:
            ilosc += ile
    iloscNominalow.append(ilosc)

print(iloscNominalow)

mini = min(iloscNominalow)
for i in range(len(iloscNominalow)):
    if iloscNominalow[i] == mini:
        print(kwoty[i])
        
