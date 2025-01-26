from store.models import Product, Profile


class Cart():
    def __init__(self, request):
        self.session = request.session
        # Get request
        self.request = request
        # Acquire current session key if it exists
        cart = self.session.get('session_key')
        
        # For a new user, there's none. Create one
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # Ensure the cart is available on all site pages
        self.cart = cart

    def __len__(self):
        """
        Return the total number of items in the cart
        """
        return len(self.cart)

    def add(self, product, quantity):
        """
        Convert the product ID and qty to strings to use them
        """
        product_id = str(product.id)
        product_quantity = str(quantity)
    
        # Control logic checking if product exists within the cart
        if product_id in self.cart:
            pass
        else:
            #self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_quantity)
        # Mark the session as modified to ensure changes to the cart are saved
        self.session.modified = True
        
        # Dealing with users who're logged in
        if self.request.user.is_authenticated:
            # Get current user profile
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            # Convert the single quote string into double for JSON reasons
            cart_double = str(self.cart)
            cart_double = cart_double.replace("\'", "\"")
            # Save cart_double to the Profile model
            current_user.update(prev_cart=str(cart_double))

    def add_db(self, product, quantity)
        """
        Convert the product ID and qty to strings to use them
        """
        product_id = str(product.id)
        product_quantity = str(quantity)
    
        # Control logic checking if product exists within the cart
        if product_id in self.cart:
            pass
        else:
            #self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_quantity)
        # Mark the session as modified to ensure changes to the cart are saved
        self.session.modified = True
        
        # Dealing with users who're logged in
        if self.request.user.is_authenticated:
            # Get current user profile
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            # Convert the single quote string into double for JSON reasons
            cart_double = str(self.cart)
            cart_double = cart_double.replace("\'", "\"")
            # Save cart_double to the Profile model
            current_user.update(prev_cart=str(cart_double))

    def update(self, product, quantity):
        """
        Update the quantity of a specific product in the cart
        """
        product_id = str(product)
        product_quantity = int(quantity)
        
        # Get cart session
        mycart = self.cart
        # Make our cart/dictionary up-to-date
        mycart[product_id] = product_quantity
        # Mark the session as modified to ensure changes are saved
        self.session.modified = True

        check = self.cart
        return check

    def delete(self, product):
        """
        Delete product from the cart
        """
        product_id = str(product)
        # Remove from the cart/dictionary
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified = True

    def get_products(self):
        # Get the product ids from cart
        product_ids = self.cart.keys()
        # Use ids to check product in the db model
        products = Product.objects.filter(id__in=product_ids)
        return products

    def get_quantities(self):
        quantities = self.cart
        return quantities

    def cart_total(self):
        # Derive the product IDs
        product_ids = self.cart.keys()
        # Find products in db using the ids
        products = Product.objects.filter(id__in=product_ids)
        # Get the qties
        quantities = self.cart
        # Begin the count from 0
        total = 0
        for key, value in quantities.items():
            # Convert the string for key into int for computation
            key = int(key)
            for product in products:
                if product.id == key:
                   if product.is_on_sale:
                      total = total + (product.sale_price * value)
                   else:
                      total = total + (product.price * value)
        return total
