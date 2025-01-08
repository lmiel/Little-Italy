
from django.shortcuts import render
from .scripts.spoonacular_info import SpoonacularInfo

def menu_view(request):
    api = SpoonacularInfo()
    
    # Obtener recetas por categorías
    pizzas = api.get_recipes_by_name("pizza").get("results", [])
    pastas = api.get_recipes_by_name("pasta").get("results", [])
    desserts = api.get_recipes_by_name("dessert").get("results", [])
    
    # Estructura las recetas
    categories = {
        "Pizzas": [{"title": item["title"], "image": item["image"], "id": item["id"]} for item in pizzas],
        "Pastas": [{"title": item["title"], "image": item["image"], "id": item["id"]} for item in pastas],
        "Postres": [{"title": item["title"], "image": item["image"], "id": item["id"]} for item in desserts],
    }
    
    # menu.html
    return render(request, "orders/menu.html", {"categories": categories})