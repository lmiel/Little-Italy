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
    image = models.ImageField(upload_to="images/")
    ingredients = models.TextField(null=True, blank=True)
    nutritional_value = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    items = models.ManyToManyField(Item)
    total = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.id)


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
