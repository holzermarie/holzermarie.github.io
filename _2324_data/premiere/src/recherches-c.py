# FONCTIONS

def recherche_sequentielle(lst_triee, cible):
    for i in range(len(lst_triee)):
        if cible == lst_triee[i]:
            return i
    return -1

def recherche_dicho(lst_triee, cible):
    ind_gauche = 0
    ind_droit = len(lst_triee) - 1
    
    while ind_gauche <= ind_droit:
        ind_milieu = (ind_droit + ind_gauche) // 2
        elem_milieu = lst_triee[ind_milieu]
        
        if elem_milieu == cible:
            return ind_milieu
        
        if cible < elem_milieu:
            ind_droit = ind_milieu - 1
            
        else:
            ind_gauche = ind_milieu + 1
            
        
    return -1

# SCRIPT

# Initialisation des variables
lst = [1, 4, 10, 14, 21, 30, 76, 78, 99]
valeur_cherchee = 99

print("On cherche %s dans %s :" % (valeur_cherchee, lst))
print("--------")

# Appel de la fonction et stockage du résultat dans res_recherche
res_seq = recherche_sequentielle(lst, valeur_cherchee)
res_dicho = recherche_dicho(lst, valeur_cherchee)

# Affichage « verbeux » du résultat
print("Recherche séquentielle :")
if res_seq == -1:
    print("Cet élément n'est pas dans la liste.")
else:
    print("Élément trouvé à l'indice %s" % res_seq)
    
print("--------")
    
print("Recherche dichotomique :")
if res_dicho == -1:
    print("Cet élément n'est pas dans la liste.")
else:
    print("Élément trouvé à l'indice %s" % res_dicho)