from Vehiculo import Vehiculo

class Vehiculo_Deportivo(Vehiculo):
    def __init__(self,matricula: str, marca: str, modelo: str, numero_puertas: int):
        super().__init__(matricula,marca,modelo)
        self._numero_puertas = numero_puertas
    
    def get_numero_puertas(self) -> int:
        return self._numero_puertas
    
    def mostrar_datos(self) -> str:
        return (
            "Datos clase vehiculo deportivo\n"
            f"Matriculas: {self.get_matricula()}\n"
            f"Marca: {self.get_marca()}\n"
            f"Modelo: {self.get_modelo()}\n"
            f"Puertas: {self.get_numero_puertas()}\n")