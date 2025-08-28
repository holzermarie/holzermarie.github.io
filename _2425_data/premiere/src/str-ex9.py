# FONCTIONS
def affiche_coordonnees(x, y):
    print("Ce point a pour coordonnées (%s ; %s)." % (x, y))
    
# version recommandée aujourd'hui
def affiche_coordonnees_v2(x, y):
    print(f"Ce point a pour coordonnées ({x} ; {y}).")
    
# cette version est affreuse à lire ! Non ?
def affiche_coordonnees_v3(x, y):
    print("Ce point a pour coordonnées (" + str(x) +" ; " + str(y) + ").")
    
# SCRIPT
affiche_coordonnees(3, 5)
affiche_coordonnees_v2(3, 5)
affiche_coordonnees_v3(3, 5)
