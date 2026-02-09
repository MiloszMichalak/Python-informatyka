# Napisz program, który znajdzie najdłuższy wspólny spójny podciąg oraz jego długość dla dwóch napisów podanych przez użytkownika.
# Możesz wykorzystać algorytm naiwny generujący wszystkie spójne podciągi lub algorytm dynamiczny.

def najdluzszyWspolnyPodciag(X, Y):
    n, m = len(X), len(Y)
    D = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if X[i - 1] == Y[j - 1]:
                D[i][j] = D[i - 1][j - 1] + 1
            else:
                D[i][j] = 0
                # D[i][j] = max(D[i - 1][j], D[i][j - 1])

    i, j = n, m
    N = []
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            N.append(X[i - 1])
            i -= 1
            j -= 1
        elif D[i - 1][j] > D[i][j - 1]:
            i -= 1
        else:
            j -= 1

    N.reverse()
    return N, D[n][m]

ciag1 = "ALGORYTMIKA"
ciag2 = "INFORMATYKA"
print(najdluzszyWspolnyPodciag(ciag1, ciag2))
