import pandas as pd 

from azure.storage.blob import BlobServiceClient 

 

def process_data(): 

    # Load data (assuming CSV for simplicity) 

    data = pd.read_csv('./data/student_performance/data.csv') 

 

    # Preprocess data (dummy code) 

    data = data.dropna() 

 

    # Store data in Azure Blob Storage 
    # Bu3f8DUujWDmOW6Lv6XWoiwTe4b97F5OwIdqK1u1v4KVeik3IztHhunz4tJR7LBgKTcy7DqRuZmb+AStfghZNQ==
    # DefaultEndpointsProtocol=https;AccountName=aksharaai;AccountKey=Bu3f8DUujWDmOW6Lv6XWoiwTe4b97F5OwIdqK1u1v4KVeik3IztHhunz4tJR7LBgKTcy7DqRuZmb+AStfghZNQ==;EndpointSuffix=core.windows.net
    connection_string = "DefaultEndpointsProtocol=https;AccountName=aksharaai;AccountKey=Bu3f8DUujWDmOW6Lv6XWoiwTe4b97F5OwIdqK1u1v4KVeik3IztHhunz4tJR7LBgKTcy7DqRuZmb+AStfghZNQ==;EndpointSuffix=core.windows.net" 

    blob_service_client = BlobServiceClient.from_connection_string(connection_string) 

    container_name = "datacontainer" 

    blob_client = blob_service_client.get_blob_client(container=container_name, blob="data.csv") 

    # Check if the blob exists
    blob_exists = blob_client.exists()

    if blob_exists:
        # If the blob exists, delete it
        blob_client.delete_blob()


    blob_client.upload_blob(data.to_csv(index=False)) 