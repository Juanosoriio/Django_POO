from Estudiante import Estudiante

class Curso():
    def __init__(self, curso):
        self.curso = curso
        self.estudiantes = []
    
    def inscribir_estudiantes(self, estudiante:Estudiante):
        if not estudiante:
            print("No ingresaste un estudiante")
        else:
            self.estudiantes.append(estudiante)
        print(f"El estudiante {estudiante.nombre} se inscribio en el curso {self.curso}")

    def mostrar_estudiantes_inscritos(self):
        print(f"Estudiantes incritos en {self.curso}")
        for i in self.estudiantes:
            print(i.mostrar_info_completa())