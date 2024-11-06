from .cart import Cart

# make cart works on all site
def cart(request):
    return {'cart': Cart(request)}