# Program 1
print("Program 1")

parts = input("Podaj liczbe binarna z przecinkiem: ").split(",")
partsTogether = "".join(parts)

nPotegi = len(parts[0]) - 1
n = len(partsTogether)
result = 0

for i in range(0, n):
    if partsTogether[i] == "1":
        result += 1 * (2 ** nPotegi)
    nPotegi -= 1
    
print(result)
    
