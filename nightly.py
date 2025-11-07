import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class Player:
    def __init__(self,nom,symbole):
        self.nom=nom
        self.symbole=symbole

    def __str__(self):
        return self.nom+ ": "+self.symbole

class Box:

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
        
        self.listeJoueurs=[Player(input("Player Ж is called: "),"Ж"),Player(input("Player 𝛀 is called: "),"𝛀")]
        self.joueurActu=random.randint(0,1)
        self.counter=0
        self.chosen_box=None
        for i in range(1,10):
            setattr(self, "dot"+str(i),0)


        for i in range(1,10):
            setattr(self,"button"+str(i),QtWidgets.QPushButton(None))
        self.wintext=QtWidgets.QLabel("")
        self.countertext=QtWidgets.QLabel(str(self.counter))
        
        self.layout=QtWidgets.QGridLayout(self)
        nb = 0
        for i in range(2,5):
            for j in range(2,5):
                nb+=1
                self.layout.addWidget(getattr(self, "button"+str(nb)),i,j)
        self.layout.addWidget(self.wintext,0,2)
        self.layout.addWidget(self.countertext,1,2)

        for i in range(1,10):
            getattr(self, "button"+str(i)).clicked.connect(getattr(self,"user_input"+str(i)))

    def user_input1(self):
        if self.dot1==1:
            pass
        else:
            chosen_box = self.current_player()
            self.counter+=1
            self.countertext.setText(str(self.counter))
            self.button1.setText(str(chosen_box))
            self.SwitchPlayer()
            self.Wincheck()
            self.dot1+=1

    def user_input2(self):
        if self.dot2==1:
            pass
        else:
            chosen_box = self.current_player()
            self.counter+=1
            self.countertext.setText(str(self.counter))
            self.button2.setText(str(chosen_box))
            self.SwitchPlayer()
            self.Wincheck()
            self.dot2+=1

    def user_input3(self):
        if self.dot3==1:
            pass
        else:
            chosen_box = self.current_player()
            self.counter+=1
            self.countertext.setText(str(self.counter))
            self.button3.setText(str(chosen_box))
            self.SwitchPlayer()
            self.Wincheck()
            self.dot3+=1

    def user_input4(self):
        if self.dot4==1:
            pass
        else:
            chosen_box = self.current_player()
            self.counter+=1
            self.countertext.setText(str(self.counter))
            self.button4.setText(str(chosen_box))
            self.SwitchPlayer()
            self.Wincheck()
            self.dot4+=1

    def user_input5(self):
        if self.dot5 == 1:
            pass
        else:
            chosen_box = self.current_player()
            self.counter+=1
            self.countertext.setText(str(self.counter))
            self.button5.setText(str(chosen_box))
            self.SwitchPlayer()
            self.Wincheck()
            self.dot5+=1

    def user_input6(self):
        if self.dot6 == 1:
            pass
        else:
            chosen_box = self.current_player()
            self.counter+=1
            self.countertext.setText(str(self.counter))
            self.button6.setText(str(chosen_box))
            self.SwitchPlayer()
            self.Wincheck()
            self.dot6+=1

    def user_input7(self):
        if self.dot7 == 1:
            pass
        else:
            chosen_box = self.current_player()
            self.counter+=1
            self.countertext.setText(str(self.counter))
            self.button7.setText(str(chosen_box))
            self.SwitchPlayer()
            self.Wincheck()
            self.dot7+=1

    def user_input8(self):
        if self.dot8 == 1:
            pass
        else:
            chosen_box = self.current_player()
            self.counter+=1
            self.countertext.setText(str(self.counter))
            self.button8.setText(str(chosen_box))
            self.SwitchPlayer()
            self.Wincheck()
            self.dot8+=1

    def user_input9(self):
        if self.dot9 == 1:
            pass
        else:
            chosen_box = self.current_player()
            self.counter+=1
            self.countertext.setText(str(self.counter))
            self.button9.setText(str(chosen_box))
            self.SwitchPlayer()
            self.Wincheck()
            self.dot9+=1

    def SwitchPlayer(self):
        if self.joueurActu == 1:
            self.joueurActu = 0
        elif self.joueurActu == 0:
            self.joueurActu = 1


    def Wincheck(self):
        for i in range(1,8):
            if getattr(self,"button"+str(i)).text() == getattr(self,"button"+str(i+1)).text() == getattr(self,"button"+str(i+2)).text() and getattr(self,"button"+str(i)).text():
                if getattr(self,"button"+str(i)).text() == getattr(self,"button"+str(i+1)).text() == getattr(self,"button"+str(i+2)).text() and getattr(self,"button"+str(i)).text() == None:
                    if getattr(self,"button"+str(i+1%2==0)):
                        pass
                else:
                    self.wintext.setText(str(getattr(self,"button"+str(i)).text())+" is the winner!")
        
        for i in range(1,4):
            if getattr(self,"button"+str(i)).text() == getattr(self,"button"+str(i+3)).text() == getattr(self,"button"+str(i+6)).text() and getattr(self,"button"+str(i)).text():
                    if getattr(self,"button"+str(i)).text() == getattr(self,"button"+str(i+3)).text() == getattr(self,"button"+str(i+6)).text() and getattr(self,"button"+str(i)).text() == None:
                        pass
                    else:
                        self.wintext.setText(str(getattr(self,"button"+str(i)).text())+" is the winner!")

            if self.button1.text() == self.button5.text() == self.button9.text() and self.button1.text():
                if self.button1.text() == self.button5.text() == self.button9.text() and self.button1.text():
                    pass
                else:
                    self.wintext.setText(str(self.button1.text())+" is the winner!")
        if self.button3.text() == self.button5.text() == self.button7.text() and self.button3.text():
            if self.button3.text() == self.button5.text() == self.button7.text() and self.button3.text():
                pass
            else:
                self.wintext.setText(str(self.button3.text())+" is the winner!")
            

    def current_player(self):
        Player_current= self.listeJoueurs[self.joueurActu]
        return Player_current

    def jeu_entier(self):
        while self.plateau.verif_victoire()!=True and self.counter!=9:
            self.SwitchPlayer()
            self.tours()
        if self.plateau.verif_victoire():
            print(f"Bravo ! "+self.current_player().nom+" vous avez gagné ! ")
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
        chosen_box = self.current_player()
        self.compteur+=1
        getattr(self,"button"+str(i)).setText(str(chosen_box))
        self.SwitchPlayer()
        self.Wincheck()
'''