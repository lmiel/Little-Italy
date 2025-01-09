from django.shortcuts import render
from .scripts.spoonacular_info import SpoonacularInfo
from .models import Item
from django.shortcuts import redirect


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
    categories = {}
    for item in items:
        if item.type not in categories:
            categories[item.type] = []
        categories[item.type].append(item)
    return render(request, "orders/menu.html", {"categories": categories})


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


def view_item(request, item_id):
    item = Item.objects.get(id=item_id)
    return render(request, "orders/item.html", {"item": item})
