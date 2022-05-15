class Alumno:

    def __init__(self, nombre , nota):
        self.nombre = nombre
        self.nota = nota
    
    def calificacion(self):
        print(f"El alumno {self.nombre} ha obtenido la calificación de {self.nota}")
        if self.nota >= 5:
            print(f"{self. nombre} ha aprobado")
        else:
            print(f"{self. nombre} está suspenso")

alumnado = ['Jose', 'Maria', 'Joaquin', 'Nacho']
notas = [ 9 , 4 , 3, 10]

for i in range(len(alumnado)):
    x = Alumno(alumnado[i], notas[i])
    x.calificacion()
    