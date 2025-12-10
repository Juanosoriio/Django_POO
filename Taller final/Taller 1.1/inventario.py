from dispositivo import Dispositivo

# ======================================
# INVENTARIO CON MÉTODOS MÁGICOS
# ======================================
class Inventario:
    def __init__(self):
        self._lista = []

    def agregar(self, dispositivo):
        self._lista.append(dispositivo)

    def __len__(self):
        """Método mágico: permite usar len(inventario)"""
        return len(self._lista)

    def __getitem__(self, index):
        """Método mágico: permite acceder inventario[i]"""
        return self._lista[index]

    def listar(self):
        return [str(d) for d in self._lista]

    def buscar_por_codigo(self, codigo):
        """Buscar un dispositivo por código."""
        for dispositivo in self._lista:
            if dispositivo._codigo == codigo:
                return dispositivo
        return None