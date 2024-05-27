# worek 5kg - 5metrow2
from math import pow, floor


# dzien urodzenia 13 / 2 = 1
# metoda prstokkatow bez dx
def f(x):
    return (-pow(x, 3)) + 2 * pow(x, 2) + x


def g(x):
    return (-pow(x, 3)) + 2 * pow(x, 2) + x + 1


def prostokatyNiedomiar(a, b, n, fun):
    dx = (b - a) / n
    suma = 0
    for i in range(n):
        suma += fun(a + i * dx) * dx
    return suma


# 15 + 13 = 28 przedzialow
powierzchniaDolnego = abs(prostokatyNiedomiar(0, 2, 28, f))

powierzchniaGornego = abs(prostokatyNiedomiar(1, 2, 28, g))

# powierzchnia dolnej dzialki
print(powierzchniaDolnego)

# powierzchnia gornej dzialki
print(powierzchniaGornego)

# Powierzchnia dzialki pod rzeka
print(powierzchniaDolnego)

# Ile workow nawozu potrzeba
print(floor((powierzchniaDolnego + powierzchniaGornego) * 1000 / 5) + 1)
