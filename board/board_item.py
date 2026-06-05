from datetime import date
from item_status import ItemStatus

class BoardItem:
    def __init__(self, title:str, due_date:date):

        if not 5 <= len(title.strip()) <= 30:
            raise ValueError('Title length should be longer than 5 and not bigger than 30 characters.')
        if due_date <= date.today():
            raise ValueError('Due date should be in the future.')

        self.title = title.strip()      #what item is about
        self.due_date = due_date        # when it should be done
        self._status = ItemStatus.OPEN   #describes the state of this item - being worked on, being completed, etc..

    @property
    def status(self):
        return self._status
    
    def advance_status(self):
        self._status = ItemStatus.next(self.status)

    def revert_status(self):
        self._status = ItemStatus.previous(self.status)

    def info(self):
        return f'{self.title}, [{self.status} | {self.due_date}]'