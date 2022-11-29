from decimal import Decimal

from Store.models import Watch

class Cart():
    """
    A base cart class that provides some default behaviours 
    that can be inherited or overriden as necessary
    """

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('skey')
        if 'skey' not in request.session:
            cart = self.session['skey'] = {}
        self.cart = cart


    def add(self, watch, qty):
        '''
        Adding and updating the user's cart using session data.
        '''
        watch_id = str(watch.id)

        if watch_id not in self.cart:
            self.cart[watch_id] = {'price' : str(watch.price), 'qty': int(qty)}
        self.session.modified = True