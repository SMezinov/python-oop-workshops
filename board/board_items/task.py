from board_items.board_item import BoardItem
from datetime import date
from board_items.item_status import ItemStatus
from user.user import User


class Task(BoardItem):
    def __init__(self, title: str, assignee: User , due_date: date):
        super().__init__(title, due_date, initial_status=ItemStatus.TODO)
        self._ensure_valid_assignee(assignee)
        self._assignee = assignee

    def __str__(self):
        return self.info()

    def __repr__(self):
        return self.info()

    @property
    def assignee(self):
        return self._assignee

    @assignee.setter
    def assignee(self, value):
        self._ensure_valid_assignee(value)
        old_assignee = self._assignee
        self._assignee = value
        self._log_event(f'Assignee changed from {old_assignee} to {value}')

    def _ensure_valid_assignee(self, assignee):
        if assignee is None:
            raise ValueError('Assignee can not be empty.')

        if not isinstance(assignee, User):
            raise ValueError('Invalid assignee.')

        return assignee

    def info(self):
        board_item_info = super().info()

        return f'Task (assigned to: {self.assignee}) {board_item_info}'
