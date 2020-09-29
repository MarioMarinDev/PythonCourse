import unittest
from rpg.item import Item
from rpg.character import Character


class TestItem(unittest.TestCase):

    def setUp(self):
        self.char = Character("Geralt", "of Rivia")

    def test_use_health(self):
        item = Item("Vemon", "asdf", "health", -25)
        item.use(self.char)
        self.assertEqual(self.char.health, 25)


if __name__ == '__main__':
    unittest.main()
