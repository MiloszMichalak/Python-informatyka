def najdluzszyWspolnyPodciag(X, Y):
    n, m = len(X), len(Y)
    D = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if X[i - 1] == Y[j - 1]:
                D[i][j] = D[i - 1][j - 1] + 1
            else:
                D[i][j] = max(D[i - 1][j], D[i][j - 1])

    return D[n][m]


dlugosci = []
file = open('pary.txt', 'r')

slowa = []
for line in file:
    slowa.append(line.split())

for i in slowa:
    dlugosci.append(najdluzszyWspolnyPodciag(i[0], i[1]))

maksik = max(dlugosci)
for i in range(len(dlugosci)):
    if dlugosci[i] == maksik:
        print(slowa[i])
    
