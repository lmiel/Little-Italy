from decouple import config


import requests


class SpoonacularInfo:
    def __init__(self):
        self.api_key = "5524b40bfb124b5caf789a840299da19"  #OJO EL DECOUPLE A MI NO IBA AL MENOS PARA LA LA API KEY
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
        
    def get_recipe_details(self, recipe_id):
            """
            Realiza una solicitud a la API de Spoonacular para obtener detalles de una receta específica.

            :param recipe_id: ID de la receta
            :return: Ingredientes y calorías de la receta
            """
            url = f"{self.base_url}/recipes/{recipe_id}/information?includeNutrition=true&apiKey={self.api_key}"
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()

                # Extraer ingredientes
                ingredients = [
                    f"{ingredient['amount']} {ingredient['unit']} of {ingredient['name']}"
                    for ingredient in data.get("extendedIngredients", [])
                ]

                # Extraer calorías
                calories = next(
                    (nutrient["amount"] for nutrient in data["nutrition"]["nutrients"] if nutrient["name"] == "Calories"), 
                    "No disponible"
                )

          
                return {"ingredients": ingredients, "calories": calories}

            else:
                return {"error": f"Error {response.status_code}: {response.text}"}
  
      
"""--->PRUEBA ELIMINAR SI NO ES NECESARIO
api_requests = SpoonacularInfo()
# Solicitudes API -Obtener Pizza,Pasta,Postres
recipes = api_requests.get_recipes_by_name("pizza")
recipes_pasta = api_requests.get_recipes_by_name("pasta")
recipes_desserts = api_requests.get_recipes_by_name("dessert")
"""


