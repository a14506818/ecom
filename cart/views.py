from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_products()
    return render(request, 'cart_summary.html', {'cart_products': cart_products})

def cart_add(request):
    # get the cart
    cart = Cart(request)
    # test for POST
    if request.POST.get('action') == 'post':
        # det stuff
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        # save to session
        cart.add(product=product)
        # QTY
        cart_QTY = cart.__len__()
        # response
        response = JsonResponse({'QTY': cart_QTY})
        return response

def cart_delete(request):
    pass

def cart_update(request):
    pass
