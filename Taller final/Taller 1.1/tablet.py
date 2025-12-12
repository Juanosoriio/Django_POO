from dispositivo import Dispositivo

class Tablet(Dispositivo):
    def __init__(self, codigo, marca, precio, tamano):
        super().__init__(codigo, marca, precio)
        self.tamano = tamano

    def encender(self):
        return f"La tablet {self._marca} está encendida."

    def obtener_info(self):
        return f"Tablet {self._marca} de {self.tamano}\""