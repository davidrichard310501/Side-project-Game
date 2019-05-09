import random

class Characters:
    def __init__(self, name, hp, mp, atkl, atkh):
        self.hp = hp
        self.mp = mp
        self.atkl = atkl
        self.atkh = atkh
        self.name = name

class Hunter(Characters):
    def __init_(self):
        Characters.__init(self, name, hp, mp, atkl, atk)

    def start_attack(self):
        return random.randrange(self.atkl, self.atkh)
    
    def get_stats(self):
        return str("HP "+ str(self.name)+ ": "+ str(self.hp)+ "\nMP "+str( self.name)+ ": "+ str(self.mp)+ "\nLowest attack "+ str(self.name)+ ": "
                   +str(self.atkl)+ "\nHighest attack "+ str(self.name)+ ": "+ str(self.atkh)+"\n")

class Boar(Characters):
    def __init_(self):
        Characters.__init(self, name, hp, mp, atkl, atk)

    def start_attack(self):
        return random.randrange(self.atkl, self.atkh)

    def get_stats(self):
        return str("HP "+ str(self.name)+ ": "+ str(self.hp)+ "\nMP "+str( self.name)+ ": "+ str(self.mp)+ "\nLowest attack "+ str(self.name)+ ": "
                   +str(self.atkl)+ "\nHighest attack "+ str(self.name)+ ": "+ str(self.atkh)+"\n")