from .cart import Cart

# Develop context processor for our cart to work on all site pages
def cart(request):
    # Return default data from the Cart
    return {'cart': Cart(request)}
