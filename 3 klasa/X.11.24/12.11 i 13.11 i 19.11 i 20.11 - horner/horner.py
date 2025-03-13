# def HornerNaiwna(A, n, x):
#     y = A[0]
#     potega = 1
#     for i in range(1, n + 1):
#         potega *= x
#         y += A[i] * potega
#     return y
#         
# # zadanie 1
# print("Zadanie 1")
# ciag = list(map(int, input("Podaj wspolczynniki od a0 do an: ").split()))
# x = float(input("Podaj x: "))
# n = len(ciag) - 1
# 
# print(HornerNaiwna(ciag, n, x))
# 
# def HornerIter(A, n, x):
#     y = A[n]
#     for i in range(n-2, -1, -1):
#         y = y * x + A[i]
#     return y
# 
# # zadanie 2
# print("Zadanie 2")
# wspolczynniki = list(map(int, input("Podaj wspolczynniki od a0 d0 an: ").split()))
# n = len(ciag) - 1
# x = float(input("Podaj x: "))
# print(HornerIter(wspolczynniki, n, x))
# 
# def HornerReku(A, n, x):
#     if n == 0: return A[0]
#     return x * HornerReku(A[1:], n - 1, x) + A[0]
#     
# # zadanie 3
# print("Zadanie 3")
# wspolczynniki = list(map(int, input("Podaj wspolczynniki od a0 d0 an: ").split()))
# n = len(ciag) - 1
# x = float(input("Podaj x: "))
# print(HornerReku(wspolczynniki, n, x))
# 
# # zadanie 4
# print("Zadanie 4")
# # Odwrotna wersja naiwna liczaca od konca
# # y ← A[n]
# # potęga ← 1
# # dla i ← n - 1, n - 2, ..., 0 wykonuj
# #   potega ← potega * x
# #   y ← y + A[i] * potega
# 
# # Odwrotny horner - liczy od poczatku
# # y ← A[0]
# # dla i ← 1, 2, ..., n wykonuj
# #   y ← x * y + A[i]
# 
# def HornerNaiwnaOdwrocona(A, n, x):
#     y = A[n]
#     potega = 1
#     for i in range(n - 1, -1, -1):
#         potega *= x
#         y = y + A[i] * potega
#     return y
# 
# # zadanie 5
# print("Zadanie 5")
# print("Zadanie 1 odwrocona kolejnosc")
# 
# ciag = list(map(int, input("Podaj wspolczynniki od an do a0: ").split()))
# x = float(input("Podaj x: "))
# n = len(ciag) - 1
# 
# print(HornerNaiwnaOdwrocona(ciag, n, x))
# 
# def HornerIterOdwrocona(A, n, x):
#     y = A[0]
#     for i in range(1, n + 1):
#         y = x * y + A[i]
#     return y
# 
# print("Zadanie 2 odwrocona kolejnosc")
# wspolczynniki = list(map(int, input("Podaj wspolczynniki od an d0 a0: ").split()))
# n = len(ciag) - 1
# x = float(input("Podaj x: "))
# print(HornerIterOdwrocona(wspolczynniki, n, x))

def HornerPython(A, x):
    y = 0
    for a in A:
        y *= x + a
    return y

#  KONWERSJA NA INNE SYSTEMY LICZBOWE
# Zadanie 6
def BinToDec(number: str) -> int:
    y = int(number[0])
    for i in range(1, len(number)):
        y = y * 2 + int(number[i])
    return y
    
    
print("Zadanie 6")
print(BinToDec("1001")) # 9
print(BinToDec("1010")) # 10
print(BinToDec("1100")) # 12

# Zadanie 7
def BinToP(number: str, p: int) -> int:
    y = int(number[0])
    for i in range(1, len(number)):
        y = y * p + int(number[i])
    return y


print("Zadanie 7")
print(BinToP("1001", 2)) # 9
print(BinToP("12", 8)) # 10


# Zadanie 8
print("Zadanie 8")
