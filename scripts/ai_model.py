import pandas as pd 

from sklearn.cluster import KMeans 

from azureml.core import Workspace, Dataset, Experiment 

import os

def train_and_upload_model(): 

    # Load data from Azure Blob Storage 
    connection_string = os.environ.get('BLOB_CONNECTION_STRING')

    data = pd.read_csv('./data/student_performance/data.csv') 

 

    # Train a simple clustering model for personalized learning 

    model = KMeans(n_clusters=3) 

    model.fit(data) 

 

    # Save the model 

    import joblib 

    joblib.dump(model, 'student_model.pkl') 

 

    # Upload model to Azure Machine Learning 

    ws = Workspace.from_config() 

    datastore = ws.get_default_datastore() 

    datastore.upload(src_dir='./', target_path='model/')  

 