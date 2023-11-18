class Arma:
    def __init__(self, nombre, daño):
        self.nombre = nombre
        self.daño = daño

class Armadura:
    def __init__(self, nombre, defensa):
        self.nombre = nombre
        self.defensa = defensa

class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.arma = None
        self.armadura = None

    def equipar_arma(self, arma):
        self.arma = arma

    def equipar_armadura(self, armadura):
        self.armadura = armadura

    def quitar_arma(self):
        self.arma = None

    def quitar_armadura(self):
        self.armadura = None

    def calcular_daño_total(self):
        if self.arma is None:
            return 0
        return self.arma.daño

    def calcular_defensa_total(self):
        if self.armadura is None:
            return 0
        return self.armadura.defensa

    def recibir_daño(self, daño):
        defensa_total = self.calcular_defensa_total()
        daño_recibido = max(daño - defensa_total, 0)
        print(f"{self.nombre} recibe {daño_recibido} de daño.")

# Crear instancias de armas y armaduras
espada = Arma("Espada", 10)
escudo = Armadura("Escudo", 5)

# Crear instancia de personaje
personaje = Personaje("Aria")

# Equipar arma y armadura al personaje
personaje.equipar_arma(espada)
personaje.equipar_armadura(escudo)

# Calcular y mostrar el daño total del personaje
daño_total = personaje.calcular_daño_total()
print(f"Daño total del personaje: {daño_total}")

# Quitar el arma y calcular el daño total nuevamente
personaje.quitar_arma()
daño_total = personaje.calcular_daño_total()
print(f"Daño total del personaje después de quitar el arma: {daño_total}")