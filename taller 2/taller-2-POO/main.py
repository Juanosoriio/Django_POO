from Estudiante import Estudiante
from Curso import Curso

nombre_curso = input("Ingrese el nombre del curso: ")
curso = Curso(nombre_curso)

while True:
    pregunta = input("Desea inscribir estudiantes? si/no ").lower()
    if pregunta == "si":
        print("------Inscribir estudiante------")
        nombre = input("Ingrese el nombre: ")
        edad = int(input("Ingrese la edad: "))
        grado = input("Ingrese el grado: ")
        estudiante = Estudiante(nombre,edad,grado)
        
        curso.inscribir_estudiantes(estudiante)
    else:
        pregunta_final = input("Desea terminar? si/no ").lower()
        if pregunta_final == "si": break


curso.mostrar_estudiantes_inscritos()
