# Zadanie 2 = dodawanie binarnych

# def binToDec(number):
#     potega = 0
#     dec = 0
#     for i in range(len(number) - 1, -1, -1):
#         if number[i] == "1":
#             dec += 2**potega
#         potega += 1
#     return dec
# 
# def decToBin(number):
#     bin = ""
#     while number > 0:
#         if number % 2 == 0:
#             bin = "0" + bin
#         else:
#             bin = "1" + bin
#         number //= 2
#     return bin
#         
# 
# print("Zadanie 2")
# number1 = input("Podaj pierwsza liczbe binarną: ")
# number2 = input("Podaj druga liczbe binarną: ")
# 
# wynik = binToDec(number1) + binToDec(number2)
# print(decToBin(wynik))


# Zadanie 3
print("Zadanie 3")

# Napisz program obliczający sumę dwóch liczb w systemie o podstawie p (p w zakresie od 2 do 9). 
# Liczby i podstawa są podawane przez użytkownika. Wynik podaj w systemie o podstawie p.
# Możesz wykorzystać pośrednią zamianę na system dziesiętnym.

def pToDec(number, base, n):
    y = 0
    for i in range(1, n + 1):
        y = y * base + int(number[i])
    return y

print(pToDec("111", 8, 2))


