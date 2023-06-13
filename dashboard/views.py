from django.shortcuts import render, redirect
from .forms import ProductForm
from store.models import Product


def dashboard(request):
    context = {}
    return render(request, "pages/dashboard.html", context)


def profile(request):
    user = request.user
    user_products = Product.objects.filter(created_by=user)
    context = {"user_products": user_products}
    return render(request, "pages/profile.html", context)


def create_product(request):
    if request.method == "POST":
        
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()
            return redirect("dashboard:profile")

    else:
        form = ProductForm()

    context = {"form": form}

    return render(request, "pages/add-product.html", context)
