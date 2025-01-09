from django.db import models

# Create your models here.
class Item(models.Model):
    name=models.CharField(max_length=100)
    size=models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    ingredients = models.TextField()
    nutritional_value = models.TextField()
    
    def __str__(self):
        return self.name
    

class Cart(models.Model):
    items = models.ManyToManyField(Item)
    total = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    
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