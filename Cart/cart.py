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

        # if watch_id not in self.cart:
        #     self.cart[watch_id] = {'price' : str(watch.price), 'qty': int(qty)}
        # self.session.modified = True

        if watch_id in self.cart:
            self.cart[watch_id]['qty'] = qty
        else:
            self.cart[watch_id] = {'price': str(watch.price), 'qty': qty}

        self.save()


    def __iter__(self):
        """
        Collects the watch_id values from the session data then queries the database and
        returns the watches

        """
        watch_ids = self.cart.keys()

        watches = Watch.watch.filter(id__in=watch_ids)

        cart = self.cart.copy()

        for watch in watches:
            cart[str(watch.id)]['watch'] = watch

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item


    def __len__(self):
        '''
        Gets cart data and returns the length of the items
        '''
        return sum(item['qty'] for item in self.cart.values())

    def save(self):
        '''
        Save cart data to the session data
        '''
        self.session.modified = True


















