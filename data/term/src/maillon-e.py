# CLASSES
class Maillon:

    def __init__(self, valeur, suivant = None):
        """ Maillon(obj) 
            renvoie un maillon contenant l'élément valeur """
        self.valeur = valeur
        self.suivant = suivant


# FONCTIONS
def longueur(lst):
    """ longueur(Maillon) -> int
        renvoie le nombre de maillons de la liste lst"""
    # à l'aide d'un algorithme récursif
    if lst is None:
        return 0
    
    return 1 + longueur(lst.suivant)

def longueur_it(lst):
    """ longueur(Maillon) -> int
        renvoie le nombre de maillons de la liste lst"""
    # à l'aide d'un algorithme itératif
    pass


def nieme_element(n, lst):
    """ nieme_element(int, Maillon) -> obj
    renvoie la valeur du n-ième élément de la liste lst
    les éléments sont numérotés à partir de 0"""


def concatener(lst1, lst2):
    """ concatener(Maillon, Maillon) -> Maillon
    concatène les listes lst1 et lst2 sous la forme d'une nouvelle liste """


def renverser(lst):
    """renverser(Maillon) -> Maillon
    inverse l'ordre de la liste dans une nouvelle liste"""

    
# SCRIPT

lst = Maillon(1, Maillon(2, Maillon(3, Maillon(4))))
assert longueur(lst) == 4
assert longueur_it(lst) == 4
assert nieme_element(2, lst) == 3

lst_bis = Maillon(4, Maillon(5, Maillon(6, Maillon(7))))
lst_total = concatener(lst, lst_bis)
assert longueur(lst_total) == longueur(lst) + longueur(lst_bis)

lst_envers = renverser(lst)
assert longueur(lst) == longueur(lst_envers)
assert nieme_element(0, lst) == nieme_element(3, lst_envers)
assert nieme_element(3, lst) == nieme_element(0, lst_envers)
