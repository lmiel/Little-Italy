from django.urls import path
from . import views

urlpatterns = [
    path("menu/", views.menu_view, name="menu"),
    path("update_menu/", views.update_menu, name="update_menu"),
    path("menu/<int:item_id>/", views.view_item, name="menu_item"),
]
