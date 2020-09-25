import unittest
from unittest.mock import patch
from rpg.database_manager import DatabaseManager


@patch('rpg.database_manager.DatabaseManager.load_file')
class TestRpgDatabaseManager(unittest.TestCase):

    def setUp(self):
        self.party_json = [
            {
                "first_name": "Geralt",
                "last_name": "of Rivia",
                "level": 50
            }, {
                "first_name": "Cloud",
                "last_name": "Strife",
                "level": 35
            }
        ]

    def test_remove_party_member(self, mock_load_file):
        mock_load_file.return_value = self.party_json
        db = DatabaseManager()
        self.assertEqual(len(db.party), 2)
        db.remove_party_member("Geralt")
        self.assertEqual(len(db.party), 1)

    def test_remove_party_member_failed(self, mock_load_file):
        mock_load_file.return_value = self.party_json
        db = DatabaseManager()
        self.assertEqual(len(db.party), 2)
        db.remove_party_member("Tifa")
        self.assertEqual(len(db.party), 2)

    def test_party_names(self, mock_load_file):
        mock_load_file.return_value = self.party_json
        db = DatabaseManager()
        expected = ["Geralt of Rivia", "Cloud Strife"]
        self.assertEqual(db.party_names(), expected)


if __name__ == '__main__':
    unittest.main()
