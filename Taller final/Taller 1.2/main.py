from libro_digital import LibroDigital
from revista_digital import RevistaDigital
from audiolibro import AudioLibro
from curso_virtual import CursoVirtual
from inventario_biblioteca import InventarioBiblioteca

# Crear inventario
inventario = InventarioBiblioteca()

# Crear un objeto de cada tipo
libro = LibroDigital("LIB001", "El Quijote", 20.0, "Miguel de Cervantes", 350)
revista = RevistaDigital("REV001", "Science Today", 10.0, "Edición 2023", "científico")
audiolibro = AudioLibro("AUD001", "Harry Potter", 15.0, 150, "Jim Dale")
curso = CursoVirtual("CUR001", "Python Básico", 50.0, "Programación", 20)

# Agregar al inventario
inventario.agregar_recurso(libro)
inventario.agregar_recurso(revista)
inventario.agregar_recurso(audiolibro)
inventario.agregar_recurso(curso)

# Imprimir lista completa
print("Lista completa de recursos:")
inventario.listar_recursos()
print()

# Imprimir costos individuales
print("Costos individuales:")
for recurso in inventario:
    print(f"{recurso.titulo}: ${recurso.calcular_costo_descarga():.2f}")
print()

# Generar reporte final
inventario.generar_reporte()