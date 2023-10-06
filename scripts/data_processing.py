import pandas as pd 
import os
from azure.storage.blob import BlobServiceClient 

 

def process_data(): 

    # Load data (assuming CSV for simplicity) 

    data = pd.read_csv('./data/student_performance/data.csv') 

 

    # Preprocess data (dummy code) 

    data = data.dropna() 

 

    # Store data in Azure Blob Storage 
    connection_string = os.environ.get('BLOB_CONNECTION_STRING')

    blob_service_client = BlobServiceClient.from_connection_string(connection_string) 

    container_name = "datacontainer" 

    blob_client = blob_service_client.get_blob_client(container=container_name, blob="data.csv") 

    # Check if the blob exists
    blob_exists = blob_client.exists()

    if blob_exists:
        # If the blob exists, delete it
        blob_client.delete_blob()


    blob_client.upload_blob(data.to_csv(index=False)) 