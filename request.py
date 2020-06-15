
# import the necessary packages 
import requests

# initialize the Keras REST API endpoint URL along with the input
# image path
KERAS_REST_API_URL = "http://localhost:5000/predict"

r = requests.post(KERAS_REST_API_URL,json={'YearsExperience':2})

print(r.json())