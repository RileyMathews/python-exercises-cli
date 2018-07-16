import sys
import unittest
sys.path.append('../')
from lootbag import LootBag


class LootbagTest(unittest.TestCase):
    """testing class for the lootbag class"""

    @classmethod
    def setUpClass(self):
        self.bag = LootBag()

    def clean_up_files(self, file_name, item):
        """method to clean up files modified after testing

        Arguments:
            file_name {string} -- file to be cleaned
            item {string} -- item to be removed from file
        """
        with open(file_name, 'r+') as target_file:
            t = target_file.read()
            target_file.seek(0)
            for line in t.split('\n'):
                if line.split(',')[1] != item:
                    target_file.write(line + '\n')
            target_file.truncate()

    def test_can_create_instance_of_LootBag(self):
        test_bag = LootBag()
        self.assertIsInstance(test_bag, LootBag)

    def test_childrens_toys_can_be_added_to_bag(self):
        self.bag.add_loot("test_toy", "test_child")
        with open('children.txt', 'r+') as children:
            self.assertTrue("test_child" in children.read())

    def test_children_can_be_added_to_bag(self):
        """method to test that a child can be added to the database
        """
        # test that test_child is not already in the bag
        with open("children.txt", "r") as children:
            self.assertFalse("test_child" in children.read())
        # add test_child to the bag
        self.bag._add_child("test_child")
        # test that child was added
        with open("children.txt", "r") as children:
            self.assertTrue("test_child" in children.read())
        # removes test_child from the list
        self.clean_up_files('children.txt', 'test_child')

    def test_childrens_toys_can_be_removed_from_bag(self):
        self.assertTrue(self.bag.remove_loot())

    def test_can_get_list_of_children(self):
        self.assertTrue(self.bag.get_children())

    def test_can_get_list_of_childs_loot(self):
        self.assertTrue(self.bag.get_childs_loot())

if __name__ == '__main__':
    unittest.main()
