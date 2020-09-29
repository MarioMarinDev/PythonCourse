
from rpg.character import Character
from rpg.item import Item

if __name__ == '__main__':
    geralt = Character("Geralt", "of Rivia")
    geralt.level_up()
    venom = Item("Venom", "asdf", "health", -50)
    venom.use(geralt)
    potion = Item("Potion", "asdf", "health", 1000)
    potion.use(geralt)
    print(geralt.health, geralt.health_max)
