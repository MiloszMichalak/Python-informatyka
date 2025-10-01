nominaly = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
rzymskie = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

a = int(input("Podaj liczbe do zamiany na rzymskie: "))

# for a in range(1, 4_001):
output = ""
for i in range(len(nominaly)):
    ile = a // nominaly[i]
    a = a % nominaly[i]
    if ile != 0:
        output += f"{ile * rzymskie[i]}"
print(output)