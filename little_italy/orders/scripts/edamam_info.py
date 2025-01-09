import requests
import json
import os
from decouple import config

class EdamamInfo:
    def __init__(self):
        self.api_key = config("EDAMAM_API_KEY")
        self.app_id= config("EDAMAM_APPLICATION_ID")
        self.base_url = "https://api.edamam.com"


    def build_recipe(title, ingredients):
        return {
            "title": title,
            "ingr": ingredients
        }
         
    def get_nutrition_details(self, title, ingredients):
        url = self.base_url + "/api/nutrition-details"
        url += f"?app_id={self.app_id}&app_key={self.api_key}"
        print(EdamamInfo.build_recipe(title, ingredients))
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json"
        }
        response = requests.post(url, json=EdamamInfo.build_recipe(title, ingredients), headers=headers).json()
        print(response)
        return response


object_info = EdamamInfo()


test = object_info.get_nutrition_details("pizza", ["1 tomato", "parmesan 20g", "1 cup of water", "1 cup of flour"])
print(test)
