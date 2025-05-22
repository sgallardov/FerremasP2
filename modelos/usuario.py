import requests

API_URL = "https://ea2p2assets-production.up.railway.app"
AUTH_TOKEN = "SaGrP9ojGS39hU9ljqbXxQ=="

HEADERS = {
    "Authorization": f"Bearer {AUTH_TOKEN}",
    "Content-Type": "application/json"
}

# Definimos los permisos asociados a cada rol
ROLES_PERMISOS = {
    "admin": ["crear_producto", "editar_producto", "eliminar_producto", "ver_pedidos", "gestionar_usuarios"],
    "mantenedor": ["crear_producto", "editar_producto", "ver_pedidos"],
    "jefe_tienda": ["ver_pedidos", "gestionar_vendedores"],
    "bodega": ["ver_pedidos"],
    "cliente": ["ver_productos", "realizar_pedido"],
    "service_account": ["integracion_externa"]
}

def obtener_usuarios():
    """
    Obtiene la lista de todos los usuarios.
    """
    try:
        response = requests.get(f"{API_URL}/usuarios", headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("Error al obtener usuarios:", e)
        return None

def obtener_usuario_por_id(usuario_id):
    """
    Obtiene los detalles de un usuario específico por su ID.
    """
    try:
        response = requests.get(f"{API_URL}/usuarios/{usuario_id}", headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error al obtener el usuario con ID {usuario_id}:", e)
        return None

def crear_usuario(data_usuario):
    """
    Crea un nuevo usuario con los datos proporcionados.
    """
    try:
        response = requests.post(f"{API_URL}/usuarios", json=data_usuario, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("Error al crear usuario:", e)
        return None

def obtener_permisos_por_rol(rol):
    """
    Devuelve la lista de permisos asociados a un rol específico.
    """
    return ROLES_PERMISOS.get(rol, [])

def verificar_permiso(rol, permiso):
    """
    Verifica si un rol tiene un permiso específico.
    """
    permisos = obtener_permisos_por_rol(rol)
    return permiso in permisos