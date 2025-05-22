from fastapi import APIRouter, HTTPException
from modelos.usuario import obtener_usuarios, obtener_usuario_por_id, crear_usuario, verificar_permiso

router = APIRouter()

@router.get("/usuarios", response_model=list)
async def ruta_obtener_usuarios():
    """
    Endpoint para obtener la lista de todos los usuarios.
    """
    usuarios = obtener_usuarios()
    if usuarios is not None:
        return usuarios
    raise HTTPException(status_code=500, detail="No se pudieron obtener los usuarios")

@router.get("/usuarios/{usuario_id}", response_model=dict)
async def ruta_obtener_usuario_por_id(usuario_id: int):
    """
    Endpoint para obtener los detalles de un usuario específico por su ID.
    """
    usuario = obtener_usuario_por_id(usuario_id)
    if usuario is not None:
        return usuario
    raise HTTPException(status_code=404, detail=f"No se pudo encontrar el usuario con ID {usuario_id}")

@router.post("/usuarios", response_model=dict)
async def ruta_crear_usuario(data: dict):
    """
    Endpoint para crear un nuevo usuario.
    """
    if not data:
        raise HTTPException(status_code=400, detail="Datos del usuario no proporcionados")
    nuevo_usuario = crear_usuario(data)
    if nuevo_usuario is not None:
        return nuevo_usuario
    raise HTTPException(status_code=500, detail="No se pudo crear el usuario")

@router.get("/usuarios/{usuario_id}/permisos", response_model=list)
async def ruta_obtener_permisos(usuario_id: int):
    """
    Endpoint para obtener los permisos de un usuario basado en su rol.
    """
    usuario = obtener_usuario_por_id(usuario_id)
    if usuario is None:
        raise HTTPException(status_code=404, detail=f"No se pudo encontrar el usuario con ID {usuario_id}")
    
    rol = usuario.get("role")
    permisos = verificar_permiso(rol, None)  # Devuelve todos los permisos del rol
    return permisos