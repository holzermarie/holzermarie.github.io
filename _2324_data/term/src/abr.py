# IMPORTS


# CLASS

class ABR:
    def __init__(self, racine):
        """ ABR(Noeud) -> ABR
        Classe représentant un arbre binaire de recherche (ABR)"""
        self.racine = racine
        
    def rechercher(self, cle):
        """ rechercher(type(cle)) -> bool
        Recherche une clé dans l'ABR. La clé peut avoir un type différent d'un ABR à un autre."""
        pass
            
    def inserer(self, cle):
        """ inserer(type(cle)) -> None
        Insère une clé dans l'ABR. La clé peut avoir un type différent d'un ABR à un autre."""
        pass

# SCRIPT

# Construction de l'arborescence de nœuds
racine = Noeud(9)
# ... À COMPLÉTER

log(racine)
display(racine)

# Initialisation de l'ABR

abr = ABR(racine)

# Tests recherche
assert abr.rechercher(11)
assert not abr.rechercher(14)

# Tests insertion
assert not abr.rechercher(7)
abr.inserer(7)
assert abr.rechercher(7)
