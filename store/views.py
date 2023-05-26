from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def home(request):
    all_products = Product.products.all()
    context = {"all_products": all_products}
    return render(request, "store/home.html", context)


def show_single_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    products = Product.objects.filter(category=category)
    context = {
        "category": category,
        "products": products,
    }
    return render(request, "store/category.html", context)


def product_detail(request, slug):
    prod_detail = get_object_or_404(Product, slug=slug, in_stock=True)
    context = {"prod_detail": prod_detail}
    return render(request, "store/product_detail.html", context)
