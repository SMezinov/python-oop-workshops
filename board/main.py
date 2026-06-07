from datetime import date, timedelta
from board import Board
from board_item import BoardItem
from event_log import EventLog
from task import Task
from issue import Issue


def add_days_to_now(d):
    return date.today() + timedelta(days=d)

issue = Issue('App flow tests?', 'We need to test the flow!', add_days_to_now(1))
issue.advance_status()
issue.due_date += timedelta(days = 1)
print(issue.history())