from lavadora_base import LavadoraBase
import winsound

class LavadoraInteligente(LavadoraBase):
    def __init__(self, kilos, tipo_ropa, tiempo_lavado, potencia_kw, estrato, wifi=True, sensores=True):
        super().__init__(kilos, tipo_ropa, tiempo_lavado, potencia_kw, estrato)
        self._wifi = wifi
        self._sensores = sensores

    def detectar_tipo_ropa(self):
        # Ajusta parámetros automáticamente basado en tipo de ropa
        prendas_delicadas = ['interior', 'pijamas', 'vestidos']
        if any(prenda.lower() in prendas_delicadas for prenda in self._tipo_ropa):
            self._tiempo_lavado += 10  # Aumenta tiempo para prendas delicadas
            print("Sensores detectaron prendas delicadas, ajustando tiempo de lavado.")
        else:
            print("Sensores detectaron prendas normales.")

    def conectar_wifi(self):
        if self._wifi:
            print("Conectando a WiFi... Reporte enviado a la nube.")
        else:
            print("WiFi no disponible.")

    def lavar(self):
        winsound.PlaySound('sonidos/lavando.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
        print("Lavado INTELIGENTE optimizado con sensores...")