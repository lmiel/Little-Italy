import requests
import json
import os
import environ

env = environ.Env()
environ.Env.read_env()

class SpoonacularInfo:
    def __init__(self):
        self.api_key = "5524b40bfb124b5caf789a840299da19"
        self.base_url = "https://api.spoonacular.com"

    def get_recipes_by_name(self, name):
        url = self.base_url + "/recipes/complexSearch"
        url += f"?query={name}&apiKey={self.api_key}"
        response = requests.get(url).json()
        for result in response["results"]:
            print(result["title"])


api_requests = SpoonacularInfo()

api_requests.get_recipes_by_name("pizza")
        
    
