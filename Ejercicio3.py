class Animal:
    def comer(self):
        print("El animal está comiendo")
class Mamífero(Animal):
    def amamantar(self):
        print("El mamífero está amamantando")
class Ave(Animal):
    def volar(self):
        print("El ave está volando")
class Murcielago(Mamífero,Ave,Animal):
    def comer(self):
        print("El murcielago está comiendo")
    def volar(self):
        print("El murcielago está volando")
    def amamantar(self):
        print("El murcielago está amamantando")

m = Murcielago()
m.comer()mro