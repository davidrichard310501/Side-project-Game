import random

class Items:

    def __init__(self, minamount, maxamount):
        self.minamount = minamount
        self.maxamount = maxamount


class Healpotion(Items):

    def __init__(self, minamount, maxamount):
        Items.__init__(self, minamount, maxamount)

    def heal(self):
        self.hp = random.randrange(self.minamount, self.maxamount)
        return self.hp


class Damagepotion(Items):
    def __init__(self, minamount, maxamount):
        Items.__init__(self, minamount, maxamount)

    def use_damage(self):
        self.damage = random.randrange(self.minamount, self.maxamount)
        return self.damage