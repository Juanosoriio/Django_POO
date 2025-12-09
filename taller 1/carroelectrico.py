from carro import Carro

class carroElectrico(Carro):
    def __init__(self, marca, color, velocidad_max, bateria_max):
        super().__init__(marca, color, velocidad_max)
        self.bateria = bateria_max
        self.bateria_max = bateria_max
    
    def recargar(self):
        self.bateria = self.bateria_max
        return "Bateria cargada al 100%"
    
    def acelerar(self, aumento):
        if not self.encendido:
            return f"El carro {self.marca} esta apagado, enciendelo primero"
        
        if self.bateria <=0:
            return "Bateria agotada, no puedes acelerar"
        
        mensaje_velocidad = super().acelerar(aumento)
        
        self.bateria -= 5
        
        return f"{mensaje_velocidad} | Bateria: {self.bateria}%"
    
    def __str__(self):
        return f"Carro {self.marca} de color {self.color}"