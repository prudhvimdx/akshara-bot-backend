from scripts import data_processing, ai_model, azure_integration 

 

def main(): 

    # Process data and upload to Azure Blob Storage 

    data_processing.process_data() 
    print("Data Processing Done")
 

    # Train the AI model and upload to Azure Machine Learning 

    ai_model.train_and_upload_model() 
    print("Train and Update Model Done")
 

    # Analyze feedback sentiment 

    feedback = input("Enter feedback for analysis: ") 

    # sentiment = azure_integration.analyze_feedback(feedback) 

    # print("Feedback Sentiment: ") 
    # print(f"Feedback Sentiment: {sentiment}") 

 

if __name__ == "__main__": 

    main() 