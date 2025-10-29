class Joueur:

    def __init__(self, nom, symbole):
        self.nom=nom
        self.symbole=symbole

    def __str__(self):
        return self.nom + ":" + self.symbole

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
        self.grille=[Case(0,None),Case(1,None),Case(2,None),Case(3,None),Case(4,None),Case(5,None),Case(6,None),Case(7,None),Case(8,None)]

    def estVide(self,position):
        return self.grille[position].valeur==None

    def SymboleJoueur(self,position):
        self.grille[position].valeur=joueur_id.symbole

    def VerifGagnant(self):
        for i in range(3):
            if self.grille[3*i].valeur == self.grille[3*i+1].valeur == self.grille[3*i+2].valeur != None:
                gagnant = True
            if self.grille[3*i].valeur == self.grille[3*i+3].valeur == self.grille[3*i+6].valeur != None:
                gagnant=True
        if self.grille[0].valeur == self.grille[4].valeur == self.grille[8].valeur != None:
            gagnant=True
        if self.grille[2].valeur == self.grille[4].valeur == self.grille[6].valeur != None:
            gagnant=True

    def __str__(self):
        text=""
        for j in range(0,9,3):
            text+="|"
            for i in range (0,3):
                if self.estVide(j+i):
                    a=" "
                else:
                    a=self.grille[j+i]
                text+=str(a)+"|"
            text+="\n"
        return text

class Jeu:

    def __init__(self):
        self.liste_joueurs=self.JeuEntier #a def dans le jeu
        self.plateau=Grille()
        self.joueur_valeur=self.JeuEntier #same
        self.compteur=0

    def joueurActuel(self):
        joueur_id=self.liste_joueurs[joueur_valeur]
        return joueur_id

    def AlternerJoueurs(self,joueur_valeur):
        if joueur_valeur==1:
            joueur_valeur=0
        if joueur_valeur==0:
            joueur_valeur=1

    def Round(self):
        print(self.plateau)
        case_choisie = input("Ecrit un nombre entre 1 et 9")-1
        while self.grille.estVide(case_choisie):
            print("La case choisie est déjà prise, choisissez une autre case")
            case_choisie = input("Ecrit un nombre entre 1 et 9")-1
        self.SymboleJoueur(case_choisie)
        self.compteur+=1

    def JeuEntier(self):
        J1=Joueur("Jean","X")
        J2=Joueur("Bris","O")
        liste_joueurs=[J1,J2]
        joueur_valeur=0
        while gagnant==None or egalite:
            self.Round()
        if gagnant==True:
            print("Bravo !{joueur_valeur}, vous avez gagné !")
        elif egalite:
            print("Egalite !")
        else:
            self.joueur_suivant()