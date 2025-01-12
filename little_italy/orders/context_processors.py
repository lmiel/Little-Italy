from .models import Cart, CartItem


def cart_item_count(request):
    if request.user.is_authenticated:
        # Obtener el carrito del usuario
        cart, created = Cart.objects.get_or_create(user=request.user)
        # Contar los items en el carrito
        item_count = CartItem.objects.filter(cart=cart).count()
    else:
        item_count = 0  # Si no está autenticado, el contador será 0
    return {"item_count": item_count}
