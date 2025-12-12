from Vehiculo import Vehiculo

class Vehiculo_Turismo(Vehiculo):
    def __init__(self, num_ventanas: int,matricula: str, marca: str, modelo: str):
        super().__init__(matricula,marca,modelo)
        self._num_ventanas = num_ventanas
    
    def get_num_ventanas(self) -> int:
        return self._num_ventanas
    
    def mostrar_datos(self) -> str:
        return (
            "Datos clase vehiculo turismo\n"
            f"Matriculas: {self.get_matricula()}\n"
            f"Marca: {self.get_marca()}\n"
            f"Modelo: {self.get_modelo()}\n"
            f"Ventanas: {self.get_num_ventanas()}\n")