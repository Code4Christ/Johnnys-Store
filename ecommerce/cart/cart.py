
from decimal import Decimal

from store.models import Product

class Cart():
    
    def __init__(self, request):
        
        # Create session
        self.session = request.session 
        
        # Returning user - obtain his/her existing session
        cart = self.session.get('session_key')

        # New user - generate a new sessions
        if 'session_key' not in request.session:
            
            cart = self.session['session_key'] = {}

        self.cart = cart

    def add(self, product, product_qty):
        
        product_id = str(product.id)
        
        # if product is already in the cart
        if product_id in self.cart:
            # then we can update quantity if needed
            self.cart[product_id]['qty'] = product_qty
        
        # if product doesnt exist
        else:
            # we are taking the products price, and quantity of items selected
            # we are assisgning all of this to the product ID 
            self.cart[product_id] = {'price': str(product.price), 'qty': product_qty}
            
        self.session.modified = True # tell Django you have modified the session.
     
    def delete(self, product):

        product_id = str(product)

        if product_id in self.cart:

            del self.cart[product_id]

        self.session.modified = True



    def update(self, product, qty):

        product_id = str(product)
        product_quantity = qty

        if product_id in self.cart:

            self.cart[product_id]['qty'] = product_quantity

        self.session.modified = True   
        
    def __len__(self):
        return sum(item['qty'] for item in self.cart.values())
        
    # For shopping cart functionality
    def __iter__(self):

        all_product_ids = self.cart.keys()

        products = Product.objects.filter(id__in=all_product_ids)

        cart = self.cart.copy()
        
        # for every product in products dictionary 
        for product in products:
            # pull the product ID and assign it to the product
            cart[str(product.id)]['product'] = product

        # for every item in the actual cart
        for item in cart.values():
            # assign the corrisponding price for each item
            item['price'] = Decimal(item['price'])
            # assign total for each item
            # total = price * quantity
            item['total'] = item['price'] * item['qty']

            yield item  # return item total 
            
    # display totals in carts        
    def get_total(self):   
        # return the sum of all products multiplied by the corresponding quantity. Do so in decimal form 
        
            return sum(Decimal(item['price']) * (item['qty']) for item in self.cart.values())
        













