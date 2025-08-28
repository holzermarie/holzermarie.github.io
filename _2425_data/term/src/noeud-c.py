# IMPORTS
from displayer import display, log
from file import *
from pile import *

# CLASS
class Noeud :

    def __init__(self, val):
        """ Construit un noeud d'étiquette val sans sous-arbre """
        self.etiquette = val
        self.sag = None # sous-arbre gauche
        self.sad = None # sous-arbre droit
    
    # sert pour l'affichage
    def get_value(self):
        return self.etiquette
    
    # sert pour l'affichage
    def get_children(self):
        return [c for c in (self.sag, self.sad) if c]

    def taille(self):
        return 1 + (self.sag.taille() if self.sag is not None else 0) + \
               (self.sad.taille() if self.sad is not None else 0)

#     def taille(self):
#         taille_g = 0 if self.sag == None else self.sag.taille()
#         taille_d = 0 if self.sad == None else self.sad.taille()
#         return 1 + taille_g + taille_d

#     def taille(self):
#         taille_g = 0
#         taille_d = 0
# 
#         if self.sag != None:
#             taille_g = self.sag.taille()
#         if self.sad != None:
#             taille_d = self.sad.taille()
# 
#         return 1 + taille_g + taille_d


#     def taille(self):
#         # cas de base, si c'est une feuille
#         if self.sag == None and self.sad == None:
#             return 1
#       
#         # si une seule branche
#         if self.sag == None:
#             return 1 + self.sad.taille()
#         if self.sad == None:
#             return 1 + self.sag.taille()
#       
#         # si deux branches
#         return 1 + self.sad.taille() + self.sag.taille()


#     def hauteur(self):
#         # Cas de base pour la feuille
#         if self.sag == None and self.sad == None:
#             return 0
#         
#         return 1 + max(self.sag.hauteur() if self.sag is not None else 0, \
#                        self.sad.hauteur() if self.sad is not None else 0)

    def hauteur(self):
        hauteur_g = 0
        hauteur_d = 0

        # Cas de base pour la feuille
        if self.sag == None and self.sad == None:
            return 0
        
        if self.sag != None:
            hauteur_g = self.sag.hauteur()
        if self.sad != None:
            hauteur_d = self.sad.hauteur()

        return 1 + max(hauteur_g, hauteur_d)

#     def nb_feuilles(self):
#         # Cas de base pour la feuille
#         if self.sag == None and self.sad == None:
#             return 1
#         return (self.sag.nb_feuilles() if self.sag is not None else 0) + \
#                (self.sad.nb_feuilles() if self.sad is not None else 0) 

    def nb_feuilles(self):
        nb_feuilles_g = 0
        nb_feuilles_d = 0

        # Cas de base pour la feuille
        if self.sag == None and self.sad == None:
            return 1
        
        if self.sag != None:
            nb_feuilles_g = self.sag.nb_feuilles()
        if self.sad != None:
            nb_feuilles_d = self.sad.nb_feuilles()

        return nb_feuilles_g + nb_feuilles_d
        

# FONCTIONS

def parcours_prefixe(noeud):
    if noeud == None:
        return []
    
    return [noeud.etiquette] + parcours_prefixe(noeud.sag) + parcours_prefixe(noeud.sad)

def parcours_infixe(noeud):
    if noeud == None:
        return []
    
    return parcours_infixe(noeud.sag) + [noeud.etiquette] + parcours_infixe(noeud.sad)

def parcours_suffixe(noeud):
    if noeud == None:
        return []
    
    return  parcours_suffixe(noeud.sag) + parcours_suffixe(noeud.sad) + [noeud.etiquette]

def parcours_largeur(racine):
    if racine == None:
        return []
    
    res = []
    file = File()
    file.enfile(racine)
    
    while not file.est_vide():
        noeud = file.defile()
        res.append(noeud.etiquette)
        if noeud.sag != None:
            file.enfile(noeud.sag)
        if noeud.sad != None:
            file.enfile(noeud.sad)
        
    return res
        

def parcours_mystere_2(racine):
    if racine == None:
        return []
    
    res = []
    pile = Pile()
    pile.empile(racine)
    
    while not pile.est_vide():
        noeud = pile.depile()
        res.append(noeud.etiquette)
        if noeud.sad != None:
            pile.empile(noeud.sad)
        if noeud.sag != None:
            pile.empile(noeud.sag)
        
    return res

# SCRIPT

# Ex 5 :
# 1)
racine = Noeud("A")
racine.sag = Noeud("B")
racine.sag.sag = Noeud("C")
racine.sag.sad = Noeud("D")
racine.sag.sad.sag = Noeud("E")
racine.sag.sad.sad = Noeud("F")

# 2) taille et hauteur complétées dans la classe ci-dessus
# print(racine.taille())
assert racine.taille() == 6
assert racine.hauteur() == 3

# Affichages
log(racine)
display(racine)

# 3)
assert racine.nb_feuilles() == 3

## TESTS ##

#
r1 = Noeud("A")
assert r1.taille() == 1
assert r1.hauteur() == 0
assert r1.nb_feuilles() == 1
#
r2 = Noeud("A")
r2.sag = Noeud("B")
assert r2.taille() == 2
assert r2.hauteur() == 1
assert r2.nb_feuilles() == 1
#
r3 = Noeud("A")
r3.sag = Noeud("B")
r3.sad = Noeud("C")
assert r3.taille() == 3
assert r3.hauteur() == 1
assert r3.nb_feuilles() == 2
#
r2 = Noeud("A")
r2.sag = Noeud("B")
r2.sad = Noeud("Z")
r2.sag.sag = Noeud("C")
r2.sag.sag.sag = Noeud("D")
assert r2.taille() == 5
assert r2.hauteur() == 3
assert r2.nb_feuilles() == 2

#  Ex 7 : parcours

racine = Noeud("A")
racine.sag = Noeud("B")
racine.sag.sag = Noeud("C")
racine.sag.sad = Noeud("D")
racine.sag.sad.sag = Noeud("E")
racine.sag.sad.sad = Noeud("F")
racine.sad = Noeud("G")
racine.sad.sag = Noeud("H")

log(racine)

# print(parcours_prefixe(racine))
assert parcours_prefixe(None) == []
assert parcours_prefixe(racine) == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']


# print(parcours_infixe(racine))
assert parcours_infixe(None) == []
assert parcours_infixe(racine) == ['C', 'B', 'E', 'D', 'F', 'A', 'H', 'G']


# print(parcours_suffixe(racine))
assert parcours_suffixe(None) == []
assert parcours_suffixe(racine) == ['C', 'E', 'F', 'D', 'B', 'H', 'G', 'A']

# print(parcours_largeur(racine))
assert parcours_largeur(None) == []
assert parcours_largeur(racine) == ['A', 'B', 'G', 'C', 'D', 'H', 'E', 'F']

# print(parcours_mystere_2(racine))
assert parcours_mystere_2(None) == []
assert parcours_mystere_2(racine) == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
display(racine)