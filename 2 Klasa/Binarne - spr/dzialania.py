print("Fix me!")

# 11011 * 101
# sposob 1 - pierwsza liczba 5 druga 3
# a = input()
# b = input()
a = "11011"
b = "101"

# dodawanie do M po kolei wynikow mnozen
def multiplyBin(a, b):
    M = []
    for i in range(len(b)):
        if b[-i - 1] == "0":
            M.append("0" * (len(a) + i))
        else:
            M.append("0" * i + a)
    return M

print(multiplyBin(a, b))

def addBinFromMultiply(M):
    out = ""
    # generowanie tablicy do wynikow koncowej dlugosci
    M2 = (["0"] * len(M[-1])) * len(M)
    print(M2)
    for i in range(len(M)):
        for j in range(len(M[-1])):
            temp = int(M2[-i][j])
            temp += int(M[i][j])
            M2[-i][j] = str(temp)

    return M2

print(addBinFromMultiply(multiplyBin(a, b)))
