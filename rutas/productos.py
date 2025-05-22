from fastapi import APIRouter, HTTPException
from modelos.producto import obtener_productos, obtener_producto_por_id, crear_producto

router = APIRouter()

@router.get("/productos", response_model=list)
async def ruta_obtener_productos():
    productos = obtener_productos()
    if productos is not None:
        return productos
    raise HTTPException(status_code=500, detail="No se pudieron obtener los productos")

@router.get("/productos/{producto_id}", response_model=dict)
async def ruta_obtener_producto_por_id(producto_id: int):
    producto = obtener_producto_por_id(producto_id)
    if producto is not None:
        return producto
    raise HTTPException(status_code=404, detail=f"No se pudo encontrar el producto con ID {producto_id}")

@router.post("/productos", response_model=dict)
async def ruta_crear_producto(data: dict):
    if not data:
        raise HTTPException(status_code=400, detail="Datos del producto no proporcionados")
    nuevo_producto = crear_producto(data)
    if nuevo_producto is not None:
        return nuevo_producto
    raise HTTPException(status_code=500, detail="No se pudo crear el producto")

