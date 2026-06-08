from models.category import Category
from models.product import Product
from models.shopping_cart import ShoppingCart

class ApplicationData:
    def __init__(self):
        self._products = []
        self._categories = []
        self._shopping_cart = ShoppingCart()

    @property
    def products(self):
        return tuple(self._products)

    @property
    def categories(self):
        return tuple(self._categories)

    @property
    def shopping_cart(self) -> ShoppingCart:
        return self._shopping_cart

    def find_product_by_name(self, name) -> Product:
        for product in self._products:
            if product.name == name:
                return product

        raise ValueError('Product not found.')

    def find_category_by_name(self, name) -> Category:
        for category in self._categories:
            if category.name == name:
                return category

        raise ValueError('Category not found.')

    def create_category(self, name) -> None:
        if self.category_exists(name):
            raise ValueError('Category already exists.')

        new_cat = Category(name)
        self._categories.append(new_cat)

    def create_product(self, name, brand, price, gender) -> None:
        if self.product_exists(name):
            raise ValueError('Product already exists.')

        new_prod = Product(name, brand, price, gender)
        self._products.append(new_prod)

    def category_exists(self, name) -> bool:
        for category in self._categories:
            if category.name == name:
                return True

        return False

    def product_exists(self, name) -> bool:
        for product in self._products:
            if product.name == name:
                return True

        return False