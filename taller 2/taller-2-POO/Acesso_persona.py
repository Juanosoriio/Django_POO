from Persona import Persona

class AccesoPersona(Persona):
    def mostrar_info(self,persona:Persona):
        return(
            f"El nombre de la persona es {self.nombre}"
            f"La edad de la persona es {self.persona.get_edad()}"
        )