from django.shortcuts import render

from store.models import Product



def dashboard(request):
    context = {}
    return render(request, 'pages/dashboard.html', context)


def profile(request):
    return render(request, 'pages/profile.html')


def product(request):
    user = request.user
    user_products = Product.objects.filter(user=user)
    context = {
        "user_products": user_products
    }
    return render(request, 'pages/profile.html', context)
    
