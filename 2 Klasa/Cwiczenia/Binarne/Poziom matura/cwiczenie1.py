print("Zadanie 1")

bin1, bin2 = input("Bin1: "), input("Bin2: ")

# gotowe
w = ""
j = 0
for i in range(len(bin1) - 1, 0, -1):
    s = j + int(bin1[i]) + int(bin2[i])
    j = s // 2
    w = str(s % 2) + w
    if j > 0:
        w = str(j) + w
print(w)
