from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
import boto3
import zipfile
from huggingface_hub import login
import os

os.environ['HF_HOME'] = '/models/'

# Step 1: Download the model from Hugging Face
model_name = "mistralai/Mistral-7B-Instruct-v0.2"  # Change this to the model you want to download
bucket_name = "jose-app-models-bucket"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Step 2: Save the model to local storage
model.save_pretrained("models/mistralai/Mistral-7B-Instruct-v0.2")
tokenizer.save_pretrained("models/mistralai/Mistral-7B-Instruct-v0.2")
zipfile("models/mistralai/Mistral-7B-Instruct-v0.2", "models/mistralai/Mistral-7B-Instruct-v0.2.zip")

# Step 3: Upload the model to S3
s3 = boto3.client('s3')
s3.upload_file("models/mistralai/Mistral-7B-Instruct-v0.2.zip", bucket_name, "models/mistralai/Mistral-7B-Instruct-v0.2")