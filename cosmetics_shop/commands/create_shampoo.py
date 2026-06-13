from core.application_data import ApplicationData
from models.gender import Gender
from commands.validation_helpers import try_parse_int, validate_params_count, try_parse_float
from models.usage_type import UsageType


class CreateShampooCommand:

    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 6)
        self._params = params
        self._app_data = app_data

    def execute(self):
        shampoo_name = self._params[0]
        brand = self._params[1]
        price = try_parse_float(self._params[2])
        gender = Gender.from_string(self._params[3])
        milliliters = try_parse_int(self._params[4])
        usage_type = UsageType.from_string(self._params[5])

        if self._app_data.product_exists(shampoo_name):
            raise ValueError(f'Product with name {shampoo_name} already exists!')

        self._app_data.create_shampoo(shampoo_name, brand, price, gender, usage_type, milliliters)

        return f'Shampoo with name {shampoo_name} was created!'