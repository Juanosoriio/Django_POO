from Persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre:str, edad:int,grado:str):
        super().__init__(nombre, edad)
        self.grado = grado
        
    def mostrar_info_completa(self):
        return(
            f"Nombre: {self.nombre} "
            f"Edad: {self.get_edad()} "
            f"Grado: {self.grado}"
        )