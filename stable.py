import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import Qt, QSize

class Player:
    def __init__(self,username,symbol):
        self.username=username
        self.symbol=symbol

    def __str__(self):
        return self.symbol

player1=Player(input("PLAYER Ж IS CALLED: "),"Ж")
player2=Player(input("PLAYER 𝛀 IS CALLED: "),"𝛀")

class Hideogame:

    def __init__(self,current_player):
        self.playerlist=[player1,player2]
        self.current_player=current_player
        self.counter=0

    def user_input1(self):
        gameloop_instance.counter+=1
        widget.countertext.setText("TURNS : "+str(gameloop_instance.counter))
        widget.button1.setText(str(gameloop_instance.current_player))
        if gameloop_instance.current_player==player1:
            gameloop_instance.current_player=player2
        elif gameloop_instance.current_player==player2:
            gameloop_instance.current_player=player1
        gameloop_instance.SwitchPlayer()
        gameloop_instance.Wincheck()
        widget.button1.setEnabled(False)
        widget.turnsymbol.setText(str(gameloop_instance.current_player))

    def user_input2(self):
        gameloop_instance.counter+=1
        widget.countertext.setText("TURNS : "+str(gameloop_instance.counter))
        widget.button2.setText(str(gameloop_instance.current_player))
        if gameloop_instance.current_player==player1:
            gameloop_instance.current_player=player2
        elif gameloop_instance.current_player==player2:
            gameloop_instance.current_player=player1
        gameloop_instance.SwitchPlayer()
        gameloop_instance.Wincheck()
        widget.button2.setEnabled(False)
        widget.turnsymbol.setText(str(gameloop_instance.current_player))

    def user_input3(self):
        gameloop_instance.counter+=1
        widget.countertext.setText("TURNS : "+str(gameloop_instance.counter))
        widget.button3.setText(str(gameloop_instance.current_player))
        if gameloop_instance.current_player==player1:
            gameloop_instance.current_player=player2
        elif gameloop_instance.current_player==player2:
            gameloop_instance.current_player=player1
        gameloop_instance.SwitchPlayer()
        gameloop_instance.Wincheck()
        widget.button3.setEnabled(False)
        widget.turnsymbol.setText(str(gameloop_instance.current_player))

    def user_input4(self):
        gameloop_instance.counter+=1
        widget.countertext.setText("TURNS : "+str(gameloop_instance.counter))
        widget.button4.setText(str(gameloop_instance.current_player))
        if gameloop_instance.current_player==player1:
            gameloop_instance.current_player=player2
        elif gameloop_instance.current_player==player2:
            gameloop_instance.current_player=player1
        gameloop_instance.SwitchPlayer()
        gameloop_instance.Wincheck()
        widget.button4.setEnabled(False)
        widget.turnsymbol.setText(str(gameloop_instance.current_player))

    def user_input5(self):
        gameloop_instance.counter+=1
        widget.countertext.setText("TURNS : "+str(gameloop_instance.counter))
        widget.button5.setText(str(gameloop_instance.current_player))
        if gameloop_instance.current_player==player1:
            gameloop_instance.current_player=player2
        elif gameloop_instance.current_player==player2:
            gameloop_instance.current_player=player1
        gameloop_instance.SwitchPlayer()
        gameloop_instance.Wincheck()
        widget.button5.setEnabled(False)
        widget.turnsymbol.setText(str(gameloop_instance.current_player))

    def user_input6(self):
        gameloop_instance.counter+=1
        widget.countertext.setText("TURNS : "+str(gameloop_instance.counter))
        widget.button6.setText(str(gameloop_instance.current_player))
        if gameloop_instance.current_player==player1:
            gameloop_instance.current_player=player2
        elif gameloop_instance.current_player==player2:
            gameloop_instance.current_player=player1
        gameloop_instance.SwitchPlayer()
        gameloop_instance.Wincheck()
        widget.button6.setEnabled(False)
        widget.turnsymbol.setText(str(gameloop_instance.current_player))

    def user_input7(self):
        gameloop_instance.counter+=1
        widget.countertext.setText("TURNS : "+str(gameloop_instance.counter))
        widget.button7.setText(str(gameloop_instance.current_player))
        if gameloop_instance.current_player==player1:
            gameloop_instance.current_player=player2
        elif gameloop_instance.current_player==player2:
            gameloop_instance.current_player=player1
        gameloop_instance.SwitchPlayer()
        gameloop_instance.Wincheck()
        widget.button7.setEnabled(False)
        widget.turnsymbol.setText(str(gameloop_instance.current_player))

    def user_input8(self):
        gameloop_instance.counter+=1
        widget.countertext.setText("TURNS : "+str(gameloop_instance.counter))
        widget.button8.setText(str(gameloop_instance.current_player))
        if gameloop_instance.current_player==player1:
            gameloop_instance.current_player=player2
        elif gameloop_instance.current_player==player2:
            gameloop_instance.current_player=player1
        gameloop_instance.SwitchPlayer()
        gameloop_instance.Wincheck()
        widget.button8.setEnabled(False)
        widget.turnsymbol.setText(str(gameloop_instance.current_player))

    def user_input9(self):
        gameloop_instance.counter+=1
        widget.countertext.setText("TURNS : "+str(gameloop_instance.counter))
        widget.button9.setText(str(gameloop_instance.current_player))
        if gameloop_instance.current_player==player1:
            gameloop_instance.current_player=player2
        elif gameloop_instance.current_player==player2:
            gameloop_instance.current_player=player1
        gameloop_instance.SwitchPlayer()
        gameloop_instance.Wincheck()
        widget.button9.setEnabled(False)
        widget.turnsymbol.setText(str(gameloop_instance.current_player))

    def SwitchPlayer(self):
        if self.current_player == 1:
            self.current_player = 0
        elif self.current_player == 0:
            self.current_player = 1  

    def current_player(self):
        Player_current= self.playerlist[self.current_player]
        return Player_current      

    def Wincheck(self):
        for i in range(1,8,3):
            if getattr(widget,"button"+str(i)).text() == getattr(widget,"button"+str(i+1)).text() == getattr(widget,"button"+str(i+2)).text() and getattr(widget,"button"+str(i)).text():
                if getattr(widget,"button"+str(i)).text() == getattr(widget,"button"+str(i+1)).text() == getattr(widget,"button"+str(i+2)).text() and getattr(widget,"button"+str(i)).text() == None:
                    pass
                else:
                    widget.wintext.setText(str(getattr(widget,"button"+str(i)).text())+" WINS")
                    widget.reseter.setVisible(True)
                    widget.countertext.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    widget.turnsymbol.setVisible(False)
        
        for i in range(1,4):
            if getattr(widget,"button"+str(i)).text() == getattr(widget,"button"+str(i+3)).text() == getattr(widget,"button"+str(i+6)).text() and getattr(widget,"button"+str(i)).text():
                    if getattr(widget,"button"+str(i)).text() == getattr(widget,"button"+str(i+3)).text() == getattr(widget,"button"+str(i+6)).text() and getattr(widget,"button"+str(i)).text() == None:
                        pass
                    else:
                        widget.wintext.setText(str(getattr(widget,"button"+str(i)).text())+" WINS")
                        widget.reseter.setVisible(True)
                        widget.countertext.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        widget.turnsymbol.setVisible(False)

            if widget.button1.text() == widget.button5.text() == widget.button9.text() and widget.button1.text():
                if widget.button1.text() == widget.button5.text() == widget.button9.text() and widget.button1.text() == None:
                    pass
                else:
                    widget.wintext.setText(str(widget.button1.text())+" WINS")
                    widget.reseter.setVisible(True)
                    widget.countertext.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    widget.turnsymbol.setVisible(False)

        if widget.button3.text() == widget.button5.text() == widget.button7.text() and widget.button3.text():
            if widget.button3.text() == widget.button5.text() == widget.button7.text() and widget.button3.text() == None:
                pass
            else:
                widget.wintext.setText(str(widget.button3.text())+" WINS")
                widget.reseter.setVisible(True)
                widget.countertext.setAlignment(Qt.AlignmentFlag.AlignCenter)
                widget.turnsymbol.setVisible(False)

    def Reset(self):
        gameloop_instance.current_player==random.choice(seq=(player1,player2))
        gameloop_instance.counter=0
        for i in range(1,10):
            getattr(widget,"button"+str(i)).setEnabled(True)
            getattr(widget,"button"+str(i)).setText(None)
        widget.wintext.setText(None)
        widget.countertext.setText("TURNS : "+str(gameloop_instance.counter))
        widget.reseter.setVisible(False)
        widget.countertext.setAlignment(Qt.AlignmentFlag.AlignLeft)
        widget.turnsymbol.setVisible(True)

gameloop_instance=Hideogame(random.choice(seq=(player1,player2)))

class GUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.layout=QtWidgets.QGridLayout(self)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.wintext=QtWidgets.QLabel("")
        self.wintext.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.wintext.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.wintext,9,4)
        
        self.countertext=QtWidgets.QLabel("TURNS : "+str(gameloop_instance.counter))
        self.layout.addWidget(self.countertext,9,2)
        self.countertext.setAlignment(Qt.AlignmentFlag.AlignLeft)
        
        for i in range(1,10):
            setattr(self,"button"+str(i),QtWidgets.QPushButton(None))
        nb = 0
        for i in range(2,5):
            for j in range(2,5):
                nb+=1
                self.layout.addWidget(getattr(self,"button"+str(nb)),i,j)
                getattr(self,"button"+str(nb)).setMinimumSize(200,200)
                getattr(self,"button"+str(nb)).setStyleSheet("font: 50pt")
        for i in range(1,10):
            getattr(self,"button"+str(i)).clicked.connect(getattr(Hideogame,"user_input"+str(i)))
        
        self.reseter=QtWidgets.QPushButton("RESET")
        self.layout.addWidget(self.reseter,9,3)
        self.reseter.clicked.connect(Hideogame.Reset)
        self.reseter.setMinimumSize(100,10)
        self.reseter.setVisible(False)

        self.turnsymbol=QtWidgets.QLabel(str(gameloop_instance.current_player))
        self.turnsymbol.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.layout.addWidget(self.turnsymbol,9,4)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = GUI()
    widget.resize(100,100)
    widget.show()

    sys.exit(app.exec())