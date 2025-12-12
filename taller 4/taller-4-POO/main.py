from Principal import Clase_Principal
from VehiculoDeportivo import Vehiculo_Deportivo
from VehiculoFurgoneta import Vehiculo_Furgoneta
from VehiculoTurismo import Vehiculo_Turismo
from Vehiculo import Vehiculo

def main ():
    
    carro = Vehiculo("Padre","Padre","Padre")
    carro_1 = Vehiculo_Deportivo("ABC123","Mazda","M3",3)
    carro_2 = Vehiculo_Turismo("ABC456","Toyota","Corola",5)
    carro_3 = Vehiculo_Furgoneta("ABC789","Nissan","Furgoneta",6)

    principal = Clase_Principal(carro)
    principal1 = Clase_Principal(carro_1)
    principal2 = Clase_Principal(carro_2)
    principal3 = Clase_Principal(carro_3)

    principal.imprimir()
    principal1.imprimir()
    principal2.imprimir()
    principal3.imprimir()

main()