from .models import Cart, CartItem


def cart_item_count(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        item_count = CartItem.objects.filter(cart=cart).count()
    else:
        item_count = 0  
    return {"item_count": item_count}
