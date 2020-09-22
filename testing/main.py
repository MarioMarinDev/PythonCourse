
from rpg.character import Character

if __name__ == '__main__':
    mario = Character("Mario", "Marin")
    jan = Character("Jan", "Marin", 5)
    mario.level_up()
    print(mario.full_name, mario.attack_damage)
    print(jan.full_name, jan.attack_damage)
