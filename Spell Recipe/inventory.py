class Inventory:

    def __init__(self):
        self._items = []

    # TODO: Implement add method to add item to the inventory
    def add(self, item) -> None:
        return self._items.append(item)

    # TODO: Implement remove method to remove item from the inventory
    def remove(self, item) -> None:
        return self._items.remove(item)

    # TODO: Implement count method to count occurrences of an item in the inventory
    def count(self, item) -> int:
        return len(self._items)

    # TODO: Implement find_by_type method to find items by their class name
    def find_by_type(self, type_name: str) -> list:
        pass
