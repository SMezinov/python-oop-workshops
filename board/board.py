from datetime import date, datetime

class Board:
    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    def add_item(self, item):
        if item in self._items:
            raise ValueError('Item already in the list')
        else:
            self._items.append(item)

    @property
    def count(self):
        return f'{len(self._items)}'

class EventLog:
    def __init__(self, description: str):
        if not description:
            raise ValueError('Description should not be empty.')

        self._description =  description
        self._timestamp =  datetime.now()

    @property
    def description(self):
        return self._description

    @property
    def timestamp(self):
        return self._timestamp

    def info(self):
        return f'[{self._timestamp.strftime("%d/%m/%Y %H:%M:%S")}] {self._description}'