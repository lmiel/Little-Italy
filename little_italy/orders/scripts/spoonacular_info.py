import requests
# ESTO LE HE CAMBIADO PQ NO ME IBA LO DEL ENVIRON
"""

import json"""
import os
from decouple import config


import requests

class SpoonacularInfo:
    def __init__(self):
        self.api_key = config("SPOONACULAR_API_KEY")
        self.base_url = "https://api.spoonacular.com"

    def get_recipes_by_name(self, name):
        """
        Realiza una solicitud a la API de Spoonacular para buscar recetas por nombre.

        :param name: Nombre de la receta (ejemplo: "pizza")
        :return: Respuesta de la API en formato JSON
        """
        url = f"{self.base_url}/recipes/complexSearch?query={name}&apiKey={self.api_key}"
        response = requests.get(url)
    
        if response.status_code == 200:
            return response.json()
      

api_requests = SpoonacularInfo()
# Solicitudes API -Obtener Pizza,Pasta,Postres
# recipes = api_requests.get_recipes_by_name("pizza")
# recipes_pasta = api_requests.get_recipes_by_name("pasta")
# recipes_desserts = api_requests.get_recipes_by_name("dessert")


# Para probarlo y ver si todo va bien --Acordarse de borrarlo
"""
print("Recetas encontradas:")
for recipe in recipes["results"]:
        print(f"- {recipe['title']} ({recipe['image']})")
"""        
