# Azure Maps Examples

This repository contains examples for using Azure Maps.

## Setup

1. Clone the repository:

```bash
git clone https://github.com/hibbertda/az-maps-examples.git
cd az-maps-examples
```

2. Environmental Configuration:

    - Rename the **.env.example** file to **.env**

    ```bash
    mv .env.example .env
    ```

    - Open the **.env** file and populate the required information:

    ```shell
    # Azure
    AZURE_TENANT_ID="your-tenant-id"
    AZURE_SUBSCRIPTION_ID="your-subscription-id"
    RESOURCE_GROUP_NAME="your-resource-group-name"

    # Azure Maps
    AZURE_MAPS_CLIENT_ID="your-maps-client-id"
    AZURE_MAPS_KEY="your-maps-key"
    AZURE_MAPS_NAME="your-maps-name"
    AZUREM_MAPS_PRINCIPAL_ID="your-maps-principal-id"

    # Service Principal authentication 
    AZURE_CLIENT_ID="your-client-id"
    AZURE_CLIENT_SECRET="your-client-secret"
    ```

3. Install required modules:

```bash
pip install -r requirements.txt
```

## Usage

Once the environmental variables and dependancies are setup, you can run the examples provided in the repository to interact with Azure Maps.