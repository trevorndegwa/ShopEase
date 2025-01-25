from store.models import Product


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

    def __len__(self):
        # Return the total number of items in the cart
        return len(self.cart)

    def add(self, product, quantity):
        # Convert the product ID and qty to strings to use them
        product_id = str(product.id)
        product_quantity = str(quantity)
    
        # Control logic checking if product exists within the cart
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_quantity)
        # Mark the session as modified to ensure changes to the cart are saved
        self.session.modified = True

    def get_products(self):
        # Get the product ids from cart
        product_ids = self.cart.keys()
        # Use ids to check product in the db model
        products = Product.objects.filter(id__in=product_ids)
        return products
