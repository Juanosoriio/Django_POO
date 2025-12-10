class Vehiculo:
    def __init__(self, matricula: str, marca: str, modelo: str):
        self._matricula = matricula
        self._marca = marca
        self._modelo = modelo
        
    def get_matricula(self) -> str:
        return self._matricula
    
    def get_marca(self) -> str:
        return self._marca
    
    def get_modelo(self) -> str:
        return self._modelo
    
    def mostrar_datos(self) -> str:
        return (
            "Datos clase vehiculo\n"
            f"Matriculas: {self.get_matricula()}\n"
            f"Marca: {self.get_marca()}\n"
            f"Modelo: {self.get_modelo()}\n")