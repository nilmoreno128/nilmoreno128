import requests
import os
from datetime import datetime

# Update the status message on GitHub
def update_status():
    url = "https://api.github.com/users/{username}"
    headers = {
        "Authorization": f"token {os.getenv('GH_TOKEN')}",
        "Content-Type": "application/json"
    }

    # Lista de mensajes de estado
    status_messages = [
        "Working on something cool!",
        "Taking a break, be back soon!",
        "In a meeting, will reply later!",
        "Looking for new project ideas!"
    ]
    
    # Usamos la hora actual para seleccionar un mensaje aleatorio de la lista
    new_status = status_messages[datetime.now().hour % len(status_messages)]
    
    payload = {
        "status": new_status,
        "emoji": ":smiley:",  # Emoji
        "expires_at": None  # No expiración
    }

    response = requests.patch(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        print(f"Status updated to: {new_status}")
    else:
        print(f"Failed to update status: {response.status_code} - {response.text}")

# Main function to run the update
if __name__ == "__main__":
    update_status()  # Ejecutar la actualización de estado una vez
