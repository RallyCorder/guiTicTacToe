class Player:
    def __init__(self,name,symbol):
        self.name=name
        self.symbol=symbol
    def __str__(self):
        printout=str(self.name) + ", " + str(self.symbol)
        return printout

#Me=Player("John","X")
#print(Me)

class Box:
    def __init__(self,position,value):
        self.position=position
        self.value=value
    def __str__(self):
        if self.value == None:
            return " "
        else:
            return self.value

#Cell=Box(9,"X")
#print(Cell)
#a = Box((1,1), "X")

class Grid:
    def __init__(self,table):
        self.table=table
    def BoxCheck(self, box):
        if box.value == None:
            return None
        else:
            return box.value
    def BoxChange(self, box, newvalue):
        if self.BoxCheck(box) == None:
            box.value = newvalue
    def WinnerCheck(self):
        for i in range(3):
            if self.table[i][0].value == self.table[i][1].value == self.table[i][2].value and self.table[i][0] != None:
                return self.table[i][0].value + "is a Winner"
        for i in range(3):
            if self.table[0][i].value == self.table[1][i].value == self.table[2][i].value and self.table[0][i] != None:
                return self.table[0][i].value + "is a Winner"
        if self.table[0][0].value == self.table[1][1].value == self.table[2][2].value and self.table[0][0] != None:
                return self.table[0][0].value + "is a Winner"
        if self.table[0][2].value == self.table[1][1].value == self.table[2][0].value and self.table[0][0] != None:
                return self.table[0][0].value + "is a Winner"

    def __str__(self):
        printout = ""
        for i in range(3):
            printout += "|"
            for j in range(3):
                printout += str(self.table[i][j])+"|"
            printout += "\n"


        if Box.value==None:
            Box.value=="  "
        printout="|" + Box.value(Box.position[0]) + "|" + Box.value(Box.position[1]) + "|" + Box.value(Box.position[2]) + "\n"
        printout+="|" + Box.value(Box.position[3]) + "|" + Box.value(Box.position[4]) + "|" + Box.value(Box.position[5]) + "\n"
        printout+="|" + Box.value(Box.position[6]) + "|" + Box.value(Box.position[7]) + "|" + Box.value(Box.position[8]) + "\n"
        return printout


#wincheck=Grid("Boris")
#boxes=Box([0,1,2,3,4,5,6,7,8],"X")
#print(wincheck.WinnerCheck("X"))

class HideoGame:
    def __init__(self,players,grid,current_p,rounds):
        self.players=Player()

        self.box_list = []
        for i in range(3):
            tab = []
            for j in range(3):
                tab.append(Box((i,j), None))
            self.box_list.append(tab)
        self.grid=Grid(self.box_list)


        self.current_p=current_p
        self.rounds=rounds
    def GameStart(self):
        self.player.name=input()
        self.player.symbol=input()
        
    def PlayerSymbol(self):
        return current_p(Player.symbol)
    def SwitchPlayer(self,current_p):
        if current_p == 1:
            current_p == 0
        if current_p == 0:
            current_p == 1
        else:
            return "Invalid"
