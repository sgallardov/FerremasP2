from fastapi import APIRouter, HTTPException
from modelos.pedido import obtener_pedidos, obtener_pedido_por_id, crear_pedido

router = APIRouter()

@router.get("/pedidos", response_model=list)
async def ruta_obtener_pedidos():
    """
    Endpoint para obtener la lista de todos los pedidos.
    """
    pedidos = obtener_pedidos()
    if pedidos is not None:
        return pedidos
    raise HTTPException(status_code=500, detail="No se pudieron obtener los pedidos")

@router.get("/pedidos/{pedido_id}", response_model=dict)
async def ruta_obtener_pedido_por_id(pedido_id: int):
    """
    Endpoint para obtener los detalles de un pedido específico por su ID.
    """
    pedido = obtener_pedido_por_id(pedido_id)
    if pedido is not None:
        return pedido
    raise HTTPException(status_code=404, detail=f"No se pudo encontrar el pedido con ID {pedido_id}")

@router.post("/pedidos", response_model=dict)
async def ruta_crear_pedido(data: dict):
    """
    Endpoint para crear un nuevo pedido.
    """
    if not data:
        raise HTTPException(status_code=400, detail="Datos del pedido no proporcionados")
    nuevo_pedido = crear_pedido(data)
    if nuevo_pedido is not None:
        return nuevo_pedido
    raise HTTPException(status_code=500, detail="No se pudo crear el pedido")