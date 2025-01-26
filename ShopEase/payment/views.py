from django.shortcuts import render
from cart.cart import Cart

def payment_successful(request):
    return render(request, "payment/payment_successful.html", {})

def checkout(request):
    # Acquire the cart
    cart = Cart(request)
    cart_products = cart.get_products
    quantities = cart.get_quantities
    sums = cart.cart_total()
    return render(request, "payment/checkout.html", {
        "cart_products": cart_products, 
	"quantities": quantities, 
	"sums": sums
    })
