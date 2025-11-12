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


slowo1 = input()
slowo2 = input()
print(najdluzszyWspolnyPodciag(slowo1, slowo2))