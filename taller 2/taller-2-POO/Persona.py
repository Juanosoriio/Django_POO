# Creamos la clase llamada persona
class Persona:
    # Iniciamos la función constructo y se parametrizan los atributos
    def __init__(self,nombre:str,edad:int):
        self.nombre = nombre
        self.__edad = edad
    
    def get_edad(self):
        return self.__edad
    
    def set_edad(self):
        if self.__edad >=1:
            self.__edad = int(input("Ingrese la nueva edad"))
        else:
            print("No puede cambiar la edad")