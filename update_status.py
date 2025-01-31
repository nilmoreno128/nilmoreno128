import requests
import os
from datetime import datetime

# Get the current GitHub status message
def get_current_status():
    url = "https://api.github.com/users/{username}"
    headers = {
        "Authorization": f"token {os.getenv('GH_TOKEN')}"
    }
    response = requests.get(url, headers=headers)
    response_data = response.json()

    if 'status' in response_data:
        return response_data['status']
    else:
        return None

# Update the status message on GitHub
def update_status():
    url = "https://api.github.com/users/{username}"
    headers = {
        "Authorization": f"token {os.getenv('GH_TOKEN')}",
        "Content-Type": "application/json"
    }
    
    status_messages = [
        "Working on something cool!",
        "Taking a break, be back soon!",
        "In a meeting, will reply later!",
        "Looking for new project ideas!"
    ]
    
    # You can customize the selection logic based on the time of day or other factors
    # For example, update to a random message from the list
    new_status = status_messages[datetime.now().hour % len(status_messages)]  # Simple logic to change status
    
    payload = {
        "status": new_status,
        "emoji": ":smiley:",  # You can customize the emoji
        "expires_at": None  # Set to None for no expiration
    }

    response = requests.patch(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        print(f"Status updated to: {new_status}")
    else:
        print(f"Failed to update status: {response.status_code} - {response.text}")

# Main function to run the update
if __name__ == "__main__":
    update_status()  # Update status once
