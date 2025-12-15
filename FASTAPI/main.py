from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, model_validator
from typing import Optional
import json
app = FastAPI()

class Producto(BaseModel):
    nombre: str = Field(..., min_length=1)
    costo: float = Field(..., gt=0)
    categoria: str = Field(..., min_length=1)
    stock: int = Field(..., gt=0)
    peso: float = Field(..., gt=0)
    precio_venta: float = Field(..., gt=0)

    @model_validator(mode="after")
    def validar_precios(self):
        if self.precio_venta < self.costo:
            raise ValueError("El precio de venta no puede ser menor que el costo")
        return self

@app.get("/")
def read_index():
    return "hello, esta es la primera aplicación con FastAPI"

# Funciones para manejar el archivo JSON
def cargar_productos():
    try:
        with open('productos.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            # Convertir los datos del JSON a objetos Producto
            return {int(k): Producto(**v) for k, v in data.items()}
    except FileNotFoundError:
        # Si el archivo no existe, retornar la base de datos por defecto
        return {
            1: Producto(nombre="Laptop Lenovo", costo=1200.00, categoria="Tecnología", 
                       stock=10, peso=1.5, precio_venta=1500.00),
            2: Producto(nombre="Mouse Logitech", costo=50.00, categoria="Accesorios", 
                       stock=100, peso=0.2, precio_venta=80.00)
        }

def guardar_productos():
    # Convertir los objetos Producto a diccionarios para guardarlos en JSON
    data = {str(k): v.dict() for k, v in productos_db.items()}
    with open('productos.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

class ProductoPatch(BaseModel):
    nombre: Optional[str] = Field(None, min_length=1)
    costo: Optional[float] = Field(None, gt=0)
    categoria: Optional[str] = Field(None, min_length=1)
    stock: Optional[int] = Field(None, gt=0)
    peso: Optional[float] = Field(None, gt=0)
    precio_venta: Optional[float] = Field(None, gt=0)

# Base de datos cargada desde JSON
productos_db = cargar_productos()

@app.get("/productos/{id}")
def mostrar_producto(id: int): #Codigo mejorado 
    if id in productos_db:
        return {"data": productos_db[id]}
    else:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

@app.post("/productos/")
def crear_producto(producto: Producto):
    # Generar nuevo ID
    nuevo_id = max(productos_db.keys()) + 1 if productos_db else 1
    
    # Agregar el producto a la base de datos
    productos_db[nuevo_id] = producto
    
    # Guardar en el archivo JSON
    guardar_productos()
    
    return {"message": f"El Producto: {producto.nombre} fue creado exitosamente", "data": producto}

@app.put("/productos/{id}")
def actualizar_producto(id: int, producto: Producto):
    if id not in productos_db:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    productos_db[id] = producto
    guardar_productos()
    return {"message": "Producto actualizado", "data": producto}

@app.patch("/productos/{id}")
def actualizar_parcial_producto(id: int, producto: ProductoPatch):
    if id not in productos_db:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    producto_actual = productos_db[id]

    # Crear un diccionario con los valores actuales
    datos_actualizados = producto_actual.dict()

    # Actualizar solo los campos proporcionados
    for campo, valor in producto.model_dump(exclude_unset=True).items():
        datos_actualizados[campo] = valor

    # Validar el producto actualizado creando una nueva instancia
    producto_actualizado = Producto(**datos_actualizados)

    productos_db[id] = producto_actualizado
    guardar_productos()

    return {
        "message": "Producto actualizado parcialmente",
        "data": producto_actualizado
    }

@app.delete("/productos/{id}")
def eliminar_producto(id: int):
    if id not in productos_db:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    producto_eliminado = productos_db.pop(id)
    
    # Guardar cambios en el archivo JSON
    guardar_productos()
    
    return {
        "message": f"El producto '{producto_eliminado.nombre}' fue eliminado exitosamente.",
        "id": id
    }

@app.get("/productos")
def listar_productos():
    return {"data": productos_db}       