from django.shortcuts import render
from .scripts.spoonacular_info import SpoonacularInfo
from .models import Item
from .forms import CheckoutForm
from django.shortcuts import redirect
from .scripts.edamam_info import EdamamInfo
import random
import json
from .models import Cart, CartItem
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from decimal import Decimal


def menu_view(request):
    items = Item.objects.all()
    categories = {"Pizza": [], "Pastas": [], "Desserts": []}
    for item in items:
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
    print("Adding to cart" + str(dish_id))
    item = Item.objects.get(spoonacular_id=dish_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    cart.total += Decimal(item.price)
    cart.save()
    return redirect("menu")


@login_required
def remove_from_cart(request, dish_id):
    item = Item.objects.get(spoonacular_id=dish_id)
    cart = Cart.objects.get(user=request.user)
    cart_item = CartItem.objects.get(cart=cart, item=item)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    cart.total -= Decimal(item.price)
    cart.save()

    return redirect("cart")


@login_required
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    return render(
        request,
        "orders/cart.html",
        {"cart_items": cart_items, "total_price": cart.total},
    )


@login_required
def checkout_view(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Aquí puedes simular el "procesamiento" del pago
            # Y redirigir a una página de éxito de pago
            # En un caso real, aquí harías la lógica de pago

            # Guardar la orden en la base de datos si lo deseas (aunque sea ficticia)
            order = form.save(commit=False)
            order.save()

            # Redirigir a una página de éxito (simulada)
            return redirect("payment_success")  # Asegúrate de crear esta vista

    else:
        form = CheckoutForm()

    return render(
        request,
        "orders/checkout.html",
        {"form": form, "cart_items": cart_items, "total_price": cart.total},
    )
