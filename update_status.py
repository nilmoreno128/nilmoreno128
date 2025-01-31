import requests
import os
from datetime import datetime

# Function to update the status message on GitHub
def update_status():
    username = "nilmoreno128"  # Replace with your GitHub username
    url = f"https://api.github.com/users/{username}"  # GitHub API endpoint to update user data
    headers = {
        "Authorization": f"token {os.getenv('GH_TOKEN')}",  # Authorization header using GitHub token
        "Content-Type": "application/json"  # Specify the content type as JSON
    }

    # List of possible status messages
    status_messages = [
        "Working on something cool!",  # Example status message 1
        "Taking a break, be back soon!",  # Example status message 2
        "In a meeting, will reply later!",  # Example status message 3
        "Looking for new project ideas!"  # Example status message 4
    ]
    
    # Select a new status based on the current hour of the day (optional: you can modify this logic)
    new_status = status_messages[datetime.now().hour % len(status_messages)]
    
    # Payload to send in the API request (status and emoji)
    payload = {
        "status": new_status,  # New status message
        "emoji": ":smiley:",  # Emoji to associate with the status
        "expires_at": None  # No expiration time for the status
    }

    # Send the PATCH request to the GitHub API
    response = requests.patch(url, json=payload, headers=headers)

    # Check if the API request was successful
    if response.status_code == 200:
        print(f"Status updated to: {new_status}")  # Print success message if status is updated
    else:
        print(f"Failed to update status: {response.status_code} - {response.text}")  # Print error message if status update fails

# Run the update status function
if __name__ == "__main__":
    update_status()  # Call the function to update the status
