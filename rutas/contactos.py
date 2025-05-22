from fastapi import APIRouter, HTTPException
from modelos.contacto import enviar_contacto, obtener_solicitudes_contacto

router = APIRouter()

@router.post("/contacto", response_model=dict)
async def ruta_enviar_contacto(data: dict):
    """
    Endpoint para enviar una solicitud de contacto.
    """
    if not data.get("nombre_cliente") or not data.get("email_cliente") or not data.get("mensaje") or not data.get("vendedor_id"):
        raise HTTPException(status_code=400, detail="Faltan datos obligatorios en la solicitud de contacto")
    
    resultado = enviar_contacto(data)
    if resultado is not None:
        return {"mensaje": "Solicitud de contacto enviada exitosamente", "solicitud": resultado}
    raise HTTPException(status_code=500, detail="No se pudo enviar la solicitud de contacto")

@router.get("/contacto", response_model=list)
async def ruta_obtener_solicitudes_contacto():
    """
    Endpoint para obtener todas las solicitudes de contacto.
    """
    solicitudes = obtener_solicitudes_contacto()
    return solicitudes