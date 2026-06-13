from core.application_data import ApplicationData
from models.gender import Gender
from commands.validation_helpers import validate_params_count, try_parse_float


class CreateToothpasteCommand:

    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 5)
        self._params = params
        self._app_data = app_data

    def execute(self):
        toothpaste_name = self._params[0]
        brand = self._params[1]
        price = try_parse_float(self._params[2])
        gender = Gender.from_string(self._params[3])
        ingredients = tuple(self._params[4].split(','))

        if self._app_data.product_exists(toothpaste_name):
            raise ValueError(f'Product with name {toothpaste_name} already exists!')

        self._app_data.create_toothpaste(toothpaste_name, brand, price, gender, ingredients)

        return f'Toothpaste with name {toothpaste_name} was created!'