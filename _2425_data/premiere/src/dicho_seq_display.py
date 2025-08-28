# IMPORTS

import timeit
import matplotlib.pyplot as plt

# FONCTIONS

# Recherche séquentielle
def recherche_seq(liste_triee, cible):
    # COMPLÉTER ICI
    # ...
    return -1

# Recherche dichotomique
def recherche_dicho(liste_triee, cible):
    # COMPLÉTER ICI
    # ...
    return -1

# Mesure du temps d'exécution
def temps_exec(nb_donnees, fct_etudiee):
    """
    Fonction qui calcule le temps d'exécution moyen de la fonction fct_etudiee
    param nb_donnees : entier positif ou nul, représentant la longueur du tableau étudié
    param fct_etudiee : nom de la fonction (comme si on l'appelait sans paramètres et sans parenthèses donc)
    return : flottant - temps moyen d'exécution de fct_etudiee
    """
    # Création d'un tableau de longueur nb_donnees rempli de 0
    lst = [0 for _ in range(nb_donnees)]
    # Mesure du temps d'exécution
    temps = timeit.Timer(lambda : fct_etudiee(lst, 42))
    # Répétition de 500 exécutions et récupération du temps le plus faible.
    return min(temps.repeat(repeat=100, number=1))

# SCRIPT

# TESTS (NE PAS CHANGER LES TESTS, ILS DOIVENT FONCTIONNER !)
assert recherche_seq(lst, valeur_cherchee) == 8
assert recherche_dicho(lst, valeur_cherchee) == 8

valeur_cherchee = 14
assert recherche_seq(lst, valeur_cherchee) == 3
assert recherche_dicho(lst, valeur_cherchee) == 3

valeur_cherchee = 8888
assert recherche_seq(lst, valeur_cherchee) == -1
assert recherche_dicho(lst, valeur_cherchee) == -1
# FIN TESTS

# AFFICHAGE
lst_tailles_donnees = [x for x in range(0, 200, 10) ]
res_dicho = [temps_exec(t, recherche_dicho) for t in lst_tailles_donnees]
res_seq = [temps_exec(t, recherche_seq) for t in lst_tailles_donnees]

plt.plot(lst_tailles_donnees, res_dicho, 'ro', lst_tailles_donnees, res_dicho, 'r', lst_tailles_donnees, res_seq, 'g^', lst_tailles_donnees, res_seq, 'g')
plt.xlabel('Taille du tableau')
plt.ylabel('Temps d\'exécution')

# plt.show()
# FIN AFFICHAGE

