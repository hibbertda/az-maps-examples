from azure.mgmt.maps import AzureMapsManagementClient
from azure.mgmt.maps.models import MapsAccountSasToken, AccountSasParameters
from azure.identity import DefaultAzureCredential
import datetime
import os
from dotenv import load_dotenv
import requests

load_dotenv()

# Replace with your subscription ID and resource group name
subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
resource_group_name = os.getenv("RESOURCE_GROUP_NAME")
account_name = os.getenv("AZURE_MAPS_NAME")

# Authenticate with Azure
credential = DefaultAzureCredential()
maps_client = AzureMapsManagementClient(credential, subscription_id)

# Define the SAS token parameters
sas_parameters = AccountSasParameters(
    signing_key="primaryKey",
    principal_id=os.getenv("AZUREM_MAPS_PRINCIPAL_ID"),
    max_rate_per_second=500,
    start=datetime.datetime.utcnow().isoformat() + 'Z',
    expiry=(datetime.datetime.utcnow() + datetime.timedelta(hours=12)).isoformat() + 'Z',
    #regions=['eastus']
)

# Generate the SAS token
sas_token = maps_client.accounts.list_sas(resource_group_name, account_name, sas_parameters)
print(f"SAS Token: {sas_token.account_sas_token}")

base_url = "https://atlas.microsoft.com/"

latitude = 47.6205
longitude = -122.3493

#url = f"{base_url}search/address/reverse/json?api-version=1.0&query={latitude},{longitude}&{sas_token.account_sas_token}"\
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'jwt-sas {sas_token.account_sas_token}'
}
url = f"{base_url}search/address/reverse/json?api-version=1.0&query={latitude},{longitude}"

response = requests.get(url, headers=headers)
print(response)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")