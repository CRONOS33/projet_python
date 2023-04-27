###Création classe Pile File car demandé par CRONOS et Aeraphal
#Date de création:14/01/2022 .Dernière modification:23/01/2022

#classe pile type FIFO
class Pile:

    def __init__(self):
        self.valeur =[]
    
    def empiler(self,valeur):
        self.valeur.append(valeur)
    
    def estvide(self):
        return self.valeur == []

    def depile(self):
        if not(self.estvide):
            return self.valeur.pop()
        else:
            print("la fonction est vide")


#classe File type FIlSO
class File:
    def __init__(self):
        self.valeur =[]
    
    def enfiler(self,valeur):
        self.valeur=[valeur]+self.valeur
    
    def estvide(self):
        return self.valeur == []

    def defile(self):
        if not(self.estvide()):
            return self.valeur.pop(0)
        else:
            print("la fonction est vide")