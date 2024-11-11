from store.models import Product

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

    def add(self, product, product_QTY:int):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'QTY': product_QTY}
        else:
            self.cart[product_id]['QTY'] += product_QTY
        self.session.modified = True

    def __len__(self):
        return len(self.cart)

    def get_products(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        return products
    
    def get_products_item(self):
        return self.cart
    
    def update_product_QTY(self, product, operation):
        product_id = str(product.id)
        if operation == '+': self.cart[product_id]['QTY'] += 1
        if operation == '-' and self.cart[product_id]['QTY'] > 0: self.cart[product_id]['QTY'] -= 1
        self.session.modified = True
        return self.cart[product_id]['QTY']