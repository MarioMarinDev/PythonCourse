
class Character:

    def __init__(self, name="Unknown", health=100, damage=10):
        self.name = name
        self.health = health
        self.damage = damage

    def show_stats(self):
        print("Name: " + self.name)
        print("HP: " + str(self.health))
        print("Damage: " + str(self.damage))


# Create two characters
char_1 = Character()
char_2 = Character("Mario", 105, 8)
char_1.show_stats()
print("\n")
char_2.show_stats()
