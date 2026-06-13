from board_items.item_status import ItemStatus


class User:
    def __init__(self, username: str, email: str):
        self._username = self._ensure_valid_username(username)
        self.email = email
        self._assigned_tasks = []

    def __str__(self):
        return self.username

    @property
    def username(self):
        return self._username

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if value is None:
            raise ValueError('Email can not be empty.')
        if '@' not in value:
            raise ValueError('Email should contain the symbol @')

        self._email = value

    @property
    def assigned_tasks(self):
        return tuple(self._assigned_tasks)

    @property
    def capacity(self):
        return 3 - self._active_tasks_count()

    def _active_tasks_count(self):
        counter = 0

        for task in self._assigned_tasks:
            if task.status == ItemStatus.TODO or task.status == ItemStatus.IN_PROGRESS:
                counter += 1

        return counter

    def has_capacity(self):
        if self.capacity <= 0:
            return False
        return True

    def _ensure_valid_username(self, username):
        if username is None or username.strip() == '':
            raise ValueError('Username can not be empty!')
        return username.strip()

    def receive_task(self, task):
        if not self.has_capacity():
            raise ValueError("User does not have capacity")

        task.assignee = self
        self._assigned_tasks.append(task)

    def remove_task(self, task):
        if task not in self._assigned_tasks:
            raise ValueError('Task not found.')
        self._assigned_tasks.remove(task)

    def advance_task_status(self, task):
        if task.assignee is not self:
            raise ValueError("Task is not assigned to this user")

        if task.status not in (ItemStatus.TODO, ItemStatus.IN_PROGRESS):
            raise ValueError("Task status can not be advanced")

        task.advance_status()