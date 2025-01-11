from django.urls import path
from . import views

urlpatterns = [
    path("menu/", views.menu_view, name="menu"),
    path("update_menu/", views.update_menu, name="update_menu"),
    path("dish/<int:dish_id>/", views.dish_detail_view, name="dish_detail"),
    path("cart/", views.cart_view, name="cart"),
    path("cart/add/<int:dish_id>/", views.add_to_cart, name="add_to_cart"),
    path("cart/remove/<int:dish_id>/", views.remove_from_cart, name="remove_from_cart"),
]
