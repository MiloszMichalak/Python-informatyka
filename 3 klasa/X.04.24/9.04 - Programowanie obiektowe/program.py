class Prostokat:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def pole(self):
        return self.a * self.b

    def obwod(self):
        return 2 * (self.a + self.b)
    
    
class ProstokatEkstra(Prostokat):
    def __init__(self, a, b):
        super().__init__(a, b)

    def pole(self):
        return super().pole() * 2

    def obwod(self):
        return super().obwod() * 2
    
    def wyswietl_pole(self):
        print(f"Pole prostokąta: {self.pole()}")
        
    def wyswietl_obwod(self):
        print(f"Obwód prostokąta: {self.obwod()}")
    
    
obiekt1 = Prostokat(2, 3)
print(obiekt1.pole())
print(obiekt1.obwod())

a = int(input("Podaj długość a: "))
b = int(input("Podaj długość b: "))

obiekt2 = ProstokatEkstra(a, b)
print(obiekt2.pole())
print(obiekt2.obwod())
obiekt2.wyswietl_pole()
obiekt2.wyswietl_obwod()

