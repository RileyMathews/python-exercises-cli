from uuid import uuid4
from sys import argv


class LootBag:

    def _add_child(self, name):
        entry = f'{uuid4()},{name}'
        with open("children.txt", "a") as children:
            children.write(entry)

    def add_loot(self, toy, child):
        return True

    def remove_loot(self):
        return True

    def get_children(self):
        return True

    def get_childs_loot(self):
        return True
