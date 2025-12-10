from dispositivo import Dispositivo

class Telefono(Dispositivo):
    def __init__(self, codigo, marca, precio, conectividad, camara):
        super().__init__(codigo, marca, precio)
        self.conectividad = conectividad
        self.camara = camara

    def encender(self):
        return f"El teléfono {self._marca} está encendiendo..."

    def obtener_info(self):
        return f"Teléfono {self._marca} con red {self.conectividad} y cámara {self.camara}MP"