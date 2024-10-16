from random import randint

folder = "Odpowiedzi/"

# Zadanie 1
print("Zadanie 1")
file = open(folder+"dane_osobowe.txt", "w")
name = input("Podaj imie: ")
surname = input("Podaj nazwisko: ")
file.write(name+"\n")
file.write(surname)

file.close()

# Zadanie 2
print("Zadanie 2")
file = open(folder+"dane_osobowe.txt", "r")
imie = file.readline().strip()
nazwisko = file.readline()
print(f"Witaj {imie} i {nazwisko}")

file.close()

# Zadanie 3b
print("Zadanie 3a")
file = open(folder+"losowe.txt", "w")
for i in range(10):
    file.write(str(randint(1, 10)) + "\n")
file.close()

# Zdadanie 3b
file = open(folder+"losowe.txt", "r")
numbers = []
for i in file:
    numbers.append(int(i.strip()))
print(f"Min: {min(numbers)}")
print(f"Max: {max(numbers)})")
print(f"Avg: {sum(numbers) / len(numbers)}")

file.close()

# Zadanie 4
print("Zadanie 4")
file = open("ciagi.txt", "r")
for i in file:
    numbers = list(map(int, i.split()))
    if len(numbers) % 2 == 0:
        print(*numbers)

# zadanie 5a
print("Zadanie 5a")
file = open("slowa.txt")
number = 1
for line in file:
    print(number, line.strip())
    number += 1
file.close()

# Zadanie 5b
print("Zadanie 5b")
file = open("slowa.txt")
ile = 0
for line in file:
    ile += 1
print(ile)
file.close()

# Zadanie 5c
print("Zadanie 5c")
file = open("slowa.txt")
for line in file:
    if str(line[0]) == 'A':
        print(line.strip())
file.close()

# Zadanie 5d
print("Zadanie 5d")
file = open("slowa.txt")
for line in file:
    if str(line.strip()[-1]) == 'A':
        print(line.strip())
file.close()

# Zadanie 5e
print("Zadanie 5e")
file = open("slowa.txt")
for line in file:
    print(line.strip(), len(line.strip()))
file.close()

# Zadanie 5f
print("Zadanie 5f")
file = open("slowa.txt")
dlugosci = []
slowa = []

for line in file:
    dlugosci.append(len(line.strip()))
    slowa.append(line.strip())

mini = min(dlugosci)
maxi = max(dlugosci)

indexMin = dlugosci.index(mini)
indexMax = dlugosci.index(maxi)
print(slowa[indexMin], mini)
print(slowa[indexMax], maxi)

file.close()

# Zadanie  5g
print("Zadanie 5g")
file = open("slowa.txt")
for line in file:
    if len(line.strip()) == 6:
        print(line.strip())
file.close()

# Zdadanie 5h
print("Zadanie 5h")
file = open("slowa.txt")
for line in file:
    if line.count('O') > 0:
        print(line.strip(), line.count('O'))
file.close()

# Zadanie 5i
print("Zadanie 5i")
file = open("slowa.txt")
ile = 0
for line in file:
    ile += line.count("O")
file.close()
