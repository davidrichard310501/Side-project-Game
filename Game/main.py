#!/usr/bin/python
import random
from classes.Chars import Boar
from classes.Chars import Hunter
from classes.Items import Healpotion
from classes.Items import Damagepotion
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from HunterVsBoar import Ui_Form

class PythonGame(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
       super(PythonGame, self).__init__(parent=parent)
       self.ui = Ui_Form()
       self.ui.setupUi(self)

       self.ui.attack_btn.clicked.connect(self.start_attack)
       self.ui.heal_btn.clicked.connect(self.heal_hunter)
       self.ui.dmg_btn.clicked.connect(self.use_potion_on_boar)
       self.ui.start_btn.clicked.connect(self.event_start)
       self.ui.stop_btn.clicked.connect(self.event_stop)
       self.ui.hp_hunter.setValue(100)
       self.ui.hp_boar.setValue(100)

       self.ui.attack_btn.setEnabled(False)
       self.ui.heal_btn.setEnabled(False)
       self.ui.dmg_btn.setEnabled(False)
       self.ui.stop_btn.setEnabled(False)
               
    #Initalize character values   
    boar = Boar('Boar', 400, 250, 30, 90)
    hunter = Hunter('Hunter', 300, 500, 35, 90)
    #Initialize item values
    healpotion = Healpotion(30, 50)
    damagepotion = Damagepotion(15, 35)
    #Initialize base values
    boar_base_hp = boar.hp
    hunter_base_hp = hunter.hp


    def event_start(self):
        #Starts the game, displays the stats of the characters and enables the buttons
        self.ui.textBrowser.append(self.hunter.get_stats())
        self.ui.textBrowser.append(self.boar.get_stats())
        self.ui.start_btn.setEnabled(False)

        self.ui.attack_btn.setEnabled(True)
        self.ui.heal_btn.setEnabled(True)
        self.ui.dmg_btn.setEnabled(True)
        self.ui.stop_btn.setEnabled(True)


    def event_stop(self):
        #Calls the rest function, disables every button expect the start button
        self.reset_event()

        self.ui.attack_btn.setEnabled(False)
        self.ui.heal_btn.setEnabled(False)
        self.ui.dmg_btn.setEnabled(False)
        self.ui.stop_btn.setEnabled(False)


    def clear_browser(self):
        #Clears the history of the textBrowser
        self.ui.textBrowser.clear()


    def reset_event(self):
        #Sets hp values to base values, updates the hp bars, disables the buttons expect start, clears textBrowser history
        self.boar.hp = self.boar_base_hp
        self.hunter.hp = self.hunter_base_hp
        self.hp_bar_hunter()
        self.hp_bar_boar()         
        self.clear_browser()
        self.ui.start_btn.setEnabled(True)

        self.ui.attack_btn.setEnabled(False)
        self.ui.heal_btn.setEnabled(False)
        self.ui.dmg_btn.setEnabled(False)
        self.ui.stop_btn.setEnabled(False)

            
    def heal_boar(self):
        #Heals the boar for a random value between the set value
        self.heal = self.healpotion.heal()
        self.boar.hp = self.boar.hp + self.heal
        self.ui.textBrowser.append('Boar used a heal potion and has healed for'+ str(self.heal) + 'hp')
        self.hp_bar_boar()
        
            
    def use_potion_on_hunter(self):
        #Boar attacks the hunter with a "damage potion", this deals a random value of damage between two set values
        if self.hunter.hp > 0:
            self.dmg = self.damagepotion.use_damage()
            self.hunter.hp = self.hunter.hp - self.dmg
            self.ui.textBrowser.append("Damage dealt to hunter through damagepotion is: " + str(self.dmg))
            self.hp_bar_hunter()

        else:
            self.hunter.hp = 0
            self.hp_bar_hunter()
            self.ui.textBrowser.append('Hunter was killed!, resetted to previous health points, game will start again')
            self.reset_event()


    def use_potion_on_boar(self):
        #Hunter attacks the hunter with a "damage potion", this deals a random value of damage between two set values
        self.heal_nmb_1 = random.randrange(0, 5, 1)
        self.heal_nmb_2 = random.randrange(0, 5, 1)

        self.dmg = self.damagepotion.use_damage()
        self.boar.hp = self.boar.hp - self.dmg
        self.ui.textBrowser.append("Damage dealt to boar through damagepotion is: " + str(self.dmg)) 
        self.ui.textBrowser.append("HP left: "+ str(self.boar.hp))
        self.hp_bar_boar()


        if self.boar.hp <= 0:
            self.boar.hp = 0
            self.ui.textBrowser.append('Boar was killed!, resetted to previous health points, game will start again')
            self.reset_event()   
        elif self.boar.hp < 150 and self.heal_nmb_1 == self.heal_nmb_2:
            self.heal_boar()
             
            
    def heal_hunter(self): 
        self.heal = self.healpotion.heal()
        self.hunter.hp = self.hunter.hp + self.heal
        self.ui.textBrowser.append('Hunter used a heal potion and has healed for'+ str(self.heal)+ ' hp '+ 'and has '+ str(self.hunter.hp)+ ' HP now')
        if self.hunter.hp > self.hunter_base_hp:
            self.ui.hp_hunter.setValue(100)
        else:
            self.hp_bar_hunter()


    def hp_bar_boar(self):
        #Updates the HP bar of the boar
        self.change_hp_boar = self.boar.hp * 100 / self.boar_base_hp
        self.ui.hp_boar.setValue(self.change_hp_boar)


    def hp_bar_hunter(self):
        #Updates the HP bar of the hunter
        self.change_hp_hunter = self.hunter.hp * 100 / self.hunter_base_hp
        self.ui.hp_hunter.setValue(self.change_hp_hunter)


    def hunter_attack(self):
        #Starts the attack of the hunter, calls reset function upon death of the boar
        if self.boar.hp <= 0:
            self.boar.hp = 0
            self.hp_bar_boar()
            self.ui.textBrowser.append('Boar was killed!, resetted to previous health points, game will start again')
            self.reset_event()
        else:          
            self.ui.textBrowser.append('Your turn: ')
            self.dmg = self.hunter.start_attack()
            self.boar.hp = self.boar.hp - self.dmg
            self.hp_bar_boar()
            if self.boar.hp > 0:
                self.ui.textBrowser.append('Hunter dealt: '+ str(self.dmg)+ ' damage')
                self.ui.textBrowser.append('Boar hp left: '+ str(self.boar.hp)+ '\n')
                self.hp_bar_boar()
            else:
                self.ui.textBrowser.append('Hunter dealt: '+ str(self.dmg)+ ' damage')
                self.ui.textBrowser.append('Boar hp left: '+ str(0)+ '\n')              
                self.hp_bar_boar()
                
    def boar_attack(self):
        #Starts the attack of the boar (counterattack to the hunter), calls reset function upon death of the hunter
        if self.hunter.hp <=0:
            self.hunter.hp = 0
            self.hp_bar_hunter()
            self.ui.textBrowser.append('Hunter was killed!, resetted to previous health points, game will start again')
            self.reset_event()        
        else:           
             self.ui.textBrowser.append("Boar's turn: ")
             self.dmg = self.boar.start_attack()
             self.hunter.hp = self.hunter.hp - self.dmg
             self.hp_bar_hunter()
             if self.hunter.hp > 0:
                self.ui.textBrowser.append('Boar dealt: ' + str(self.dmg) + ' damage')
                self.ui.textBrowser.append('Hunter hp left: '+ str(self.hunter.hp)+ '\n')                    
                self.hp_bar_hunter()
             else:
                self.ui.textBrowser.append('Boar dealt: ' + str(self.dmg) + ' damage')
                self.ui.textBrowser.append('Hunter hp left: '+ str(0)+ '\n')                     
                self.hp_bar_hunter()
        #Boar heal choice ( 1:5 )
        self.heal_nmb_1 = random.randrange(0, 5, 1)
        self.heal_nmb_2 = random.randrange(0, 5, 1)
        if self.boar.hp < 150 and self.heal_nmb_1 == self.heal_nmb_2:
            self.heal_boar()
            if self.boar.hp > self.boar_base_hp:
                self.ui.hp_boar.setValue(100)
        #Boar 1:5 chance of using the damage potion
        self.rnd_nmb_1 = random.randrange(0, 5, 1)
        self.rnd_nmb_2 = random.randrange(0, 5, 1)
        if self.rnd_nmb_1 == self.rnd_nmb_2:
            self.use_potion_on_hunter()

    
    def start_attack(self): 
        #Starts the attack sequences with the "attack_btn"
        self.hunter_attack()
        self.boar_attack()
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = PythonGame()
    Form.show()
    sys.exit(app.exec_())