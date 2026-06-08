class Category:
    def __init__(self, name):
        self.name = name
        self._products = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value is None:
            raise ValueError("Category name cannot be None.")

        if not 2 <= len(value) <= 15:
            raise ValueError('Minimum category name’s length is 2 symbols and maximum is 15 symbols.')

        self._name = value

    @property
    def products(self):
        return tuple(self._products)

    def add_product(self, product):
        if product in self._products:
            raise ValueError('Product already exists in this category.')

        self._products.append(product)

    def remove_product(self, product):
        if product not in self._products:
            raise ValueError('This product is not in Product list.')

        self._products.remove(product)

    def to_string(self):
        result = f'#Category: {self.name}'

        if len(self._products) == 0:
            result += '\n #No products in this category'
            return result

        for i in range(len(self._products)):
            current_product = self._products[i]
            result += '\n' + current_product.to_string()

            if i < len(self._products) - 1:
                result += '\n ==='

        return result