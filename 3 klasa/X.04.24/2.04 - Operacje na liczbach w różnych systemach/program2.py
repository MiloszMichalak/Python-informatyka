def binToDec(number):
    potega = 0
    dec = 0
    for i in range(len(number) - 1, -1, -1):
        if number[i] == "1":
            dec += 2**potega
        potega += 1
    return dec

def decToBin(number):
    bin = ""
    while number > 0:
        if number % 2 == 0:
            bin = "0" + bin
        else:
            bin = "1" + bin
        number //= 2
    return bin


print("Zadanie 2")
number1 = input("Podaj pierwsza liczbe binarną: ")
number2 = input("Podaj druga liczbe binarną: ")

wynik = binToDec(number1) + binToDec(number2)
print(decToBin(wynik))