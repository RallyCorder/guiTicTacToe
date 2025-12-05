import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import Qt, QSize
import csv

leaderboardfile='leaderboard.csv'

class Player:

    def __init__(self,symbol):
        self.symbol=symbol

    def __str__(self):
        return self.symbol

player1=Player("Ж")
player2=Player("𝛀")

class Leaderboard:

    def import_csv(leaderboardfile):
        tab=[]
        with open(leaderboardfile) as csvfile:
            reader=csv.DictReader(csvfile)
            for row in reader:
                tab.append(row)
        return tab

    def add_to_csv(user):
        actuator=False
        for dico in leaderboard:
            if dico["Username"]==user:
                dico["Victories"]=int(dico["Victories"])+1
                actuator=True
        if not actuator:
            leaderboard.append({'Username':user,'Victories':1})

    def export_csv(file,table):
        with open(file, 'w', newline='') as csvfile:
            fields=table[0].keys()
            writer=csv.DictWriter(csvfile, fields)
            writer.writeheader()
            writer.writerows(table)

leaderboard=Leaderboard.import_csv(leaderboardfile)

class Hideogame:

    def __init__(self,current_player):
        self.playerlist=[player1,player2]
        self.current_player=current_player
        self.counter=0
        self.scoreP1=0
        self.scoreP2=0

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
        if self.current_player==1:
            self.current_player=0
        elif self.current_player==0:
            self.current_player=1  

    def current_player(self):
        Player_current=self.playerlist[self.current_player]
        return Player_current      

    def Wincheck(self):
        for i in range(1,8,3):
            if getattr(widget,"button"+str(i)).text()==getattr(widget,"button"+str(i+1)).text()==getattr(widget,"button"+str(i+2)).text() and getattr(widget,"button"+str(i)).text():
                if getattr(widget,"button"+str(i)).text()==getattr(widget,"button"+str(i+1)).text()==getattr(widget,"button"+str(i+2)).text() and getattr(widget,"button"+str(i)).text()==None:
                    pass
                else:
                    self.player2nametext=widget.player2name.toPlainText()
                    self.player1nametext=widget.player1name.toPlainText()
                    widget.reseter.setVisible(True)
                    widget.countertext.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    widget.turnsymbol.setVisible(False)
                    if getattr(widget,"button"+str(i)).text()==player1.symbol:
                        gameloop_instance.scoreP1+=1
                    if getattr(widget,"button"+str(i)).text()==player2.symbol:
                        gameloop_instance.scoreP2+=1
                    widget.scoreshow.setText(str(gameloop_instance.scoreP1)+" - "+str(gameloop_instance.scoreP2))
                    if getattr(widget,"button"+str(i)).text()==player1.symbol and self.player1nametext !=None:
                        widget.wintext.setText(str(self.player1nametext)+" WINS")
                        if widget.wintext.text()==" WINS":
                            widget.wintext.setText("Ж WINS")
                            Leaderboard.add_to_csv("Ж")
                            Leaderboard.export_csv(leaderboardfile, leaderboard)
                        else:
                            Leaderboard.add_to_csv(str(self.player1nametext))
                            Leaderboard.export_csv(leaderboardfile, leaderboard)
                    if getattr(widget,"button"+str(i)).text()==player2.symbol and self.player2nametext !=None:
                        widget.wintext.setText(str(self.player2nametext)+" WINS")  
                        if widget.wintext.text()==" WINS":
                            widget.wintext.setText("𝛀 WINS")
                            Leaderboard.add_to_csv("𝛀")
                            Leaderboard.export_csv(leaderboardfile, leaderboard)
                        else:
                            Leaderboard.add_to_csv(str(self.player2nametext))
                            Leaderboard.export_csv(leaderboardfile, leaderboard)
                        
        for i in range(1,4):
            if getattr(widget,"button"+str(i)).text()==getattr(widget,"button"+str(i+3)).text()==getattr(widget,"button"+str(i+6)).text() and getattr(widget,"button"+str(i)).text():
                    if getattr(widget,"button"+str(i)).text()==getattr(widget,"button"+str(i+3)).text()==getattr(widget,"button"+str(i+6)).text() and getattr(widget,"button"+str(i)).text()==None:
                        pass
                    else:
                        self.player2nametext=widget.player2name.toPlainText()
                        self.player1nametext=widget.player1name.toPlainText()
                        widget.reseter.setVisible(True)
                        widget.countertext.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        widget.turnsymbol.setVisible(False)
                        if getattr(widget,"button"+str(i)).text()==player1.symbol:
                            gameloop_instance.scoreP1+=1
                        if getattr(widget,"button"+str(i)).text()==player2.symbol:
                            gameloop_instance.scoreP2+=1
                        widget.scoreshow.setText(str(gameloop_instance.scoreP1)+" - "+str(gameloop_instance.scoreP2))
                        if getattr(widget,"button"+str(i)).text()==player1.symbol and self.player1nametext !=None:
                            widget.wintext.setText(str(self.player1nametext)+" WINS")
                            if widget.wintext.text()==" WINS":
                                widget.wintext.setText("Ж WINS")
                                Leaderboard.add_to_csv("Ж")
                                Leaderboard.export_csv(leaderboardfile, leaderboard)
                            else:
                                Leaderboard.add_to_csv(str(self.player1nametext))
                                Leaderboard.export_csv(leaderboardfile, leaderboard)
                        elif getattr(widget,"button"+str(i)).text()==player2.symbol and self.player2nametext !=None:
                            widget.wintext.setText(str(self.player2nametext)+" WINS")
                            if widget.wintext.text()==" WINS":
                                widget.wintext.setText("𝛀 WINS")
                                Leaderboard.add_to_csv("𝛀")
                                Leaderboard.export_csv(leaderboardfile, leaderboard)
                            else:
                                Leaderboard.add_to_csv(str(self.player2nametext))
                                Leaderboard.export_csv(leaderboardfile, leaderboard)

            if widget.button1.text()==widget.button5.text()==widget.button9.text() and widget.button1.text():
                if widget.button1.text()==widget.button5.text()==widget.button9.text() and widget.button1.text()==None:
                    pass
                else:
                    self.player2nametext=widget.player2name.toPlainText()
                    self.player1nametext=widget.player1name.toPlainText()
                    widget.reseter.setVisible(True)
                    widget.countertext.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    widget.turnsymbol.setVisible(False)
                    if getattr(widget,"button"+str(i)).text()==player1.symbol:
                        gameloop_instance.scoreP1+=1
                    if getattr(widget,"button"+str(i)).text()==player2.symbol:
                        gameloop_instance.scoreP2+=1
                    widget.scoreshow.setText(str(gameloop_instance.scoreP1)+" - "+str(gameloop_instance.scoreP2))
                    if getattr(widget,"button"+str(i)).text()==player1.symbol and self.player1nametext !=None:
                        widget.wintext.setText(str(self.player1nametext)+" WINS")
                        if widget.wintext.text()==" WINS":
                            widget.wintext.setText("Ж WINS")
                            Leaderboard.add_to_csv("Ж")
                            Leaderboard.export_csv(leaderboardfile, leaderboard)
                        else:
                            Leaderboard.add_to_csv(str(self.player1nametext))
                            Leaderboard.export_csv(leaderboardfile, leaderboard)
                    elif getattr(widget,"button"+str(i)).text()==player2.symbol and self.player2nametext !=None:
                        widget.wintext.setText(str(self.player2nametext)+" WINS")  
                        if widget.wintext.text()==" WINS":
                            widget.wintext.setText("𝛀 WINS")
                            Leaderboard.add_to_csv("𝛀")
                            Leaderboard.export_csv(leaderboardfile, leaderboard) 
                        else:
                            Leaderboard.add_to_csv(str(self.player2nametext))
                            Leaderboard.export_csv(leaderboardfile, leaderboard)
                        
        if widget.button3.text()==widget.button5.text()==widget.button7.text() and widget.button3.text():
            if widget.button3.text()==widget.button5.text()==widget.button7.text() and widget.button3.text()==None:
                pass
            else:
                self.player2nametext=widget.player2name.toPlainText()
                self.player1nametext=widget.player1name.toPlainText()
                widget.reseter.setVisible(True)
                widget.countertext.setAlignment(Qt.AlignmentFlag.AlignCenter)
                widget.turnsymbol.setVisible(False)
                if getattr(widget,"button"+str(i)).text()==player1.symbol:
                    gameloop_instance.scoreP1+=1
                if getattr(widget,"button"+str(i)).text()==player2.symbol:
                    gameloop_instance.scoreP2+=1
                widget.scoreshow.setText(str(gameloop_instance.scoreP1)+" - "+str(gameloop_instance.scoreP2))
                if getattr(widget,"button"+str(i)).text()==player1.symbol and self.player1nametext !=None:
                    widget.wintext.setText(str(self.player1nametext)+" WINS")
                    if widget.wintext.text()==" WINS":
                        widget.wintext.setText("Ж WINS")
                        Leaderboard.add_to_csv("Ж")
                        Leaderboard.export_csv(leaderboardfile, leaderboard)
                    else:
                        Leaderboard.add_to_csv(str(self.player1nametext))
                        Leaderboard.export_csv(leaderboardfile, leaderboard)
                elif getattr(widget,"button"+str(i)).text()==player2.symbol and self.player2nametext !=None:
                    widget.wintext.setText(str(self.player2nametext)+" WINS")  
                    if widget.wintext.text()==" WINS":
                        widget.wintext.setText("𝛀 WINS")
                        Leaderboard.add_to_csv("𝛀")
                        Leaderboard.export_csv(leaderboardfile, leaderboard) 
                    else:
                        Leaderboard.add_to_csv(str(self.player2nametext))
                        Leaderboard.export_csv(leaderboardfile, leaderboard)

        if gameloop_instance.counter==9:
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
        nb=0
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

        self.player1name=QtWidgets.QTextEdit()
        self.player1name.setPlaceholderText("Player Ж")
        self.layout.addWidget(self.player1name,0,2)
        self.player1name.setMaximumSize(200,30)
        self.player1name.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.player1name.setTabChangesFocus(True)

        self.player2name=QtWidgets.QTextEdit()
        self.player2name.setPlaceholderText("Player 𝛀")
        self.layout.addWidget(self.player2name,0,4)
        self.player2name.setMaximumSize(200,30)
        self.player2name.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.player2name.setTabChangesFocus(True)
        
        self.scoreshow=QtWidgets.QLabel(str(gameloop_instance.scoreP1)+" - "+str(gameloop_instance.scoreP2))
        self.layout.addWidget(self.scoreshow,0,3)
        self.scoreshow.setAlignment(Qt.AlignmentFlag.AlignCenter)

app=QtWidgets.QApplication([])
widget=GUI()
widget.setMaximumSize(650,700)
widget.setMinimumSize(650,700)
widget.show()
sys.exit(app.exec())