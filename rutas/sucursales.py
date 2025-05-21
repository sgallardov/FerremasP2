from fastapi import APIRouter, HTTPException
from modelos import sucursal

router = APIRouter(
    prefix="/sucursales",
    tags=["sucursales"]
)

@router.get("/", summary="Obtener todas las sucursales")
def listar_sucursales():
    resultado = sucursal.obtener_sucursales()
    if resultado is None:
        raise HTTPException(status_code=500, detail="No se pudieron obtener las sucursales")
    return resultado

@router.get("/{sucursal_id}", summary="Obtener sucursal por ID")
def obtener_sucursal(sucursal_id: int):
    resultado = sucursal.obtener_sucursal_por_id(sucursal_id)
    if resultado is None:
        raise HTTPException(status_code=404, detail="Sucursal no encontrada")
    return resultado