from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('cart/', home, name='cart'),
    path('products/', home, name='products'),
    path('login/', home, name='login'),

    
]