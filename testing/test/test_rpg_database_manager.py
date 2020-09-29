import unittest
import json
import os
from unittest.mock import patch
from rpg.database_manager import DatabaseManager


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
        with patch('rpg.database_manager.DatabaseManager.load_file') as mock_load_file:
            mock_load_file.return_value = self.party_json
            self.db = DatabaseManager()

    def test_remove_party_member(self):
        self.assertEqual(len(self.db.party), 2)
        self.db.remove_party_member("Geralt")
        self.assertEqual(len(self.db.party), 1)

    def test_remove_party_member_failed(self):
        self.assertEqual(len(self.db.party), 2)
        self.db.remove_party_member("Tifa")
        self.assertEqual(len(self.db.party), 2)

    def test_party_names(self):
        expected = ["Geralt of Rivia", "Cloud Strife"]
        self.assertEqual(self.db.party_names(), expected)

    def test_load_file(self):
        # File does not exist
        db = DatabaseManager()
        self.assertEqual(db.party, [])
        # File does exists
        file = open("party.json", "w")
        file.write(json.dumps(self.party_json, indent=2))
        file.close()
        db = DatabaseManager()
        self.assertEqual(len(db.party), 2)
        os.remove("party.json")


if __name__ == '__main__':
    unittest.main()
