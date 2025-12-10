class InventarioBiblioteca:
    def __init__(self):
        self.recursos = []

    def agregar_recurso(self, recurso):
        self.recursos.append(recurso)

    def listar_recursos(self):
        for recurso in self.recursos:
            print(recurso)

    def __len__(self):
        return len(self.recursos)

    def __getitem__(self, index):
        return self.recursos[index]

    def generar_reporte(self):
        total = 0
        print("Reporte de Inventario:")
        for recurso in self.recursos:
            costo = recurso.calcular_costo_descarga()
            print(f"Tipo: {recurso.obtener_tipo()}, Título: {recurso.titulo}, Costo de descarga: ${costo:.2f}")
            total += costo
        print(f"Total final de todos los recursos: ${total:.2f}")