
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



class Jeu :
    def __init__(self):
        self.listeJoueurs =  [Joueur(input("Nom joueur 1:"),"X"),Joueur(input("Nom joueur 2:"),"O")]
        self.plateau = Grille()
        self.joueurActu = 1
        self.compteur = 0


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
        casechoisie= input("Ecrit un nombre entre 1 et 9 ")
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



j=Jeu()
j.jeu_entier()