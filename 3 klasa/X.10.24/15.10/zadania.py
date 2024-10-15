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
        print(numbers)
