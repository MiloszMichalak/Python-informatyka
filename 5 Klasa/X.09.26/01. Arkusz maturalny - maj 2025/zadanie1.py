# Algorytm od konca bierze pary i odwroca ja czyli 76 - 67 itd

# 1.1
def przestaw(n):
    r = n % 100
    a = r // 10
    b = r % 10
    n = n // 100
    if n > 0:
        w = a + 10 * b + 100 * przestaw(n)
    else:
        if a > 0:
            w = a + 10 * b
        else:
            w = b
    return w

print(przestaw(316498))  # 3
print(przestaw(43657688))  # 4
print(przestaw(154005710)) # 5
print(przestaw(998877665544321)) # 8

print()
# 1.2
# 1 F
# 2 P
# 3 P
# 4 F

# 1.3
def przestaw2(n):
    wynik = 0
    mnoznik = 1
    while True:
        r = n % 100
        a = r // 10
        b = r % 10
        n = n // 100
        if n > 0:
            wynik += (10 * b + a) * mnoznik
            mnoznik *= 100
        else:
            if a > 0:
                wynik += (10 * b + a) * mnoznik
            else:
                wynik += b * mnoznik
            break
    return wynik

print(przestaw2(316498))
print(przestaw2(43657688))
print(przestaw2(154005710))
print(przestaw(998877665544321))
