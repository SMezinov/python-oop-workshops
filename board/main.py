from datetime import date, timedelta
from board_items.issue import Issue
from board.read_only_board import ReadonlyBoard


def add_days_to_now(d):
    return date.today() + timedelta(days=d)

issue = Issue("Test issue", "Something is broken", add_days_to_now(2))
readonly_board = ReadonlyBoard()

readonly_board.add_item(issue)
print(readonly_board.count)

print(hasattr(readonly_board, "remove_item"))