import unittest


class LootbagTest(unittest.TestCase):
    """testing class for the lootbag class"""

    def test_childrens_toys_can_be_added_to_bag(self):
        loot_bag = Bag()
        loot_bag.add_toy_for_child("Billy", "xbox")
