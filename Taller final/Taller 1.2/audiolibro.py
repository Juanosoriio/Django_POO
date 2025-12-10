from recurso_digital import Material

class AudioLibro(Material):
    def __init__(self, codigo, titulo, precio_base, duracion, narrador):
        super().__init__(codigo, titulo, precio_base)
        self.duracion = duracion  # en minutos
        self.narrador = narrador

    def mostrar_informacion(self):
        return f"Audiolibro: {self.titulo}, Narrado por {self.narrador}, Duración: {self.duracion} minutos"

    def calcular_costo_descarga(self):
        costo = self.precio_base
        if self.duracion > 120:
            costo *= 1.20
        return costo

    def obtener_tipo(self):
        return "Audiolibro"