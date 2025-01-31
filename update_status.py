import os
import random
import time
import requests

# Obtiene el token desde la variable de entorno
gh_token = os.environ.get('GH_TOKEN')
if not gh_token:
    raise Exception("No se encontró el token en la variable GH_TOKEN.")

# Lista de posibles descripciones para el estado
descriptions = [
    "Trabajando en nuevos proyectos 🚀",
    "Revisando código... 💻",
    "Enfocado en la mejora continua 🔧",
    "Explorando nuevas ideas 💡",
    "Mediando entre ideas y código 🖥️"
]

# Intervalo de tiempo para cambiar el estado (en segundos)
interval = 3600  # 1 hora (puedes ajustarlo a lo que necesites)

# Define la URL del endpoint para actualizar el estado
url = "https://api.github.com/user/status"

# Configura las cabeceras
headers = {
    "Authorization": f"token {gh_token}",
    "Accept": "application/vnd.github+json"
}

# Función para actualizar el estado de GitHub
def update_status():
    description = random.choice(descriptions)  # Elige un estado aleatorio de la lista

    # Configura el payload con el nuevo estado
    payload = {
        "emoji": ":rocket:",  # Emoji que se mostrará en el estado
        "message": description  # Mensaje del estado
    }

    # Realiza la petición PATCH a la API de GitHub
    response = requests.patch(url, json=payload, headers=headers)

    if response.status_code == 200:
        print(f"Estado actualizado: {description}")
    else:
        print(f"Error al actualizar el estado: {response.status_code} - {response.text}")

# Bucle para cambiar el estado según el intervalo
while True:
    update_status()  # Actualiza el estado
    time.sleep(interval)  # Espera el intervalo antes de cambiar el estado
