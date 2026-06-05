from board_item import BoardItem
from datetime import date, timedelta
from item_status import ItemStatus

def add_days_to_now(d):
    return date.today() + timedelta(days=d)


item = BoardItem('Registration doesn\'t work', add_days_to_now(2))
item.advance_status()  # properly changing the status
item.advance_status()
print(item.info())  # Status: InProgress
