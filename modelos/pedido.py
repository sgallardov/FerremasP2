import requests

API_URL = "https://ea2p2assets-production.up.railway.app"
AUTH_TOKEN = "SaGrP9ojGS39hU9ljqbXxQ=="

HEADERS = {
    "Authorization": f"Bearer {AUTH_TOKEN}",
    "Content-Type": "application/json"
}

def obtener_pedidos():
    """
    Obtiene la lista de todos los pedidos.
    """
    try:
        response = requests.get(f"{API_URL}/pedidos", headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("Error al obtener pedidos:", e)
        return None

def obtener_pedido_por_id(pedido_id):
    """
    Obtiene los detalles de un pedido específico por su ID.
    """
    try:
        response = requests.get(f"{API_URL}/pedidos/{pedido_id}", headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error al obtener el pedido con ID {pedido_id}:", e)
        return None

def crear_pedido(data_pedido):
    """
    Crea un nuevo pedido con los datos proporcionados.
    """
    try:
        response = requests.post(f"{API_URL}/pedidos", json=data_pedido, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("Error al crear pedido:", e)
        return None