from django.shortcuts import render, redirect
from cart.cart import Cart
from payment.forms import ShippingForm, PaymentForm
from payment.models import ShippingAddress
from django.contrib import messages

def payment_successful(request):
    return render(request, "payment/payment_successful.html", {})

def order_process(request):
    if request.POST:
        # Get billing stuff from prev page
        payment_form = PaymentForm(request.POST or None)
        # Get data for Shipping session
        me_shipping = request.session.get('me_shipping')
        
        # Use shipping info to make Shipping Address
        shipping_address = f"{me_shipping['address1_shipping']}\n{me_shipping['address2_shipping']}\n{me_shipping['city_shipping']}\n{me_shipping['county_shipping']}\n{me_shipping['postalcode_shipping']}\n{me_shipping['country_shipping']}"
        print(shipping_address)



        messages.success(request, "Order sent!")
        return redirect('home')

    else:
        messages.success(request, "Access denied!")
        return redirect('home')

def billing_info(request):
    if request.POST:
        # Acquire the cart
        cart = Cart(request)
        cart_products = cart.get_products
        quantities = cart.get_quantities
        sums = cart.cart_total()

        # Create a sesh with Shipping information
        me_shipping = request.POST
        request.session['me_shipping'] = me_shipping

        # Check is the user is logged in
        if request.user.is_authenticated:
            # Get billing form
            billing_form = PaymentForm() 
            return render(request, "payment/billing_info.html", {
                "cart_products": cart_products, 
                "quantities": quantities, 
                "sums": sums,
                "shipping_info": request.POST,
                "billing_form": billing_form
            })

        else:
            billing_form = PaymentForm()
            return render(request, "payment/billing_info.html", {
                "cart_products": cart_products, 
                "quantities": quantities, 
                "sums": sums,
                "shipping_info": request.POST,
                "billing_form": billing_form
            })
             
        shipping_form = request.POST
        return render(request, "payment/billing_info.html", {
                "cart_products": cart_products, 
                "quantities": quantities, 
                "sums": sums,
                "shipping_form": shipping_form
        })
    else:
        messages.success(request, "Access denied!")
        return redirect('home')

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
