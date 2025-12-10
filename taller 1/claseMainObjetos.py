from carro import Carro
from carroelectrico import carroElectrico

carro_gasolina = Carro("Mazda", "Negro", 180)

print(carro_gasolina.encender())
print(carro_gasolina.acelerar(100))
print(carro_gasolina.frenar())
print(carro_gasolina, "\n")

carro_electrico = carroElectrico("Tesla", "Gris", 250, 100)

print(carro_electrico.encender())
print(carro_electrico.acelerar(100))
print(carro_electrico.acelerar(200))
print(carro_electrico.frenar())
print(carro_electrico)