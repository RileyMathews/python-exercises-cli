import sys
import unittest

from lootbag import LootBag

sys.path.append('../')


class LootbagTest(unittest.TestCase):
    """testing class for the lootbag class"""

    def test_childrens_toys_can_be_added_to_bag(self):
        loot_bag = LootBag()
        self.assertTrue(loot_bag.add_loot())

if __name__ == '__main__':
    unittest.main()
