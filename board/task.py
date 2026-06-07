from board_item import BoardItem
from datetime import date
from item_status import ItemStatus


class Task(BoardItem):
    def __init__(self, title: str, assignee: str, due_date: date):
        super().__init__(title, due_date, initial_status=ItemStatus.TODO)
        self._ensure_valid_assignee(assignee)
        self._assignee = assignee

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
        if assignee is None or assignee.strip() == '':
            raise ValueError('Illegal assignee. It must be minimum one symbol.')

        if (len(assignee) < 5 or len(assignee) > 30):
            raise ValueError('Illegal assignee length [5:30]')