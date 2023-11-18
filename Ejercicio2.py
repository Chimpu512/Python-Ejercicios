class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def mostrar_datos(self):
        print(f"Me llamo {self.nombre}, mi edad es {self.edad}")
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre,edad)
        self.grado = grado
    def mostrar_grado(self):
        print(f"Mi grado es {self.grado}")
    
Juan = Estudiante("Juan","15","2°")
Juan.mostrar_datos()
Juan.mostrar_grado()