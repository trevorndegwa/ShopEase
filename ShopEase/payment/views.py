from django.shortcuts import render, redirect
from cart.cart import Cart
from store.models import Product
from django.contrib.auth.models import User
from payment.forms import ShippingForm, PaymentForm
from payment.models import ShippingAddress, Order, OrderItem
from django.contrib import messages

def dash_shipped(request):
    if request.user.is_authenticated and request.user.is_superuser:
        orders = Order.objects.filter(shipped=True)
        return render(request, "payment/dash_shipped.html", {"orders":orders})
    else:
        messages.success(request, "Access denied!")
        return redirect('home')  
  
def dash_not_shipped(request):
    if request.user.is_authenticated and request.user.is_superuser:
        orders = Order.objects.filter(shipped=False)
        return render(request, "payment/dash_not_shipped.html", {"orders":orders})
    else:
        messages.success(request, "Access denied!")
        return redirect('home')    


def payment_successful(request):
    return render(request, "payment/payment_successful.html", {})

def order_process(request):
    if request.POST:
        cart = Cart(request)
        cart_products = cart.get_products
        quantities = cart.get_quantities
        sums = cart.cart_total()

        # Get billing stuff from prev page
        payment_form = PaymentForm(request.POST or None)
        # Get data for Shipping session
        me_shipping = request.session.get('me_shipping')
        
        full_name = me_shipping['fullname_shipping']
        email = me_shipping['email_shipping']
         
        # Use shipping info to make Shipping Address
        shipping_address = f"{me_shipping['address1_shipping']}\n{me_shipping['address2_shipping']}\n{me_shipping['city_shipping']}\n{me_shipping['county_shipping']}\n{me_shipping['postalcode_shipping']}\n{me_shipping['country_shipping']}"
        amount_paid = sums
  
        # Make an order
        if request.user.is_authenticated:
            # Logged in
            user = request.user
            # Make the order
            order_create = Order(user=user, full_name=full_name, email=email, shipping_address=shipping_address, amount_paid=amount_paid)
            order_create.save()

            # Add the order items
            # Acquire the order ID
            order_id = order_create.pk

            # Acquire the product information
            for product in cart_products():
                product_id = product.id
                if product.is_on_sale:
                    price = product.sale_price
                else:
                    price = product.price
                # Get quantity
                for key,value in quantities().items():
                    if int(key) == product.id:
                        # Create order item
                        order_item_create = OrderItem(order_id=order_id, product_id=product_id, user=user, quantity=value, price=price)
                        order_item_create.save()

            messages.success(request, "Order sent!")
            return redirect('home')

        else:
            # Not logged in but create the order
            order_create = Order(full_name=full_name, email=email, shipping_address=shipping_address, amount_paid=amount_paid)
            order_create.save()

            # Add the order items
            # Acquire the order ID
            order_id = order_create.pk

            # Acquire the product information
            for product in cart_products():
                product_id = product.id
                if product.is_on_sale:
                    price = product.sale_price
                else:
                    price = product.price
                # Get quantity
                for key,value in quantities().items():
                    if int(key) == product.id:
                        # Create order item
                        order_item_create = OrderItem(order_id=order_id, product_id=product_id, quantity=value, price=price)
                        order_item_create.save()
           
            # Clear the cart
            for key in list(request.session.keys()):
                if key == "session_key":
                    # Delete this key
                    del request.session[key] 


 
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
        # Get shipping address for the logged-in user
        try:
            shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
        except ShippingAddress.DoesNotExist:
            shipping_user = None

        # If shipping address exists, pass it as an instance to the form
        if shipping_user:
            shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        else:
            shipping_form = ShippingForm(request.POST or None)

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

