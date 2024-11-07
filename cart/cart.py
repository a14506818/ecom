class Cart():
    def __init__(self, request):
        self.session = request.session
        # get current session key
        cart = self.session.get('session_key')
        # create new key if not found
        if 'session_key' not in self.session:
            cart = self.session['session_key'] = {}
        # make sure cart is available on all pages of site
        self.cart = cart

    def add(self, product):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'Price': str(product.price)}
        self.session.modified = True