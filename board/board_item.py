from datetime import date, datetime
from item_status import ItemStatus


class BoardItem:
    def __init__(self, title: str, due_date: date):
        self._status = ItemStatus.OPEN
        self._event_logs = []

        self.title = title
        self.due_date = due_date

        self._log_event(f'Item created: {self.info()}')

    @property
    def status(self):
        return self._status

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value: str):
        if len(value) < 5 or len(value) > 30:
            raise ValueError('Illegal title length [5:30]')

        if not hasattr(self, '_title'):
            self._title = value
            return

        if value == self._title:
            return

        old_title = self.title
        self._title = value
        self._log_event(f'Title changed from {old_title} to {value}')

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, value: date):
        if value < date.today():
            raise ValueError("Due date can't be in the past.")

        if not hasattr(self, '_due_date'):
            self._due_date = value
            return

        if value == self._due_date:
            return

        old_due_date = self.due_date
        self._due_date = value
        self._log_event(f'DueDate changed from {old_due_date} to {value}')

    def revert_status(self):
        old_status = self.status
        self._status = ItemStatus.previous(self.status)

        if old_status == self.status:
            self._log_event(f"Can't change status, already at {self.status}")
        else:
            self._log_event(f'Status changed from {old_status} to {self.status}')

    def advance_status(self):
        old_status = self.status
        self._status = ItemStatus.next(self.status)

        if old_status == self.status:
            self._log_event(f"Can't change status, already at {self.status}")
        else:
            self._log_event(f'Status changed from {old_status} to {self.status}')

    def info(self):
        return f'{self.title}, [{self.status} | {self.due_date}]'

    def history(self):
        return '\n'.join(self._event_logs)

    def _log_event(self, description):
        self._event_logs.append(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] {description}")