# 2.1
file = open('dane/symbole_przyklad.txt', 'r')
linie = file.read().splitlines()

for linia in linie:
    if linia[::-1] == linia:
        print(linia)


for i in range(2, len(linie)):
    for j in range(2, 12):
        if (linie[i][j] == linie[i][j - 1] and linie[i][j - 1] == linie[i][j - 2] and
                linie[i - 1][j] == linie[i - 1][j - 1] and linie[i - 1][j - 1] == linie[i - 1][j - 2] and
                linie[i - 2][j] == linie[i - 2][j - 1] and linie[i - 2][j - 1] == linie[i - 2][j - 2]):
            print(i, j)

