# zadanie 1 - sortowanie przez scalanie, bedzie pseudokod
print("Zadanie 1")

# zadanie 2 - od najnizszego do najwyzszego, 11 -2 3 3, x = 2, wynik = 43
print("Zadanie2")
# wspolczynniki = list(map(int, input("Podaj wspolczynniki od a0 do an: ").split()))
# liczba = int(input("Podaj x: "))
# 
# n = len(wspolczynniki)
# y = wspolczynniki[n - 1]
# for i in range(n - 2, -1, -1):
#     y = y * liczba + wspolczynniki[i]
#     
# print(y)

# zadanie 3 - smiesznie latwe
print("Zadanie 3")
ciag = list(map(int, input("Podaj ciag").split()))
for i in range(1, len(ciag)):
    if ciag[i] < ciag[i - 1]:
        print("Nie")
        break
else:
    print("Tak")
        

# zadanie 4
print("Zadanie 4")
ciag = list(map(int, open("liczby.txt", "r").readline().split()))
dlugoscMax = 1
dlugosc = 1
for i in range(1, len(ciag)):
    if ciag[i] >= ciag[i - 1]:
        dlugosc += 1
        if dlugosc > dlugoscMax:
            dlugoscMax = dlugosc
    else:
        dlugosc = 1
        
# lub tak
# if dlugosc > dlugoscMax:
#     dlugoscMax = dlugosc

print(dlugoscMax)
        
