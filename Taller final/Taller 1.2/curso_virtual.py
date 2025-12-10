from recurso_digital import Material

class CursoVirtual(Material):
    def __init__(self, codigo, titulo, precio_base, categoria, horas):
        super().__init__(codigo, titulo, precio_base)
        self.categoria = categoria
        self.horas = horas

    def mostrar_informacion(self):
        return f"Curso Virtual: {self.titulo}, Categoría: {self.categoria}, Duración: {self.horas} horas"

    def calcular_costo_descarga(self):
        costo = self.precio_base
        if self.horas > 15:
            costo *= 1.25
        return costo

    def obtener_tipo(self):
        return "Curso Virtual"