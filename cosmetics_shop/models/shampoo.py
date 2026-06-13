from models.product import Product


class Shampoo(Product):
    def __init__(self, name, brand, price, gender, usage_type, milliliters):
        super().__init__(name, brand, price, gender)
        self._validate_milliliters(milliliters)

        self._usage_type = usage_type
        self._milliliters = milliliters

    @property
    def usage_type(self):
        return self._usage_type

    @property
    def milliliters(self):
        return self._milliliters

    def _validate_milliliters(self, milliliters):
        if milliliters < 0:
            raise ValueError('Milliliters cannot be negative.')

    def to_string(self):
        return '\n'.join([
            f' #{self.name} {self.brand}',
            f' #Price: ${self.price:.2f}',
            f' #Gender: {self.gender}',
            f' #Milliliters: {self.milliliters}',
            f' #Usage: {self.usage_type}',
        ])