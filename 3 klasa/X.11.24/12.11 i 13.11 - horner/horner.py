def HornerNaiwna(A, n, x):
    y = A[0]
    potega = 1
    for i in range(1, n + 1):
        potega *= x
        y += A[i] * potega
    return y
        
# zadanie 1
print("Zadanie 1")
ciag = list(map(int, input("Podaj wspolczynniki od a0 do an: ").split()))
x = float(input("Podaj x: "))
n = len(ciag) - 1

print(HornerNaiwna(ciag, n, x))

def HornerIter(A, n, x):
    y = A[n]
    for i in range(n-1, -1, -1):
        y = x * y + A[i]
    return y

# zadanie 2
print("Zadanie 2")
wspolczynniki = list(map(int, input("Podaj wspolczynniki od a0 d0 an: ").split()))
n = len(ciag) - 1
x = float(input("Podaj x: "))
print(HornerIter(wspolczynniki, n, x))

def HornerReku(A, n, x):
    if n == 0: return A[0]
    return x * HornerReku(A[1:], n - 1, x) + A[0]
    
# zadanie 3
print("Zadanie 3")
wspolczynniki = list(map(int, input("Podaj wspolczynniki od a0 d0 an: ").split()))
n = len(ciag) - 1
x = float(input("Podaj x: "))
print(HornerReku(wspolczynniki, n, x))

# zadanie 4
print("Zadanie 4")
# smieszny pseudokod dla odwroconych po prostu

# zadanie 5
print("Zadanie 5")

