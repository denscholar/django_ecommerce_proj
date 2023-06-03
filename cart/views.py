from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
import json

from cart.cart import Cart
from store.models import Product


def cart_detail(request):

    return render(request, "cart/cart_detail_page.html", {})


# def add_to_cart(request):
#     pass
    # data = json.loads(request.body)
    # print(data)
    # productId = data["productId"]
    # action = data["action"]
    # print(action, productId)
    # user = request.user
    # product = Product.objects.get(slug=productId)

    # cart = Cart.objects.get(user=user)  # associate the user with the cart
    # cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    # if action == "add":
    #     cart_item.quantity += 1
    # elif action == "remove":
    #     cart_item.quantity -= 1
    #     if cart_item.quantity <= 0:
    #         cart_item.delete()
    # elif action == "delete":
    #     cart_item.delete()

    # cart_item.save()
    
    # # Create a dictionary containing the data you want to send in the response
    # response_data = {
    #     "productId": productId,
    # }

    # return JsonResponse(response_data)

def add_to_cart(request):
    cart = Cart(request)
        
    if request.POST.get('action') == 'add':
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, product_id=product_id)
        cart.add(product=product)
        response = JsonResponse({'test': "this is a test data"})
        return response
    return JsonResponse({'message': 'invalid data'})