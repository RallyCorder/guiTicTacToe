import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class Player:
    def __init__(self,username,symbol):
        self.username=username
        self.symbol=symbol

    def __str__(self):
        return self.username+ ": "+self.symbol

class Gameloop:

    def __init__(self):
        super().__init__()

        self.listeJoueurs=[Player(input("Player Ж is called: "),"Ж"),Player(input("Player 𝛀 is called: "),"𝛀")]
        self.joueurActu=random.randint(0,1)
        self.chosen_box=None
        for i in range(1,10):
            setattr(self, "dot"+str(i),0)
        
#py thinks of self in self.dot1 as a boolean

    def user_input1(self):
        if self.dot1==1:
            pass
        else:
            chosen_box = self.current_player()
            self.counter+=1
            GUI.countertext.setText(str(self.counter))
            GUI.button1.setText(str(chosen_box))
            self.SwitchPlayer()
            GUI.Wincheck()
            self.dot1+=1

    def user_input2(self):
        if self.dot2==1:
            pass
        else:
            chosen_box = self.current_player()
            self.counter+=1
            GUI.countertext.setText(str(self.counter))
            GUI.button2.setText(str(chosen_box))
            self.SwitchPlayer()
            GUI.Wincheck()
            self.dot2+=1

    def user_input3(self):
        if self.dot3==1:
            pass
        else:
            chosen_box = self.current_player()
            self.counter+=1
            GUI.countertext.setText(str(self.counter))
            GUI.button3.setText(str(chosen_box))
            self.SwitchPlayer()
            GUI.Wincheck()
            self.dot3+=1

    def user_input4(self):
        if self.dot4==1:
            pass
        else:
            chosen_box = self.current_player()
            self.counter+=1
            GUI.countertext.setText(str(self.counter))
            GUI.button4.setText(str(chosen_box))
            self.SwitchPlayer()
            GUI.Wincheck()
            self.dot4+=1

    def user_input5(self):
        if self.dot5 == 1:
            pass
        else:
            chosen_box = self.current_player()
            self.counter+=1
            GUI.countertext.setText(str(self.counter))
            GUI.button5.setText(str(chosen_box))
            self.SwitchPlayer()
            GUI.Wincheck()
            self.dot5+=1

    def user_input6(self):
        if self.dot6 == 1:
            pass
        else:
            chosen_box = self.current_player()
            self.counter+=1
            GUI.countertext.setText(str(self.counter))
            GUI.button6.setText(str(chosen_box))
            self.SwitchPlayer()
            GUI.Wincheck()
            self.dot6+=1

    def user_input7(self):
        if self.dot7 == 1:
            pass
        else:
            chosen_box = self.current_player()
            self.counter+=1
            GUI.countertext.setText(str(self.counter))
            GUI.button7.setText(str(chosen_box))
            self.SwitchPlayer()
            GUI.Wincheck()
            self.dot7+=1

    def user_input8(self):
        if self.dot8 == 1:
            pass
        else:
            chosen_box = self.current_player()
            self.counter+=1
            GUI.countertext.setText(str(self.counter))
            GUI.button8.setText(str(chosen_box))
            self.SwitchPlayer()
            GUI.Wincheck()
            self.dot8+=1

    def user_input9(self):
        if self.dot9 == 1:
            pass
        else:
            chosen_box = self.current_player()
            self.counter+=1
            GUI.countertext.setText(str(self.counter))
            GUI.button9.setText(str(chosen_box))
            self.SwitchPlayer()
            GUI.Wincheck()
            self.dot9+=1

    def SwitchPlayer(self):
        if self.joueurActu == 1:
            self.joueurActu = 0
        elif self.joueurActu == 0:
            self.joueurActu = 1  

    def current_player(self):
        Player_current= self.listeJoueurs[self.joueurActu]
        return Player_current      

    def Game(self):
        self.listeJoueurs

Gameloop()

class GUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        for i in range(1,10):
            setattr(self,"button"+str(i),QtWidgets.QPushButton(None))
        self.wintext=QtWidgets.QLabel("")
        self.counter=0
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
            getattr(self, "button"+str(i)).clicked.connect(getattr(Gameloop,"user_input"+str(i)))


    def Wincheck(self):
        for i in range(1,8,3):
            if getattr(self,"button"+str(i)).text() == getattr(self,"button"+str(i+1)).text() == getattr(self,"button"+str(i+2)).text() and getattr(self,"button"+str(i)).text():
                if getattr(self,"button"+str(i)).text() == getattr(self,"button"+str(i+1)).text() == getattr(self,"button"+str(i+2)).text() and getattr(self,"button"+str(i)).text() == None:
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
                if self.button1.text() == self.button5.text() == self.button9.text() and self.button1.text() == None:
                    pass
                else:
                    self.wintext.setText(str(self.button1.text())+" is the winner!")
        if self.button3.text() == self.button5.text() == self.button7.text() and self.button3.text():
            if self.button3.text() == self.button5.text() == self.button7.text() and self.button3.text() == None:
                pass
            else:
                self.wintext.setText(str(self.button3.text())+" is the winner!")
            

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = GUI()
    widget.resize(200,200)
    widget.show()

    sys.exit(app.exec())

''' attempt at optimising the user_input func, failure due to line 50 getattr(self, "user_input"+str(i)), 'GUI' object has no attribute 'user_input1'
    def user_input(self, i):
        chosen_box = self.current_player()
        self.compteur+=1
        getattr(self,"button"+str(i)).setText(str(chosen_box))
        self.SwitchPlayer()
        self.Wincheck()
'''