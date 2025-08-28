# IMPORTS
from noeud2 import *

# CLASS

class ABR:
    
    def __init__(self, racine):
        """ ABR(Noeud) -> ABR
        Classe représentant un arbre binaire de recherche (ABR)"""
        self.racine = racine
        
    def rechercher(self, cle):
        """ rechercher(type(cle)) -> bool
        Recherche une clé dans l'ABR. La clé peut avoir un type différent d'un ABR à un autre."""
        etiquette = self.racine.etiquette
        if cle == etiquette:
            return True
        
        if cle < etiquette:
            if self.racine.sag == None:    # s'il n'y a rien à gauche, la clé n'est pas présente
                return False
            return ABR(self.racine.sag).rechercher(cle)   # on continue de chercher à gauche
        
        if cle > etiquette:
            if self.racine.sad == None:     # s'il n'y a rien à droite, la clé n'est pas présente
                return False
            return ABR(self.racine.sad).rechercher(cle)    # on continue de chercher à droite
            
    def inserer(self, cle):
        """ inserer(type(cle)) -> None
        Insère une clé dans l'ABR. La clé peut avoir un type différent d'un ABR à un autre."""
        etiquette = self.racine.etiquette
        if cle <= etiquette:
            if self.racine.sag == None:   # le sous-arbre gauche est vide, on peut faire l'insertion ici
                self.racine.sag = Noeud(cle)
            else: # on cherche une place pour faire l'insertion à gauche
                ABR(self.racine.sag).inserer(cle)
        else:
            if self.racine.sad == None:    # le sous-arbre droit est vide, on peut faire l'insertion ici
                self.racine.sad = Noeud(cle)
            else:   # on cherche une place pour faire l'insertion à droite
                ABR(self.racine.sad).inserer(cle)

# SCRIPT

racine = Noeud(9)
racine.sag = Noeud(3)
racine.sag.sag = Noeud(2)
racine.sag.sad = Noeud(5)
racine.sad = Noeud(13)
racine.sad.sag = Noeud(11)
racine.sad.sad = Noeud(17)
racine.sad.sad.sad = Noeud(19)

abr = ABR(racine)

# print(abr.rechercher(11))

# Tests recherche
assert abr.rechercher(11)
assert not abr.rechercher(14)

# Tests insertion
assert not abr.rechercher(7)
abr.inserer(7)
assert abr.rechercher(7)

log(racine)

display(racine)