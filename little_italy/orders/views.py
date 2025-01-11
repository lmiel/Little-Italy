from django.shortcuts import render
from .scripts.spoonacular_info import SpoonacularInfo
from .models import Item
from django.shortcuts import redirect


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

#MENU
def update_menu(request):
    api = SpoonacularInfo()

    # Obtener recetas por categorías
    pizzas = api.get_recipes_by_name("pizza").get("results", [])
    pastas = api.get_recipes_by_name("pasta").get("results", [])
    desserts = api.get_recipes_by_name("dessert").get("results", [])
    # Insertar recetas en la base de datos
    for category, items in [
        ("Pizza", pizzas),
        ("Pastas", pastas),
        ("Desserts", desserts),
    ]:
        for item in items:
            Item.objects.update_or_create(
                name=item["title"],  # Campo de búsqueda
                defaults={
                    "type": category,
                    "image": item["image"],
                    # "size": item["title"],
                    # "price": item["title"],
                    # "description": item["title"],
                    # "ingredients": item["title"],
                    # "nutritional_value": item["title"],
                },
            )
    return redirect("menu")

#PEDIDOS
def view_item(request, item_id):
    item = Item.objects.get(id=item_id)
    return render(request, "orders/item.html", {"item": item})

#INFO MENU
def dish_detail_view(request, dish_id):
    """
    Vista para mostrar los detalles de un plato.
    """
    api_requests = SpoonacularInfo()
    dish_details = api_requests.get_recipe_details(dish_id)  # Obtiene ingredientes y calorías


    # Pasar los datos a la plantilla
    return render(request, "orders/dish_detail.html", {"details": dish_details})