# metoda prostokatow - potrzebna jest funkcja oraz trzy warianty tej metody

def f(x):
    return -x ** 2 + 6 * x + 2


# tutaj sie dzieli na 2 czyli bierze od srodka prostokata
def prostokaty1(a, b, n):
    dx = (b - a) / n
    s = 0
    for i in range(n):
        s += f(a + dx / 2 + i * dx) * dx
    return s


# tutaj nie dodaje nic czyli bierze od poczatku prostokata
def prostokaty2(a, b, n):
    dx = (b - a) / n
    suma = 0
    for i in range(n):
        suma += f(a + i * dx) * dx
    return suma


# tutaj dodaje cale dx czyli bierze od konca prostokata
def prostokaty3(a, b, n):
    dx = (b - a) / n
    s = 0
    for i in range(n):
        s += f(a + dx + i * dx) * dx
    return s


# metoda trapezow - bierze 2 wierzcholki i liczy ich pole
def trapezy1(a, b, n):
    dx = (b - a) / n
    s = 0
    for i in range(n):
        s += (f(a + i * dx) + f(a + (i + dx) * dx)) * dx / 2
    return s


# tworzy jeden duzy trapez
def trapezy2(a, b, n):
    dx = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += 2 * f(a + i * dx)
    return s * dx / 2


print(prostokaty1(3, 27, 10000000))
print(prostokaty2(3, 27, 10000000))
print(prostokaty3(3, 27, 10000000))
print(trapezy1(3, 27, 10000000))
print(trapezy2(3, 27, 10000000))
