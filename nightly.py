import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class Player:
    def __init__(self,username,symbol):
        self.username=username
        self.symbol=symbol

    def __str__(self):
        return self.username+ ": "+self.symbol

player1=Player(input("Player Ж is called: "),"Ж")
player2=Player(input("Player 𝛀 is called: "),"𝛀")

class Gameloop:

    def __init__(self,current_player):
        self.playerlist=[player1,player2]
        self.current_player=current_player
        self.counter=0
        for i in range(1,10):
            setattr(self,"dot"+str(i),0)  

    def user_input1(self):
        gameloop.counter+=1
        widget.countertext.setText(str(gameloop.counter))
        widget.button1.setText(str(gameloop.current_player))
        if gameloop.current_player==player1:
            gameloop.current_player=player2
        elif gameloop.current_player==player2:
            gameloop.current_player=player1
        gameloop.SwitchPlayer()
        widget.Wincheck()
        widget.button1.setEnabled(False)

    def user_input2(self):
        gameloop.counter+=1
        widget.countertext.setText(str(gameloop.counter))
        widget.button2.setText(str(gameloop.current_player))
        if gameloop.current_player==player1:
            gameloop.current_player=player2
        elif gameloop.current_player==player2:
            gameloop.current_player=player1
        gameloop.SwitchPlayer()
        widget.Wincheck()
        widget.button2.setEnabled(False)

    def user_input3(self):
        gameloop.counter+=1
        widget.countertext.setText(str(gameloop.counter))
        widget.button3.setText(str(gameloop.current_player))
        if gameloop.current_player==player1:
            gameloop.current_player=player2
        elif gameloop.current_player==player2:
            gameloop.current_player=player1
        gameloop.SwitchPlayer()
        widget.Wincheck()
        widget.button3.setEnabled(False)

    def user_input4(self):
        gameloop.counter+=1
        widget.countertext.setText(str(gameloop.counter))
        widget.button4.setText(str(gameloop.current_player))
        if gameloop.current_player==player1:
            gameloop.current_player=player2
        elif gameloop.current_player==player2:
            gameloop.current_player=player1
        gameloop.SwitchPlayer()
        widget.Wincheck()
        widget.button4.setEnabled(False)

    def user_input5(self):
        gameloop.counter+=1
        widget.countertext.setText(str(gameloop.counter))
        widget.button5.setText(str(gameloop.current_player))
        if gameloop.current_player==player1:
            gameloop.current_player=player2
        elif gameloop.current_player==player2:
            gameloop.current_player=player1
        gameloop.SwitchPlayer()
        widget.Wincheck()
        widget.button5.setEnabled(False)

    def user_input6(self):
        gameloop.counter+=1
        widget.countertext.setText(str(gameloop.counter))
        widget.button6.setText(str(gameloop.current_player))
        if gameloop.current_player==player1:
            gameloop.current_player=player2
        elif gameloop.current_player==player2:
            gameloop.current_player=player1
        gameloop.SwitchPlayer()
        widget.Wincheck()
        widget.button6.setEnabled(False)

    def user_input7(self):
        gameloop.counter+=1
        widget.countertext.setText(str(gameloop.counter))
        widget.button7.setText(str(gameloop.current_player))
        if gameloop.current_player==player1:
            gameloop.current_player=player2
        elif gameloop.current_player==player2:
            gameloop.current_player=player1
        gameloop.SwitchPlayer()
        widget.Wincheck()
        widget.button7.setEnabled(False)

    def user_input8(self):
        gameloop.counter+=1
        widget.countertext.setText(str(gameloop.counter))
        widget.button8.setText(str(gameloop.current_player))
        if gameloop.current_player==player1:
            gameloop.current_player=player2
        elif gameloop.current_player==player2:
            gameloop.current_player=player1
        gameloop.SwitchPlayer()
        widget.Wincheck()
        widget.button8.setEnabled(False)

    def user_input9(self):
        gameloop.counter+=1
        widget.countertext.setText(str(gameloop.counter))
        widget.button9.setText(str(gameloop.current_player))
        if gameloop.current_player==player1:
            gameloop.current_player=player2
        elif gameloop.current_player==player2:
            gameloop.current_player=player1
        gameloop.SwitchPlayer()
        widget.Wincheck()
        widget.button9.setEnabled(False)

    def SwitchPlayer(self):
        if self.current_player == 1:
            self.current_player = 0
        elif self.current_player == 0:
            self.current_player = 1  

    def current_player(self):
        Player_current= self.playerlist[self.current_player]
        return Player_current      

gameloop=Gameloop(random.choice(seq=(player1,player2)))

class GUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        for i in range(1,10):
            setattr(self,"button"+str(i),QtWidgets.QPushButton(None))
        self.wintext=QtWidgets.QLabel("")
        self.countertext=QtWidgets.QLabel(str(gameloop.counter))
        self.layout=QtWidgets.QGridLayout(self)
        nb = 0
        for i in range(2,5):
            for j in range(2,5):
                nb+=1
                self.layout.addWidget(getattr(self, "button"+str(nb)),i,j)
        self.layout.addWidget(self.wintext,0,2)
        self.layout.addWidget(self.countertext,1,2)
        for i in range(1,10):
            getattr(self,"button"+str(i)).clicked.connect(getattr(Gameloop,"user_input"+str(i)))

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