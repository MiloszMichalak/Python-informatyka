# Zadanie 1

# print("Zadanie 1")
# 
# file = open("liczby.txt")
# ciag = list(map(int, file.readline().split()))
# itemsNumber = len(ciag)
# 
# # sposobu mojego nie ma
# 
# #sposob prosty
# n = len(ciag)
# def prostySposob(n):
#     for len in range(1, n + 1):
#         for start in range(n - len + 1):
#             print(*ciag[start:start + len])
# 
# 
# prostySposob(len(ciag))
# 
# file.close()
# 
# 
# # Zadanie 2
# print("Zadanie 2")
# file = open("liczby.txt")
# ciag = list(map(int, file.readline().split()))
# itemsNumber = len(ciag)
# 
# def sposobProsty(ciag):
#     for i in range(itemsNumber):
#         for j in range(i, itemsNumber):
#             print(*ciag[i:j + 1])
# 
# 
# sposobProsty(ciag)
# 
# file.close()
# 
# # Zadanie 3
# print("Zadanie 3")
# file = open("liczby.txt")
# ciag = list(map(int, file.readline().split()))
# 
# 
# for i in range(len(ciag) - 4):
#     podciag = ciag[i:i + 5]
#     suma = sum(podciag)
#     print(podciag, suma)
# 
# file.close()
# 
# # Zadanie 4
# print("Zadanie 4")
# file = open("liczby.txt")
# ciag = list(map(int, file.readline().split()))
# file.close()
# 
# for i in range(len(ciag) - 2):
#     podciag = ciag[i:i + 3]
#     print(podciag)
# 
# # Zadanie 6
# print("Zadanie 6")
# 
# def wypiszTakLubNie(czy: bool) -> str:
#     if czy:
#         return "Tak"
#     return "Nie"
# 
# ciag = list(map(int, input("Podaj ciag liczb: ").split()))
# 
# def czy_rosnacy(ciag: []) -> bool:
#     for i in range(len(ciag) - 1):
#         if ciag[i] >= ciag[i + 1]:
#             return False
#     return True
# 
# print(wypiszTakLubNie(czy_rosnacy(ciag)))
# 
# # Zadanie 7
# print("Zadanie 7")
# ciag = list(map(int, input("Podaj ciag liczb: ").split()))
# 
# def czy_malejacy(ciag: []) -> bool:
#     for i in range(len(ciag) - 1):
#         if ciag[i] <= ciag[i + 1]:
#             return False
#     return True
# 
# print(wypiszTakLubNie(czy_malejacy(ciag)))
# 
# # Zadanie 8
# print("Zadanie 8")
# ciag = list(map(int, input("Podaj ciag liczb: ").split()))
# 
# def czy_nierosnacy(ciag: []) -> bool:
#     for i in range(len(ciag) - 1):
#         if ciag[i] < ciag[i + 1]:
#             return False
#     return True
# 
# print(wypiszTakLubNie(czy_nierosnacy(ciag)))
# 
# # Zadanie 9
# print("Zadanie 9")
# ciag = list(map(int, input("Podaj ciag liczb: ").split()))
# 
# def czy_niemalejacy(ciag: []) -> bool:
#     for i in range(len(ciag) - 1):
#         if ciag[i] > ciag[i + 1]:
#             return False
#     return True
# 
# print(wypiszTakLubNie(czy_niemalejacy(ciag)))
# 
# # Zadanie 10
# print("Zadanie 10")
# ciag = list(map(int, input("Podaj ciag liczb: ").split()))
# 
# def czy_staly(ciag: []) -> bool:
#     for i in range(len(ciag) - 1):
#         if ciag[i] != ciag[i + 1]:
#             return False
#     return True
# 
# print(wypiszTakLubNie(czy_staly(ciag)))
# 
# # Zadanie 11
# print("Zadanie 11")
# 
# file = open("liczby.txt")
# ciag = list(map(int, file.readline().split()))
# file.close()
# 
# maksymalna_dlugosc = 0
# aktualna_dlugosc = 1
# n = len(ciag)
# for i in range(1, n):
#     if ciag[i] >= ciag[i - 1]:
#         aktualna_dlugosc += 1
#     else:
#         maksymalna_dlugosc = max(maksymalna_dlugosc, aktualna_dlugosc)
#         aktualna_dlugosc = 1
#         
# print(maksymalna_dlugosc)
        
        
# Zadanie 12
print("Zadanie 12")

file = open("liczby.txt")
ciag = list(map(int, file.readline().split()))
print(ciag)

file.close()

podciagi = []
podciag = []

for i in range(1, len(ciag)):
    if ciag[i] >= ciag[i - 1]:
        if not podciag:
            podciag.append(ciag[i - 1])
        podciag.append(ciag[i])
    else:
        if len(podciag) > 1:
            podciagi.append(podciag)
        podciag = []
        
        
print(podciagi)

