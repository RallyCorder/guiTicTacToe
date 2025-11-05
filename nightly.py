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


class Grille:

    def __init__(self):
        self.grille= [Case(0,None),Case(1,None),Case(2,None),Case(3,None),Case(4,None),Case(5,None),Case(6,None),Case(7,None),Case(8,None)]

    def estVide(self,pos):
        return self.grille[pos].valeur==None

    def joue(self,pos,perso):
        self.grille[pos].valeur= perso.symbole

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



    def __str__(self):
        text=""
        for j in range(0,9,3):
            text+="|"
            for i in range (0,3):
                if self.estVide(j+i):
                    a=" "
                else:
                    a= self.grille[j+i]
                text+=str(a)+"|"
            text+="\n"

        return text

class GUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.hello = ["X","O"]
        self.listeJoueurs =  [Joueur(input("Nom joueur 1:"),"X"),Joueur(input("Nom joueur 2:"),"O")]
        self.plateau = Grille()
        self.joueurActu = 1
        self.compteur = 0

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
        self.button1.clicked.connect(self.round)
        self.button2.clicked.connect(self.magic)
        self.button3.clicked.connect(self.magic)
        self.button4.clicked.connect(self.magic)
        self.button5.clicked.connect(self.magic)
        self.button6.clicked.connect(self.magic)
        self.button7.clicked.connect(self.magic)
        self.button8.clicked.connect(self.magic)
        self.button9.clicked.connect(self.magic)


    @QtCore.Slot()
    def magic(self):
        self.button1.setText(GUI.tours.casechoisie(self.hello))
        self.button2.setText(random.choice(self.hello))
        self.button3.setText(random.choice(self.hello))
        self.button4.setText(random.choice(self.hello))
        self.button5.setText(random.choice(self.hello))
        self.button6.setText(random.choice(self.hello))
        self.button7.setText(random.choice(self.hello))
        self.button8.setText(random.choice(self.hello))
        self.button9.setText(random.choice(self.hello))

    def joueur_actuel(self):
        Player= self.listeJoueurs[self.joueurActu]
        return Player


    def SwitchPlayer(self):
        if self.joueurActu == 1:
            self.joueurActu = 0
        elif self.joueurActu == 0:
            self.joueurActu = 1


    def tours(self):
        print(self.plateau)
        casechoisie= GUI.self.QtWidgets("Ecrit un nombre entre 1 et 9 ")
        while self.plateau.estVide(int(casechoisie)-1)!=True:
            print("La case choisie est déjà prise, choisissez une autre case")
            casechoisie = input("Ecrit un nombre entre 1 et 9 ") #peut rajouter une condition pour verifier que le joueur met bien un numéro entre 1 et 9
        self.plateau.joue(int(casechoisie)-1,self.joueur_actuel())
        self.compteur+=1

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