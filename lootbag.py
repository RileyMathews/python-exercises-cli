from uuid import uuid4
from sys import argv


class LootBag:

    def _add_child(self, name):
        new_id = uuid4()
        entry = f'{new_id},{name}\n'
        with open("children.txt", "a") as children:
            children.write(entry)
        return new_id

    def add_loot(self, toy, child):
        child_id = None
        # search for child in chidlren file
        with open('children.txt', 'r') as children:
            for line in children.readlines():
                if child in line:
                    child_id = line.split(',')[0]
        # if child wasn't found, create a new one
        if child_id == None:
            child_id = self._add_child(child)
        entry = f'{uuid4()},{toy},{child_id}\n'
        with open('toys.txt', 'a') as toys:
            toys.write(entry)

    def remove_loot(self):
        return True

    def get_children(self):
        return True

    def get_childs_loot(self):
        return True
