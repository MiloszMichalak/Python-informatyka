file = open("nominaly.txt", "r")
nominaly = list(map(int, file.readline().split()))
file.close()

a = int(input("Podaj kwotę do wydania: "))

while a != 0:
    ile = 0
    for nominal in nominaly:
        ile = a // nominal
        a = a % nominal
        if ile != 0:
            print(f"{ile}x{nominal}")