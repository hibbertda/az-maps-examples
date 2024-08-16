import os
import requests
from dotenv import load_dotenv
from azure.identity import ClientSecretCredential

load_dotenv()

# Load service principal credentials from environment variables
client_id = os.getenv("AZURE_CLIENT_ID")
tenant_id = os.getenv("AZURE_TENANT_ID")
client_secret = os.getenv("AZURE_CLIENT_SECRET")

# Authenticate using the service principal
credential = ClientSecretCredential(
    tenant_id=tenant_id,
    client_id=client_id,
    client_secret=client_secret
)

# Define the base URL for Azure Maps
base_url = "https://atlas.microsoft.com/"

# Get the access token
url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"
payload = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
    'resource': base_url
}
response = requests.post(url, data=payload)
access_token = response.json().get('access_token')
print(access_token)


# Example: Reverse Geocoding
latitude = 47.6205
longitude = -122.3493

# Construct the request URL
url = f"{base_url}search/address/reverse/json?api-version=1.0&query={latitude},{longitude}"

# Set up the headers with the access token
headers = {
    "x-ms-client-id": os.getenv("AZURE_MAPS_CLIENT_ID"), #Azure Maps Client ID
    "Authorization": f"Bearer {access_token}" # User/SP Access Token
}

# Make the request to Azure Maps API
response = requests.get(url, headers=headers)

# Check and handle the response
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
