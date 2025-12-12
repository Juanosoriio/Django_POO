from VehiculoTurismo import Vehiculo_Turismo
from VehiculoDeportivo import Vehiculo_Deportivo
from VehiculoFurgoneta import Vehiculo_Furgoneta

class Clase_Principal ():
    def __init__(self, vehiculo):
        self._vehiculo = vehiculo
    
    def imprimir(self):
        print(self._vehiculo.mostrar_datos())