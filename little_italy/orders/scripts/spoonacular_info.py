from decouple import config


import requests


class SpoonacularInfo:
    def __init__(self):
        self.api_key = config("SPOONACULAR_API_KEY2")
        self.base_url = "https://api.spoonacular.com"

    def get_recipes_by_name(self, name):
        """
        Realiza una solicitud a la API de Spoonacular para buscar recetas por nombre.

        :param name: Nombre de la receta (ejemplo: "pizza")
        :return: Respuesta de la API en formato JSON
        """
        url = (
            f"{self.base_url}/recipes/complexSearch?query={name}&apiKey={self.api_key}"
        )
        response = requests.get(url)

        if response.status_code == 200:
            with open("recipes.json", "w") as file:
                file.write(response.text)
            return response.json()

