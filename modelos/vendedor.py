import requests

API_URL = "https://ea2p2assets-production.up.railway.app"
AUTH_TOKEN = "SaGrP9ojGS39hU9ljqbXxQ=="

HEADERS = {
    "Authorization": f"Bearer {AUTH_TOKEN}",
    "Content-Type": "application/json"
}

def obtener_vendedores():
    """
    Obtiene la lista de todos los vendedores.
    """
    try:
        response = requests.get(f"{API_URL}/vendedores", headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("Error al obtener vendedores:", e)
        return None

def obtener_vendedor_por_id(vendedor_id):
    """
    Obtiene los detalles de un vendedor específico por su ID.
    """
    try:
        response = requests.get(f"{API_URL}/vendedores/{vendedor_id}", headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error al obtener el vendedor con ID {vendedor_id}:", e)
        return None

