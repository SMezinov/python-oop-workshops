from board_items.item_status import ItemStatus
from user.user import User

class Board:
    def __init__(self):
        self._items = []
        self._users = []

    def add_user(self, username, email):
        for new_user in self._users:
            if username.strip() == new_user.username:
                raise ValueError('This user already exist.')

        user = User(username, email)
        self._users.append(user)

        return user

    def reassign_task(self, task, new_assignee):
        if task not in self._items:
            raise ValueError('The task not exist.')
        if task.assignee is new_assignee:
            raise ValueError('Assignee must be not the same.')

        current_assignee = task.assignee
        if new_assignee.capacity > 0:
            current_assignee.remove_task(task)
        else:
            raise ValueError('This User not have more capacity.')

        while task.status is not ItemStatus.TODO:
            task.revert_status()

        new_assignee.receive_task(task)

    def _team_capacity(self):
        team_capacity = 0
        for user in self._users:
            team_capacity += user.capacity

        return team_capacity

    @property
    def count(self):
        return len(self._items)

    @property
    def team_capacity(self):
        return self._team_capacity()