
class Character:

    def __init__(self, first_name, last_name, level=1):
        self.first_name = first_name
        self.last_name = last_name
        self.level = level
        self.health = self.health_max

    @property
    def attack_damage(self):
        return self.level * 2

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    @property
    def health_max(self):
        return 50 + (self.level - 1) * 2

    def level_up(self):
        self.level += 1
        self.health = self.health_max
        return

    def modify_health(self, amount):
        new_health = self.health + amount
        if new_health < 0:
            new_health = 0
        elif new_health > self.health_max:
            new_health = self.health_max
        self.health = new_health
        return
