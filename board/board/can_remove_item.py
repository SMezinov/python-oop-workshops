from board_items.board_item import BoardItem


class CanRemoveItem:
    def remove_item(self, item: BoardItem):
        if item not in self._items:
            raise ValueError('BoardItem not in the list.')

        self._items.remove(item)
