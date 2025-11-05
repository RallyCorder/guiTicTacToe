import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class Joueur :
    def __init__(self, nom, symbole):
        self.nom = nom
        self.symbole = symbole

    def __str__(self):
        return self.nom + ": "+ self.symbole

class Case:

    def __init__(self,position,valeur):
        self.position=position
        self.valeur=valeur

    def __str__(self):
        if self.valeur!= None:
            return self.valeur
        else:
            return str(self.position)

class GUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.hello = ["X","O"]
        self.listeJoueurs =  [Joueur(input("Nom joueur 1:"),"X"),Joueur(input("Nom joueur 2:"),"O")]
        self.joueurActu = 1
        self.compteur = 0
        self.casechoisie = None

        self.button1 = QtWidgets.QPushButton("")
        self.button2 = QtWidgets.QPushButton("")
        self.button3 = QtWidgets.QPushButton("")
        self.button4 = QtWidgets.QPushButton("")
        self.button5 = QtWidgets.QPushButton("")
        self.button6 = QtWidgets.QPushButton("")
        self.button7 = QtWidgets.QPushButton("")
        self.button8 = QtWidgets.QPushButton("")
        self.button9 = QtWidgets.QPushButton("")

        self.layout = QtWidgets.QGridLayout(self)
        self.layout.addWidget(self.button1, 0, 0)
        self.layout.addWidget(self.button2, 0, 1)
        self.layout.addWidget(self.button3, 0, 2)
        self.layout.addWidget(self.button4, 1, 0)
        self.layout.addWidget(self.button5, 1, 1)
        self.layout.addWidget(self.button6, 1, 2)
        self.layout.addWidget(self.button7, 2, 0)
        self.layout.addWidget(self.button8, 2, 1)
        self.layout.addWidget(self.button9, 2, 2)

        self.button1.clicked.connect(self.input1)
        self.button2.clicked.connect(self.input2)
        self.button3.clicked.connect(self.input3)
        self.button4.clicked.connect(self.input4)
        self.button5.clicked.connect(self.input5)
        self.button6.clicked.connect(self.input6)
        self.button7.clicked.connect(self.input7)
        self.button8.clicked.connect(self.input8)
        self.button9.clicked.connect(self.input9)



    def SwitchPlayer(self):
        if self.joueurActu == 1:
            self.joueurActu = 0
        elif self.joueurActu == 0:
            self.joueurActu = 1

    @QtCore.Slot()
    def input1(self):
        casechoisie = self.joueur_actuel()
        self.compteur+=1
        self.button1.setText(str(casechoisie))
        self.SwitchPlayer()

    def input2(self):
        casechoisie = self.joueur_actuel()
        self.compteur+=1
        self.button2.setText(str(casechoisie))
        self.SwitchPlayer()

    def input3(self):
        casechoisie = self.joueur_actuel()
        self.compteur+=1
        self.button3.setText(str(casechoisie))
        self.SwitchPlayer()

    def input4(self):
        casechoisie = self.joueur_actuel()
        self.compteur+=1
        self.button4.setText(str(casechoisie))
        self.SwitchPlayer()

    def input5(self):
        casechoisie = self.joueur_actuel()
        self.compteur+=1
        self.button5.setText(str(casechoisie))
        self.SwitchPlayer()

    def input6(self):
        casechoisie = self.joueur_actuel()
        self.compteur+=1
        self.button6.setText(str(casechoisie))
        self.SwitchPlayer()

    def input7(self):
        casechoisie = self.joueur_actuel()
        self.compteur+=1
        self.button7.setText(str(casechoisie))
        self.SwitchPlayer()

    def input8(self):
        casechoisie = self.joueur_actuel()
        self.compteur+=1
        self.button8setText(str(casechoisie))
        self.SwitchPlayer()

    def input9(self):
        casechoisie = self.joueur_actuel()
        self.compteur+=1
        self.button9.setText(str(casechoisie))
        self.SwitchPlayer()

    def joueur_actuel(self):
        Player= self.listeJoueurs[self.joueurActu]
        return Player

    def jeu_entier(self):
        while self.plateau.verif_victoire()!=True and self.compteur!=9:
            self.SwitchPlayer()
            self.tours()
        if self.plateau.verif_victoire():
            print(f"Bravo ! "+self.joueur_actuel().nom+" vous avez gagné ! ")
        else:
            print("Egalité")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = GUI()
    widget.resize(200,200)
    widget.show()

    sys.exit(app.exec())

j=GUI()
j.jeu_entier()

''''
NOW NEED TO WRITE THE WINCHECK, EITHER PATCH LEGACY CODE TO NEW OR CHANGE NEW TO MATCH COUNTING SCHEME
LEGACY CODE:
   
    def verif_victoire(self):
        for i in range(0,9,3):
            if self.grille[0+i].valeur == self.grille[1+i].valeur == self.grille[2+i].valeur and self.grille[0+i].valeur != None:
                return True
        for i in range(3):
            if self.grille[0+i].valeur == self.grille[3+i].valeur == self.grille[6+i].valeur and self.grille[0+i].valeur != None:
                return True
        if self.grille[0].valeur == self.grille[4].valeur == self.grille[8].valeur and self.grille[0].valeur != None:
                return True
        if self.grille[2].valeur == self.grille[4].valeur == self.grille[6].valeur and self.grille[2].valeur != None:
                return True


'''''