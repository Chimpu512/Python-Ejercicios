class Personaje():
    def __init__(self,nombre, clase, poder, fuerza, resistencia, velocidad):
        self.nombre = nombre
        self.clase = clase
        self.poder = poder
        self.fuerza = fuerza
        self.resistencia = resistencia
        self.velocidad = velocidad

    def __str__(self):
        return f"Personaje = {self.nombre} Clase = {self.clase} Poder = {self.poder}"
    
    def __repr__(self):
        return f"Pesonaje('{self.nombre}','{self.clase}','{self.poder}')"
    
    def __add__(self,otro):
        fusion_fuerza = self.fuerza + (otro.fuerza / 2) **2
        fusion_velocidad = (self.velocidad + otro.velocidad) **2
        return Personaje(self.nombre, self.clase, self.poder, fusion_fuerza, 
                 self.resistencia + otro.resistencia, fusion_velocidad)
        
mago = Personaje("Nebula","Mago","Lanzar hechizos",15,20,50)
rango = Personaje("Vortex","Rango","Disparar",20,30,25)
melee = Personaje("Solar","Cuerpo a cuerpo","Espada y lanza",60,50,10)
invocador = Personaje("Polvo estelar","Invocador","Invocar",10,15,30)

personaje_fusionado = invocador + mago
print(personaje_fusionado.fuerza)