import tkinter as tk

# Funkcja rysująca Dywan Sierpińskiego
def rysuj_dywan(x, y, rozmiar, stopien):
    if stopien == 0:
        # Rysowanie kwadratu
        canvas.create_rectangle(x, y, x + rozmiar, y + rozmiar, fill="black")
    else:
        # Dzielimy kwadrat na 9 mniejszych kwadratów i usuwamy środkowy
        nowy_rozmiar = rozmiar / 3
        # Rekurencyjnie rysujemy pozostałe kwadraty
        for i in range(3):
            for j in range(3):
                if i != 1 or j != 1:  # Pomijamy środkowy kwadrat
                    rysuj_dywan(x + i * nowy_rozmiar, y + j * nowy_rozmiar, nowy_rozmiar, stopien - 1)

# Ustawienia okna
root = tk.Tk()
root.title("Dywan Sierpińskiego")

# Ustawienia płótna
canvas = tk.Canvas(root, width=1920, height=1080)
canvas.pack()

# Parametry rysowania
rozmiar = 750  # Rozmiar początkowego kwadratu
stopien = 6  # Stopień fraktala (ilość poziomów)

# Wywołanie funkcji rysującej
rysuj_dywan(20, 20, rozmiar, stopien)

# Uruchomienie pętli aplikacji
root.mainloop()
