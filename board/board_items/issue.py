from board_items.board_item import BoardItem
from datetime import date
from board_items.item_status import ItemStatus


class Issue(BoardItem):
    def __init__(self, title: str, description: str, due_date: date):
        super().__init__(title, due_date, initial_status=ItemStatus.OPEN)
        if description is None or description.strip() == '':
            description = 'No description'
        self._description = description

    @property
    def description(self):
        return self._description

    def info(self):
        board_item_info = super().info()

        return f'Issue ({self.description}) {board_item_info}'
