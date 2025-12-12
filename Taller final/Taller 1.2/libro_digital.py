from recurso_digital import Material

class LibroDigital(Material):
    def __init__(self, codigo, titulo, precio_base, autor, num_paginas):
        super().__init__(codigo, titulo, precio_base)
        self.autor = autor
        self.num_paginas = num_paginas

    def mostrar_informacion(self):
        return f"Libro: {self.titulo} por {self.autor}, {self.num_paginas} páginas"

    def calcular_costo_descarga(self):
        costo = self.precio_base
        if self.num_paginas > 300:
            costo *= 1.10
        return costo

    def obtener_tipo(self):
        return "Libro Digital"