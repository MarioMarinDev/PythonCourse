import json
import os
from rpg.character import Character


class DatabaseManager:

    def __init__(self):
        self.party = self.load_party()

    def load_party(self):
        party = []
        members_data = self.load_file("party.json")
        for member in members_data:
            party.append(Character(member["first_name"], member["last_name"], member["level"]))
        return party

    def load_file(self, file):
        if not os.path.exists(file):
            return []
        with open(file, "r") as file:
            return json.loads(file.read())

    def remove_party_member(self, member_name):
        for index, member in enumerate(self.party):
            if member.first_name == member_name:
                del self.party[index]

    def party_names(self):
        names = []
        for party_member in self.party:
            names.append(party_member.full_name)
        return names
