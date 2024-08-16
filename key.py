import os
import requests
from dotenv import load_dotenv

load_dotenv()

subscription_key = os.getenv('AZURE_MAPS_KEY')
base_url = "https://atlas.microsoft.com/"
latitude = 47.6205
longitude = -122.3493

url = f"{base_url}search/address/reverse/json?api-version=1.0&subscription-key={subscription_key}&query={latitude},{longitude}"

response = requests.get(url)
print(response)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")