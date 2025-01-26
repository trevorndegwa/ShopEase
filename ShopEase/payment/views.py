from django.shortcuts import render
from cart.cart import Cart
from payment.forms import ShippingForm
from payment.models import ShippingAddress

def payment_successful(request):
    return render(request, "payment/payment_successful.html", {})

def checkout(request):
    # Acquire the cart
    cart = Cart(request)
    cart_products = cart.get_products
    quantities = cart.get_quantities
    sums = cart.cart_total()
    
    if request.user.is_authenticated:
        # Checkout as a logged in user
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        return render(request, "payment/checkout.html", {
            "cart_products": cart_products, 
	    "quantities": quantities, 
	    "sums": sums,
            "shipping_form": shipping_form
        })
    else:
        # Checkout as a guest
        shipping_form = ShippingForm(request.POST or None)
        return render(request, "payment/checkout.html", {
            "cart_products": cart_products, 
	    "quantities": quantities, 
	    "sums": sums,
            "shipping_form": shipping_form
    })
