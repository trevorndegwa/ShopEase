from django.shortcuts import render, get_object_or_404
from store.models import Product
from .cart import Cart
from django.http import JsonResponse

def cart_add(request):
    # Acquire the cart
    cart = Cart(request)
    # test if POST-ing
    if request.POST.get('action') == 'post':
        # Get the sent data
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))
        # Find the product in the database
        product = get_object_or_404(Product, id=product_id)
        # Save to the session
        cart.add(product=product, quantity=product_quantity)
        # Get number of items in cart
        cart_number = cart.__len__()
        # Return the response
        response = JsonResponse({'num': cart_number})
        return response

def cart_delete(request):
    pass

def cart_update(request):
    pass

def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_products
    return render(request, "cart_summary.html", {"cart_products": cart_products})

