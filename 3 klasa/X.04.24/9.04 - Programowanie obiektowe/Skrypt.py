from socket import EAGAIN


class Osoba:
    def __init__(self, imie, nazwisko, wzrost, waga):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wzrost = wzrost
        self.waga = waga

    def powitanie(self):
        print(f"Witaj, {self.imie} {self.nazwisko}!")
        
        
    def informacje(self):
        print(f"Imię: {self.imie}")
        print(f"Nazwisko: {self.nazwisko}")
        print(f"Wzrost: {self.wzrost} cm")
        print(f"Waga: {self.waga} kg")
        

imie = input("Podaj imię: ")
nazwisko = input("Podaj nazwisko: ")
wzrost = int(input("Podaj wzrost (w cm): "))
waga = int(input("Podaj wagę (w kg): "))

osoba = Osoba(imie, nazwisko, wzrost, waga)
osoba.powitanie()
osoba.informacje()
