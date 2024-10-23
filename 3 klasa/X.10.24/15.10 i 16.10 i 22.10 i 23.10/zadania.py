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
    if sum(numbers) % 2 == 0:
        print(*numbers)

# zadanie 5a
print("Zadanie 5a")
file = open("slowa.txt", "r")
number = 1
for line in file:
    print(number, line.strip())
    number += 1
file.close()

# Zadanie 5b
print("Zadanie 5b")
file = open("slowa.txt", "r")
ile = 0
for line in file:
    ile += 1
print(ile)
file.close()

# Zadanie 5c
print("Zadanie 5c")
file = open("slowa.txt", "r")
for line in file:
    if str(line[0]) == 'A':
        print(line.strip())
file.close()

# Zadanie 5d
print("Zadanie 5d")
file = open("slowa.txt", "r")
for line in file:
    if str(line.strip()[-1]) == 'A':
        print(line.strip())
file.close()

# Zadanie 5e
print("Zadanie 5e")
file = open("slowa.txt", "r")
for line in file:
    print(line.strip(), len(line.strip()))
file.close()

# Zadanie 5f
print("Zadanie 5f")
file = open("slowa.txt", "r")
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
file = open("slowa.txt", "r")
for line in file:
    if len(line.strip()) == 6:
        print(line.strip())
file.close()

# Zdadanie 5h
print("Zadanie 5h")
file = open("slowa.txt", "r")
for line in file:
    if line.count('O') > 0:
        print(line.strip(), line.count('O'))
file.close()

# Zadanie 5i
print("Zadanie 5i")
file = open("slowa.txt", "r")
ile = 0
for line in file:
    ile += line.count('A')
print(ile)
file.close()

zapis = open(folder+"wyniki.txt", "w")
# Zadanie 6a
print("Zadanie 6a")
zapis.write("Zadanie 6a\n")

file = open("liczby.txt", "r")
zapis.write(f"Dlugosc {len(list(map(str, file)))}\n")
file.close()

# Zadanie 6b
print("Zadanie 6b")
zapis.write("Zadanie 6b\n")

file = open("liczby.txt", "r")
for line in file:
    if int(line.rstrip()[-1]) == 0:
        zapis.write(line)
file.close()

# Zadanie 6c
print("Zadanie 6c")
zapis.write("Zadanie 6c\n")

file = open("liczby.txt", "r")
for line in file:
    if int(line.strip()) == 0 or int(line.rstrip()[-3:]) == 000:
        zapis.write(line)
file.close()

# Zadanie 6d
print("Zadanie 6d")
zapis.write("Zadanie 6d\n")
file = open("liczby.txt", "r")
for line in file:
    if line.count('1') > line.count('0'):
        zapis.write(line)
file.close()

# Zadanie 6e
print("Zadanie 6d")
zapis.write("Zadanie 6d\n")
file = open("liczby.txt", "r")
for line in file:
    dec = int(line, 2)
    zapis.write(str(dec) + "\n")

file.close()
zapis.close()

# Zadanie 7
print("Zadanie 7")
zapis = open(folder+"losowe_w_linii.txt", "w")
for i in range(20):
    zapis.write(str(randint(1, 10)) + " ")
else:
    zapis.write("\n")

zapis.close()

file = open(folder+"losowe_w_linii.txt", "r")
numbers = list(map(int, file.readline().split()))
file.close()

liczby = [0] * 15
for line in numbers:
    liczby[int(line)] += 1

maksymalneLiczby = []

maks = max(liczby)
for i in range(len(liczby)):
    print(f"Liczba: {numbers[i]} ilosc: {liczby[i]}")
    if liczby[i] == maks:
        maksymalneLiczby.append(numbers[i])

print(set(maksymalneLiczby))


