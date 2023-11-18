class Estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    def estudiar(self):
        print(f"El estudiante {self.nombre} de {self.edad} años del grado {self.grado} está estudiando en este momento")
   
nombre = input("Escribe el nombre del estudiante: ")
edad = input("Escribe la edad del estudiante: ")
grado = input("Escribe el grado en el que estudia: ")
pregunta = input("Escribe estudiar si deseas poner al estudiante a estudiar: ")
estudiante = Estudiante(nombre,edad,grado)
if pregunta.lower() == "estudiar":
    estudiante.estudiar()
else:
    print("El estudiante no está estudiando")