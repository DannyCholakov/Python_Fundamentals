class Inventory:
    def __init__(self, capacity: int):
        self.__capacity = capacity  # Private attribute for capacity
        self.items = []  # List to store items

    def add_item(self, item: str):
        if len(self.items) < self.__capacity:
            self.items.append(item)
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        items_list = ", ".join(self.items)  # Join items with ', '
        left_capacity = self.__capacity - len(self.items)
        return f"Items: {items_list}.\nCapacity left: {left_capacity}"
