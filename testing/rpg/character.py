
class Character:

    def __init__(self, first_name, last_name, level=1):
        self.first_name = first_name
        self.last_name = last_name
        self.level = level

    @property
    def attack_damage(self):
        return self.level * 2

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    def level_up(self):
        self.level += 1
        return
