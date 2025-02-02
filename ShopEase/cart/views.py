from django.shortcuts import render, get_object_or_404
from store.models import Product
from .cart import Cart
from django.contrib import messages
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
        messages.success(request, ("You've added the product to the cart"))
        return response

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # Get the sent data
        product_id = int(request.POST.get('product_id'))
        # Call delete fxn within the cart
        cart.delete(product=product_id)
        response = JsonResponse({'product':product_id})
        messages.success(request, ("Item deleted from the cart"))
        return response

def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # Get the sent data
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))
        cart.update(product=product_id, quantity=product_quantity)
        response = JsonResponse({'quantity':product_quantity})
        #return redirect('cart_summary')
        messages.success(request, ("You've updated the cart successfully"))
        return response

def cart_summary(request):
    # Acquire the cart
    cart = Cart(request)
    cart_products = cart.get_products
    quantities = cart.get_quantities
    sums = cart.cart_total()
    return render(request, "cart_summary.html", {
        "cart_products": cart_products, 
	"quantities": quantities, 
	"sums": sums
    })

