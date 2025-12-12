from dispositivo import Dispositivo

class Computador(Dispositivo):
    def __init__(self, codigo, marca, precio, ram, procesador):
        super().__init__(codigo, marca, precio)
        self.ram = ram
        self.procesador = procesador

    def encender(self):
        return f"El computador {self._marca} está iniciando..."

    def obtener_info(self):
        return f"PC {self._marca} con {self.ram}GB RAM y CPU {self.procesador}"