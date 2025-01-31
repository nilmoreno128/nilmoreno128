import os
import random
import time
import requests

# Get the token from the environment variable
gh_token = os.environ.get('GH_TOKEN')
if not gh_token:
    raise Exception("No token found in the GH_TOKEN environment variable.")

# List of possible descriptions for the status
descriptions = [
    "Working on new projects 🚀",
    "Reviewing code... 💻",
    "Focused on continuous improvement 🔧",
    "Exploring new ideas 💡",
    "Mediating between ideas and code 🖥️"
]

# Time interval for changing the status (in seconds)
interval = 3600  # 1 hour (you can adjust it to whatever you need)

# Define the URL for the GitHub status update endpoint
url = "https://api.github.com/user/status"

# Set up headers
headers = {
    "Authorization": f"token {gh_token}",
    "Accept": "application/vnd.github+json"
}

# Function to update GitHub status
def update_status():
    description = random.choice(descriptions)  # Choose a random status from the list

    # Set up the payload with the new status
    payload = {
        "emoji": ":rocket:",  # Emoji to show in the status
        "message": description  # Status message
    }

    # Make the PATCH request to the GitHub API
    response = requests.patch(url, json=payload, headers=headers)

    if response.status_code == 200:
        print(f"Status updated: {description}")
    else:
        print(f"Error updating status: {response.status_code} - {response.text}")

# Loop to change the status based on the interval
while True:
    update_status()  # Update the status
    time.sleep(interval)  # Wait for the interval before changing the status again
