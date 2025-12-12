from computador import Computador
from tablet import Tablet
from telefono import Telefono
from inventario import Inventario

# ======================================
# PROGRAMA PRINCIPAL (MAIN)
# ======================================
if __name__ == "__main__":
    pc = Computador("PC01", "HP", 2500000, 16, "i7")
    tablet = Tablet("TAB1", "Samsung", 1200000, 10.5)
    phone = Telefono("TEL1", "Xiaomi", 900000, "5G", 48)
    inventario = Inventario()
    inventario.agregar(pc)
    inventario.agregar(tablet)
    inventario.agregar(phone)

    print("\n=== LISTA DE DISPOSITIVOS ===")
    for d in inventario.listar():
        print(d)

    print("\nEncendiendo dispositivos:")
    print(pc.encender())
    print(tablet.encender())
    print(phone.encender())

    print("\nInformación detallada:")
    for d in inventario:
        print(d.obtener_info())

    print(f"\nTotal de dispositivos: {len(inventario)}")

    # Ejemplo de búsqueda
    dispositivo_buscado = inventario.buscar_por_codigo("PC01")
    if dispositivo_buscado:
        print(f"\nDispositivo encontrado: {dispositivo_buscado}")
    else:
        print("\nDispositivo no encontrado.")