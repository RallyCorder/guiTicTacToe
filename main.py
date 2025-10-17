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

class Jeu :
    def __init__(self):
        self.listeJoueurs = listeJoueurs #a def dans le jeu
        self.plateau = Grille()
        self.joueurActuel = joueurActuel #same
        self.compteur = 0

    def joueur_actuel(self):
        Player= self.listeJoueurs[joueurActuel]
        return Player

    def SwitchPlayer(self,joueurActuel):
        if joueurActuel == 1:
            joueurActuel = 0
        if joueurActuel == 0:
            joueurActuel = 1

    def tours(self):
        print(self.plateau)
        casechoisie = input("Ecrit un nombre entre 1 et 9")-1
        while self.grille.estVide(casechoisie):
            print("La case choisie est déjà prise, choisissez une autre case")
            casechoisie = input("Ecrit un nombre entre 1 et 9")-1
        self.joue(casechoisie)
        self.compteur+=1

    def jeu_entier(self):
        J1=Joueur("Jean","X")
        J2=Joueur("Bris","O")
        listeJoueurs=[J1,J2]
        joueurActuel=0
        while gagnant == None or egalite :
            self.tours()
        if gagnant :
            print(f"Bravo ! {joueurActuel}, vous avez gagné ! ")
        elif egalite :
            print("Egalite !")
        else :
            self.joueur_suivant()

def jeu_entier(self):
        while gagnant == None or egalite :
            self.tours()
        if gagnant :
            print(f"Bravo ! {joueurActuel}, vous avez gagné ! ")
        elif egalite :
            print("Egalite !")
        else :
            self.joueur_suivant()