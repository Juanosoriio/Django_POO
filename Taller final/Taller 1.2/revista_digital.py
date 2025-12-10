from recurso_digital import Material

class RevistaDigital(Material):
    def __init__(self, codigo, titulo, precio_base, edicion, tema):
        super().__init__(codigo, titulo, precio_base)
        self.edicion = edicion
        self.tema = tema

    def mostrar_informacion(self):
        return f"Revista: {self.titulo}, Edición {self.edicion}, Tema: {self.tema}"

    def calcular_costo_descarga(self):
        costo = self.precio_base
        if self.tema.lower() == "científico":
            costo *= 1.15
        return costo

    def obtener_tipo(self):
        return "Revista Digital"