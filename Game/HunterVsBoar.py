from PyQt5 import QtCore, QtGui, QtWidgets
import random
from classes.Enemy import Characters
from classes.Items import Healpotion
from classes.Items import Damagepotion

class Ui_Form(object):

   
    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.resize(1037, 885)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 819, 1031, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.attack_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.attack_btn.setFont(font)
        self.attack_btn.setObjectName("attack_btn")
        self.horizontalLayout.addWidget(self.attack_btn)
        self.heal_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.heal_btn.setCheckable(False)
        self.heal_btn.setObjectName("heal_btn")
        self.horizontalLayout.addWidget(self.heal_btn)
        self.dmg_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.dmg_btn.setObjectName("dmg_btn")
        self.horizontalLayout.addWidget(self.dmg_btn)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1041, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout.addWidget(self.textBrowser_2)
        self.textBrowser_1 = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser_1.setObjectName("textBrowser_1")
        self.verticalLayout.addWidget(self.textBrowser_1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(440, 790, 131, 16))
        self.label.setObjectName("label")
        self.hp_hunter = QtWidgets.QProgressBar(Form) 
        self.hp_hunter.setGeometry(QtCore.QRect(10, 790, 118, 23))
        self.hp_hunter.setProperty("value", 100)#change value to hp in %
        self.hp_hunter.setObjectName("hp_hunter")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 770, 47, 13))
        self.label_2.setObjectName("label_2")
        #hpbar
        self.hp_boar = QtWidgets.QProgressBar(Form)
        self.hp_boar.setGeometry(QtCore.QRect(900, 790, 118, 23))
        self.hp_boar.setProperty("value", 100) #change value to hp in %
        self.hp_boar.setObjectName("hp_boar")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(930, 770, 47, 13))
        self.label_3.setObjectName("label_3")
        self.start_btn = QtWidgets.QPushButton(Form)
        self.start_btn.setGeometry(QtCore.QRect(370, 630, 75, 23))
        self.start_btn.setObjectName("start_btn")
        self.stop_btn = QtWidgets.QPushButton(Form)
        self.stop_btn.setGeometry(QtCore.QRect(520, 630, 75, 23))
        self.stop_btn.setObjectName("stop_btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Hunter vs Boar"))
        self.attack_btn.setText(_translate("Form", "Attack"))
        self.heal_btn.setText(_translate("Form", "Heal"))
        self.dmg_btn.setText(_translate("Form", "Damage potion"))
        self.label.setText(_translate("Form", "What do you want to do?"))
        self.label_2.setText(_translate("Form", "Hunter"))
        self.label_3.setText(_translate("Form", "Boar"))
        self.start_btn.setText(_translate("Form", "Start!"))
        self.stop_btn.setText(_translate("Form", "Stop!"))





