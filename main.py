class Joueur :
    def __init__(self, nom, symbole):
        self.nom = nom
        self.symbole = symbole

    def __str__(self):
        return self.nom + ":"+ self.symbole

class Case:

    def __init__(self,position,valeur):
        self.position=position
        self.valeur=valeur

    def __str__(self):
        if self.valeur!= None:
            return self.valeur
        else:
            return str(self.position)

    def __str__(self):
        if self.valeur!= None:
            return str(self.valeur)
        else:
            return str(self.position)



class Grille:

    def __init__(self):
        self.grille= [Case(0,None),Case(1,None),Case(2,None),Case(3,None),Case(4,None),Case(5,None),Case(6,None),Case(7,None),Case(8,None)]

    def estVide(self,pos):
        return self.grille[pos].valeur==None

    def joue(self,pos):
        self.grille[pos].valeur= Player.symbole


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

def jeu_entier(self):
        while gagnant == None or egalite :
            self.tours()
        if gagnant :
            print(f"Bravo ! {joueurActuel}, vous avez gagné ! ")
        elif egalite :
            print("Egalite !")
        else :
            self.joueur_suivant()

class HideoGame:
    def __init__(self,players,current_p,rounds):
        self.players=Player
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

    def __str__(self):
        printout=str(Grid())
        return printout

test=HideoGame(2,0,1)
testp=Player("John","X")
tab=[]
testg=Grid(tab)
print(test)