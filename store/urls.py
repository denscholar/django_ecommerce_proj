from django.urls import path
from . import views

app_name = "store"


urlpatterns = [
    path("", views.home, name="products"),
    path("<slug:slug>/", views.product_detail, name="product_detail"),
    path("shop/<int:pk>/", views.show_single_category, name="category"),
]
