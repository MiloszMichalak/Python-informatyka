# Zadanie 3
print("Zadanie 3")

def pToDec(number, base):
    y = int(number[0])
    for i in range(1, len(number)):
        y = y * base + int(number[i])
    return y

number1 = input("Podaj liczbę w systemie 2-9: ")
number2 = input("Podaj liczbę w systemie 2-9: ")
base1 = int(input("Podaj system liczbowy: "))
sum1 = pToDec(number1, base1) + pToDec(number2, base1)
print(sum1)

