
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
    product_id = str(product.id)
    
    # Control logic
    if product_id in self.cart:
        pass
    else:
        self.cart[product_id] = {'price': str(product.price)}

    self.session.modified = True
