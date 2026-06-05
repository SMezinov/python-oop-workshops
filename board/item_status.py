class ItemStatus:

    OPEN = 'Open'
    TODO = 'Todo'
    IN_PROGRESS = 'In progress'
    DONE = 'Done'
    VERIFIED = 'Verified'

    STATUSES = [OPEN, TODO, IN_PROGRESS, DONE, VERIFIED]

    @classmethod
    def next(cls, current):
        current_index = cls.STATUSES.index(current)

        if current_index == len(cls.STATUSES) - 1:
            return cls.STATUSES[current_index]

        return cls.STATUSES[current_index + 1]

    @classmethod
    def previous(cls, current):
        current_index = cls.STATUSES.index(current)

        if current_index == 0:
            return cls.STATUSES[current_index]

        return cls.STATUSES[current_index - 1]