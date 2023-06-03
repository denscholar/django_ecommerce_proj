class Cart:
    """
    A cart class, providing some ddefault behaviour that can be inherited or override as necessary
    """

    def __init__(self, request):
        self.session = request.session  # this sets the session
        cart = self.session.get("session_key")  # this retrieves the session key

        # the code below checks if the session already exists
        if "session_key" not in request.session:
            cart = self.session["session_key"] = {}
        self.cart = cart

    def add(self, product):
        """
        Adding and updating the users cart session data
        """
        product_id = product.product_id

        # if the product does not exists
        if product_id not in self.cart:
            self.cart[product_id] = {"price": str(product.price)}
            
        self.session.modified = True  # save the data in the seession
