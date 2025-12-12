from lavadora_base import LavadoraBase
import winsound

class LavadoraEstandar(LavadoraBase):
    def __init__(self, kilos, tipo_ropa, tiempo_lavado, potencia_kw, estrato):
        super().__init__(kilos, tipo_ropa, tiempo_lavado, potencia_kw, estrato)

    def lavar(self):
        winsound.PlaySound('sonidos/lavando.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
        print("Lavando en modo ESTÁNDAR…")