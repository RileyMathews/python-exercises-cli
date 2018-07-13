import sys
import unittest
sys.path.append('../')
from lootbag import LootBag


class LootbagTest(unittest.TestCase):
    """testing class for the lootbag class"""

    @classmethod
    def setUpClass(self):
        self.bag = LootBag()

    def test_can_create_instance_of_LootBag(self):
        bag = LootBag()
        self.assertIsInstance(bag, LootBag)

    def test_childrens_toys_can_be_added_to_bag(self):
        self.assertTrue(self.bag.add_loot())

    def test_children_can_be_added_to_bag(self):
        self.bag._add_child("susie")
        with open("../children.txt", "r") as children:
            self.assertEqual("susie", children.readline())

    def test_childrens_toys_can_be_removed_from_bag(self):
        self.assertTrue(self.bag.remove_loot())

    def test_can_get_list_of_children(self):
        self.assertTrue(self.bag.get_children())

    def test_can_get_list_of_childs_loot(self):
        self.assertTrue(self.bag.get_childs_loot())

if __name__ == '__main__':
    unittest.main()
