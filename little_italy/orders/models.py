from django.db import models
from authentication.models import User


# Create your models here.
class Item(models.Model):
    spoonacular_id = models.IntegerField(null=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, null=True)
    size = models.CharField(max_length=100, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    description = models.TextField(null=True)
    image = models.URLField(max_length=200, null=True, blank=True)
    ingredients = models.TextField(null=True, blank=True)
    nutritional_value = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    total = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    items = models.ManyToManyField(
        Item, through="CartItem"
    )  # Usamos el modelo intermedio

    def __str__(self):
        return f"Cart {self.id} for {self.user}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)  # Guardar la cantidad del item

    def __str__(self):
        return f"{self.quantity} of {self.item.name} in cart {self.cart.id}"


class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    total = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
