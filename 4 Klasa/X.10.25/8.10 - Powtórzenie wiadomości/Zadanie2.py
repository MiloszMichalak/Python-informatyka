file = open('macierz.txt', 'r')
maciorka = []
for line in file:
    maciorka.append(list(map(int, line.split())))

n = len(maciorka)
droga = ""
    
i = 0
j = 0
suma = maciorka[0][0]
while i < n - 1 or j < n - 1:
    if i == n - 1:
        j += 1
        suma += maciorka[i][j]
        droga += "P"
    elif j == n - 1:
        i += 1
        suma += maciorka[i][j]
        droga += "D"
    elif maciorka[i][j + 1] > maciorka[i + 1][j]:
        j += 1
        suma += maciorka[i][j]
        droga += "P"
    else:
        i += 1
        suma += maciorka[i][j]
        droga += "D"
        
    
for lista in maciorka:
    print(*lista, sep="\t")
    
print(suma)
print(droga)