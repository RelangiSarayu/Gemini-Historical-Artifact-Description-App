from google import genai
import os

client = genai.Client(api_key="Place_your_api_here")

models = client.models.list()

for model in models:
    print(model.name)
