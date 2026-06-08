class ShoppingCart:
    def __init__(self):
        self._products = []

    @property
    def products(self):
        return tuple(self._products)

    def add_product(self, product):
        self._products.append(product)

    def remove_product(self, product):
        if product in self._products:
            self._products.remove(product)

    def contains_product(self, product):
        return product in self._products

    def total_price(self):
        total = 0

        for product in self._products:
            total += product.price

        return total
