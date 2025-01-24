
class Cart():
    def __init__(self, request):
        self.session = request.session
        # Acquire current session key if it exists
        cart = self.session.get('session_key')
        
        # For a new user, there's none. Create one
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # Ensure the cart is available on all site pages
        self.cart = cart

def add(self, product):
    # Convert the product ID to a string to use it as a key in the cart dictionary
    product_id = str(product.id)
    
    # Control logic checking if product exists within the cart
    if product_id in self.cart:
        pass
    else:
        self.cart[product_id] = {'price': str(product.price)}
    # Mark the session as modified to ensure changes to the cart are saved
    self.session.modified = True
