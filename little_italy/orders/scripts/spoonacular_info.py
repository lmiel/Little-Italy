from decouple import config


import requests


class SpoonacularInfo:
    def __init__(self):
        self.api_key = config("SPOONACULAR_API_KEY2")
        self.base_url = "https://api.spoonacular.com"

    def get_recipes_by_name(self, name):
        url = (
            f"{self.base_url}/recipes/complexSearch?query={name}&apiKey={self.api_key}"
        )
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()

    def get_recipe_details(self, recipe_id):
        url = f"{self.base_url}/recipes/{recipe_id}/information?&apiKey={self.api_key}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            # Extraer ingredientes
            ingredients = [
                f"{ingredient['original']}"  # {ingredient['unit']} of {ingredient['name']}
                for ingredient in data.get("extendedIngredients", [])
            ]

            summary = data.get("summary", "")
            return {"ingredients": ingredients, "summary": summary}

        else:
            return {"error": f"Error {response.status_code}: {response.text}"}


"""--->PRUEBA ELIMINAR SI NO ES NECESARIO
api_requests = SpoonacularInfo()
# Solicitudes API -Obtener Pizza,Pasta,Postres
recipes = api_requests.get_recipes_by_name("pizza")
recipes_pasta = api_requests.get_recipes_by_name("pasta")
recipes_desserts = api_requests.get_recipes_by_name("dessert")
"""
