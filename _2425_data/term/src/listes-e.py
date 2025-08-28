# CLASSES

###################################################################
############# COPIER VOTRE CLASSE MAILLON ICI #####################
###################################################################

class Liste:
    
    def __init__(self):
        """ Liste() -> Liste
        crée une liste vide"""
        self.tete = None
        
    def est_vide(self):
        """ est_vide() -> bool
        renvoie True si la liste est vide, False sinon"""
        pass
    
    def ajoute_tete(self, x):
        """ ajoute_tete() -> None
        ajoute un maillon dont la valeur est x en tête de liste"""
        pass
        
    def __len__(self): # permet d'utiliser len(Liste)
        """ len(Liste) -> int
        renvoie la longueur de la liste"""
        pass
    
    def __getitem__(self, n): # permet d'utiliser les crochets Liste[i]
        """ Liste[n] -> obj
        renvoie la valeur du maillon à l'indice n dans la liste"""
        pass
    
    def renverse(self):
        """ renverse() -> None
        inverse (en place) les éléments de la liste (le premier devient le
        dernier, le deuxième l'avant-dernier, etc.)"""
        pass
        
    def __add__(self, lst): # permet d'utiliser + pour concaténer Liste + Liste = Liste
        """ Liste + Liste -> Liste
        concatène deux listes"""
        pass
    
    def __repr__(self): # permet d'utiliser print(Liste)
        """ print(Liste) -> str
        affiche la liste avec des flèches entre chaque élément"""
        chaine = ""
        courant = self.tete
        while courant.suivant is not None:
            chaine += str(courant.valeur)
            chaine += " -> "
            courant = courant.suivant
        chaine += str(courant.valeur)
        chaine += " -> None"
        return chaine

# FONCTIONS

###################################################################
############# COPIER LES FONCTIONS DU FICHIER MAILLON ICI #########
###################################################################

# SCRIPT

liste_vide = Liste()
assert liste_vide.est_vide()


liste = Liste()
liste.ajoute_tete(4)
liste.ajoute_tete(3)
liste.ajoute_tete(2)
liste.ajoute_tete(1)

print(liste)

assert len(liste) == 4
assert liste[1] == 2

liste_bis = Liste()
liste_bis.ajoute_tete(4)
liste_bis.ajoute_tete(3)
liste_bis.ajoute_tete(2)
liste_bis.ajoute_tete(1)
liste_bis.renverse()
assert liste[0] == liste_bis[3]
assert liste[3] == liste_bis[0]

liste_total = liste + liste_bis
assert len(liste_total)