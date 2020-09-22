import unittest
from rpg.character import Character


class TestRpgCharacter(unittest.TestCase):

    def setUp(self):
        self.geralt = Character("Geralt", "of Rivia", 50)
        self.cloud = Character("Cloud", "Strife", 35)

    def tearDown(self):
        pass

    def test_full_name(self):
        self.assertEqual(self.geralt.full_name, "Geralt of Rivia")
        self.assertEqual(self.cloud.full_name, "Cloud Strife")
        self.geralt.first_name = "Gray"
        self.geralt.last_name = "Wolf"
        self.assertEqual(self.geralt.full_name, "Gray Wolf")

    def test_level_up(self):
        self.assertEqual(self.geralt.level, 50)
        self.assertEqual(self.cloud.level, 35)
        self.geralt.level_up()
        self.cloud.level_up()
        self.assertEqual(self.geralt.level, 51)
        self.assertEqual(self.cloud.level, 36)

    def test_attack_damage(self):
        self.assertEqual(self.geralt.attack_damage, 100)
        self.assertEqual(self.cloud.attack_damage, 70)
        self.geralt.level_up()
        self.cloud.level_up()
        self.assertEqual(self.geralt.attack_damage, 102)
        self.assertEqual(self.cloud.attack_damage, 72)


if __name__ == '__main__':
    unittest.main()
