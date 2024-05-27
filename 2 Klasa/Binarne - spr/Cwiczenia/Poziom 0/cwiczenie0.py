print("Zadanie 1")

binarna = input("bin: ")

if binarna[-1] == "1":
    print("nie parzysta")
else:
    print("parzysta")

print()

print("Zadanie 2")
bin1, bin2 = input("Bin1: "), input("Bin2: ")

# dodawanie i odejmowanie
if bin1[-1] == bin2[-1]:
    print("parzysta")
else:
    print("nie parzysta")

# mnozenie
if (bin1[-1] == "0" or bin2[-1] == "0"):
    print("parzysta")
else:
    print("nie parzysta")

