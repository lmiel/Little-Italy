
from django.shortcuts import render
from .scripts.spoonacular_info import SpoonacularInfo
from models import Item

def menu_view(request):
    # api = SpoonacularInfo()
    
    # # Obtener recetas por categorías
    # pizzas = api.get_recipes_by_name("pizza").get("results", [])
    # pastas = api.get_recipes_by_name("pasta").get("results", [])
    # desserts = api.get_recipes_by_name("dessert").get("results", [])
    
    # # Estructura las recetas
    # categories = {
    #     "Pizzas": [{"title": item["title"], "image": item["image"], "id": item["id"]} for item in pizzas],
    #     "Pastas": [{"title": item["title"], "image": item["image"], "id": item["id"]} for item in pastas],
    #     "Postres": [{"title": item["title"], "image": item["image"], "id": item["id"]} for item in desserts],
    # }
    
    # # menu.html
    # return render(request, "orders/menu.html", {"categories": categories})
    # Obtener todos los items de la base de datos
    items = Item.objects.all()
    return render(request, "orders/menu.html", {"items": items})

def update_menu(request):
    api = SpoonacularInfo()
    
    # Obtener recetas por categorías
    pizzas = api.get_recipes_by_name("pizza").get("results", [])
    pastas = api.get_recipes_by_name("pasta").get("results", [])
    desserts = api.get_recipes_by_name("dessert").get("results", [])
    
    # Insertar recetas en la base de datos
    for item in pizzas+pastas+desserts:
        data = {
            "name":item["title"],
            # "size":item["title"],
            # "price":item["title"],
            "description":item["title"],
            "image":item["title"],
            "ingredients":item["title"],
            "nutritional_value":item["title"],
        }
        Item.objects.update_or_create(data)