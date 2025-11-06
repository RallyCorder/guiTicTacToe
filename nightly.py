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

        for i in range(1,10):
            setattr(self, "button"+str(i), QtWidgets.QPushButton(None))
        self.text = QtWidgets.QLabel ("Winner?")

        self.layout = QtWidgets.QGridLayout(self)

        nb = 0
        for i in range(3):
            for j in range(3):
                nb += 1
                self.layout.addWidget(getattr(self, "button"+str(nb)), i, j)

        self.layout.addWidget(self.text)

        for i in range(1,10):
            getattr(self, "button"+str(i)).clicked.connect(getattr(self, "user_input"+str(i)))

    def user_input1(self):
        casechoisie = self.joueur_actuel()
        self.compteur+=1
        self.button1.setText(str(casechoisie))
        self.SwitchPlayer()

    def user_input2(self):
        casechoisie = self.joueur_actuel()
        self.compteur+=1
        self.button2.setText(str(casechoisie))
        self.SwitchPlayer()

    def user_input3(self):
        casechoisie = self.joueur_actuel()
        self.compteur+=1
        self.button3.setText(str(casechoisie))
        self.SwitchPlayer()

    def user_input4(self):
        casechoisie = self.joueur_actuel()
        self.compteur+=1
        self.button4.setText(str(casechoisie))
        self.SwitchPlayer()

    def user_input5(self):
        casechoisie = self.joueur_actuel()
        self.compteur+=1
        self.button5.setText(str(casechoisie))
        self.SwitchPlayer()

    def user_input6(self):
        casechoisie = self.joueur_actuel()
        self.compteur+=1
        self.button6.setText(str(casechoisie))
        self.SwitchPlayer()

    def user_input7(self):
        casechoisie = self.joueur_actuel()
        self.compteur+=1
        self.button7.setText(str(casechoisie))
        self.SwitchPlayer()

    def user_input8(self):
        casechoisie = self.joueur_actuel()
        self.compteur+=1
        self.button8.setText(str(casechoisie))
        self.SwitchPlayer()

    def user_input9(self):
        casechoisie = self.joueur_actuel()
        self.compteur+=1
        self.button9.setText(str(casechoisie))
        self.SwitchPlayer()

    def SwitchPlayer(self):
        if self.joueurActu == 1:
            self.joueurActu = 0
        elif self.joueurActu == 0:
            self.joueurActu = 1

    @QtCore.Slot()


    def Wincheck(self):
        
        if self.button1.text() == self.button2.text() == self.button3.text():
            if all == None:
                pass
            else:
                self.text.setText("WINNER!")
        if self.button4.text() == self.button5.text() == self.button6.text():
            if all == None:
                pass
            else:
                self.text.setText("WINNER!")
        if self.button7.text() == self.button8.text() == self.button9.text():
            if all == None:
                pass
            else:
                self.text.setText("WINNER!")

        if self.button1.text() == self.button4.text() == self.button7.text():
            if all == None:
                pass
            else:
                self.text.setText("WINNER!")
        if self.button2.text() == self.button5.text() == self.button8.text():
            if all == None:
                pass
            else:
                self.text.setText("WINNER!")
        if self.button3.text() == self.button6.text() == self.button9.text():
            if all == None:
                pass
            else:
                self.text.setText("WINNER!")

        if self.button1.text() == self.button5.text() == self.button9.text():
            if all == None:
                pass
            else:
                self.text.setText("WINNER!")
        if self.button3.text() == self.button5.text() == self.button7.text():
            if all == None:
                pass
            else:
                self.text.setText("WINNER!")
        else:
            pass

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

''' attempt at optimising the user_input func, failure due to line 50 getattr(self, "user_input"+str(i)), 'GUI' object has no attribute 'user_input1'
    def user_input(self, i):
        casechoisie = self.joueur_actuel()
        self.compteur+=1
        getattr(self,"button"+str(i)).setText(str(casechoisie))
        self.SwitchPlayer()
        self.Wincheck()
'''

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