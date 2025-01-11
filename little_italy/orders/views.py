from django.shortcuts import render
from .scripts.spoonacular_info import SpoonacularInfo
from .models import Item
from django.shortcuts import redirect
from .scripts.edamam_info import EdamamInfo
import random
import json
from .models import Cart
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


def menu_view(request):
    items = Item.objects.all()
    categories = {}
    for item in items:
        if item.type not in categories:
            categories[item.type] = []
        categories[item.type].append(item)
    return render(request, "orders/menu.html", {"categories": categories})


# MENU
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
                    "spoonacular_id": item["id"],
                },
            )
    return redirect("menu")


# INFO MENU
def dish_detail_view(request, dish_id):
    item = Item.objects.get(spoonacular_id=dish_id)
    if item.ingredients:
        print(item.nutritional_value.items())
        return render(request, "orders/dish_detail.html", {"item": item})
    spoonacular_api = SpoonacularInfo()
    dish_details = spoonacular_api.get_recipe_details(
        dish_id
    )  # Obtiene ingredientes y calorías
    item.ingredients = dish_details["ingredients"]
    item.description = dish_details["summary"]
    edamam_api = EdamamInfo()
    nutritional_value = edamam_api.get_nutrition_details(item.name, item.ingredients)
    item.nutritional_value = json.dumps(nutritional_value)
    item.nutritional_value = nutritional_value
    price_ranges = {
        "Pizza": (15.0, 25.0),
        "Pastas": (10.0, 25.0),
        "Desserts": (5.0, 10.0),
    }
    item.price = round(random.uniform(*price_ranges.get(item.type, (0.0, 0.0))), 1)
    item.save()

    # Pasar los datos a la plantilla
    return render(request, "orders/dish_detail.html", {"item": item})


# CART
@csrf_exempt
@login_required
def add_to_cart(request, dish_id):
    print("Adding to cart")
    item = Item.objects.get(spoonacular_id=dish_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart.items.add(item)
    cart.total += item.price
    cart.save()
    return redirect("menu")


@login_required
def remove_from_cart(request, dish_id):
    item = Item.objects.get(spoonacular_id=dish_id)
    cart = Cart.objects.get(user=request.user)
    if item in cart.items.all():
        cart.items.remove(item)
        cart.total -= item.price
        cart.save()
    return redirect("cart")


@login_required
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.all()
    return render(
        request,
        "orders/cart.html",
        {"cart_items": cart_items, "total_price": cart.total},
    )
