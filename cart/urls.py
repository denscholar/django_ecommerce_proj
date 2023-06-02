from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("cart_items/", views.cart_detail, name="cart"),
    path('add_product/', views.add_to_cart, name='add_to_cart'),
]
