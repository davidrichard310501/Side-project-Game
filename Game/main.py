from PyQt5 import QtCore, QtGui, QtWidgets, uic
import random
import sys
from classes.Enemy import Characters
from classes.Items import Healpotion
from classes.Items import Damagepotion
from HunterVsBoar import Ui_Form
import HunterVsBoar

class MyForm(QtWidgets.QWidget):

    #Chars
    boar = Characters('Boar', 400, 250, 30, 90)
    hunter = Characters('Hunter', 300, 500, 35, 90)

    #Items
    healpotion = Healpotion(30, 50)
    damagepotion = Damagepotion(5, 12)

    #BaseValues
    boar_base_hp = boar.hp
    hunter_base_hp = hunter.hp

    change_hp_boar = boar.hp
    change_hp_hunter = hunter.hp
    value_atk_btn = True


    def __init__(self, parent = None):
        QtWidgets.Qwidget.__init__(self, parent)

        ui = Ui_Form()
        ui.setupUi(self)

        self.ui.attack_btn.clicked.connect(self.test)
        self.ui.heal_btn.clicked.connect(self.heal_hunter)
        self.ui.start_btn.clicked.connect(self.event_start)

    #Set the button connectivity to true/false based on round, give back true value at end of round
    #So hunter can't attack 1+ times
    #Base value = true, after that set it to false
    # if value = true: button = on!


    def event_start(self):
        self.boar.get_stats()
        self.hunter.get_stats()

    def heal_boar(self):
        self.heal = self.healpotion.heal()
        self.boar.hp = self.boar.hp + self.heal
        print('Boar used a heal potion and has healed for', self.heal, 'hp')
            
    def use_potion_on_hunter(self):
        self.dmg = self.damagepotion.use_damage()
        self.hunter.hp = self.hunter.hp - self.dmg
        print("Damage dealt to hunter through damagepotion is", self.dmg)

    def use_potion_on_boar(self):
        self.dmg = self.damagepotion.use_damage()
        self.boar.hp = self.boar.hp - self.dmg
        print("Damage dealt to boar through damagepotion is", self.dmg) 


    def heal_hunter(self): 
        self.heal = self.healpotion.heal()
        self.hunter.hp = self.hunter.hp + self.heal
        print('Hunter used a heal potion and has healed for', self.heal, 'hp', 'and has ', self.hunter.hp, ' HP now')

    def hunter_tackle(self):

        self.previous_hp_hunter = self.hunter.hp
        self.previous_hp_hunter = self.boar.hp 

        print('Your turn: ')
        self.dmg = self.hunter.start_attack()
        self.boar.hp = self.boar.hp - self.dmg
        print('Hunter dealt: ', self.dmg, 'damage')
        print('Boar hp left:', self.boar.hp, '\n')
        self.hp_change_hunter()

        #Attack round boar

        self.rnd_nbm = random.randrange(0, 10, 1)
        self.rnd_nbm_2 = random.randrange(0, 10, 1)

        print("Boar's turn: ")
        self.dmg = self.hunter.start_attack()
        self.hunter.hp = self.hunter.hp - self.dmg
        print('Boar dealt: ', self.dmg, 'damage')
        print('Hunter hp left:', self.hunter.hp, '\n')
        self.hp_change_boar()

        #AI choices of attacks based on random numbers (heal and the usage of the damagepotion)
        if self.boar.hp < 100:
            self.heal_boar()
        elif self.boar.hp == 0:
            self.boar.hp = 0
            print('Boar was killed!, resetted to previous health points, game will start again')
            self.boar.hp = self.boar_previous_hp
            #insert a game close here

        if self.rnd_nbm == self.rnd_nbm_2:
            self.use_potion_on_hunter()

        #Allows hunter to attack again
        self.value_atk_btn = True

    def hp_change_hunter(self):
        self.change_hp_hunter = self.previous_hp_hunter / self.hunter.hp
        return self.change_hp_hunter

    def hp_change_boar(self):
        self.change_hp_boar = self.previous_hp_boar / self.boar.hp
        return self.change_hp_boar


    if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())