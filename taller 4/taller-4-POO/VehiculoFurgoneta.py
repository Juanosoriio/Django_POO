from Vehiculo import Vehiculo

class Vehiculo_Furgoneta(Vehiculo):
    def __init__(self,matricula: str, marca: str, modelo: str, numero_puestos: int):
        super().__init__(matricula,marca,modelo)
        self._numero_puestos = numero_puestos
    
    def get_numero_puestos(self) -> int:
        return self._numero_puestos
    
    def mostrar_datos(self) -> str:
        return (
            "Datos clase vehiculo furgoneta\n"
            f"Matriculas: {self.get_matricula()}\n"
            f"Marca: {self.get_marca()}\n"
            f"Modelo: {self.get_modelo()}\n"
            f"Puestos: {self.get_numero_puestos()}\n")