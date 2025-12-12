# Se crea clase carro
class Carro:
    # Se inicializan los atributos del carro
    def __init__(self, marca, color, velocidad_max):
        self.marca = marca
        self.color = color
        self.velocidad = 0
        self.velocidad_max = velocidad_max
        self.encendido = False
    
    # Metodo para encender carro
    def encender(self):
        if not self.encendido:
            self.encendido = True
            return f"El carro {self.marca} está encendido."
        return f"El carro {self.marca} ya está encendido."
    
    # Metodo para acelerar el carro
    def acelerar(self, aumento):
        if not self.encendido:
            return f"El carro {self.marca} debe estar encendido para acelerar."
    
        if self.velocidad + aumento <= self.velocidad_max:
            self.velocidad += aumento
        else:
            self.velocidad = self.velocidad_max
    
        return f"La velocidad actual del carro {self.marca} es {self.velocidad} km/h"

    
    def frenar(self):
        self.velocidad = 0
        return f"El carro {self.marca} se ha detenido"
    
    def __str__(self):
        return f"Carro {self.marca} de color {self.color}"
        