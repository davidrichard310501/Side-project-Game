import random

class Characters:
    def __init__(self, name, hp, mp, atkl, atkh):
        self.hp = hp
        self.mp = mp
        self.atkl = atkl
        self.atkh = atkh
        self.name = name

    def get_stats(self):
        print(self.name, ':', "Lowest attack is ",self.atkl, ". Highest attack is ",self.atkh, ". HP is ",self.hp, ". Mana is ",self.mp)

    def start_attack(self):

        return random.randrange(self.atkl, self.atkh)