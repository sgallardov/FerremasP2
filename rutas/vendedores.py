from fastapi import APIRouter, HTTPException
from modelos.vendedor import obtener_vendedores, obtener_vendedor_por_id

router = APIRouter()

@router.get("/vendedores", response_model=list)
async def ruta_obtener_vendedores():
    """
    Endpoint para obtener la lista de todos los vendedores.
    """
    vendedores = obtener_vendedores()
    if vendedores is not None:
        return vendedores
    raise HTTPException(status_code=500, detail="No se pudieron obtener los vendedores")

@router.get("/vendedores/{vendedor_id}", response_model=dict)
async def ruta_obtener_vendedor_por_id(vendedor_id: int):
    """
    Endpoint para obtener los detalles de un vendedor específico por su ID.
    """
    vendedor = obtener_vendedor_por_id(vendedor_id)
    if vendedor is not None:
        return vendedor
    raise HTTPException(status_code=404, detail=f"No se pudo encontrar el vendedor con ID {vendedor_id}")