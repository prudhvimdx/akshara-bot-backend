from azure.ai.textanalytics import TextAnalyticsClient 

from azure.core.credentials import AzureKeyCredential 

 

def authenticate_client(): 

    key = "YOUR_AZURE_TEXT_ANALYTICS_KEY" 

    endpoint = "YOUR_AZURE_TEXT_ANALYTICS_ENDPOINT" 

    return TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key)) 

 

client = authenticate_client() 

 

def analyze_feedback(feedback): 

    response = client.analyze_sentiment(documents=[feedback])[0] 

    return response.sentiment 