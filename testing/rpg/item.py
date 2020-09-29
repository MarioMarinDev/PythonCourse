from rpg.character import Character


class Item:

    def __init__(self, name, description, effect, amount=0):
        self.name = name
        self.description = description
        self.effect = effect
        self.amount = amount

    def use(self, target):
        if self.effect == "health" and isinstance(target, Character):
            target.modify_health(self.amount)
        return
