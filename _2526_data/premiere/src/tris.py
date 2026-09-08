# IMPORTS
from random import randint
from time import time_ns

# FONCTIONS

def tri_par_selection(tab):
    pass

def tri_par_insertion(tab):
    pass

def tableau_au_hasard(n):
    pass

# SCRIPT

# Exercice 2) ------------------------------------------------------------------------
tab = [9, 7, 1, 4, -2, 0, 8, 3]
tri_par_selection(tab)
print(tab) # doit afficher [-2, 0, 1, 3, 4, 7, 8, 9]

tab = [2, 6, 7, -2, 0, -5, 1]
tri_par_selection(tab)
print(tab) # doit afficher [-5, -2, 0, 1, 2, 6, 7]


# Exercice 4) ------------------------------------------------------------------------
tab = [9, 7, 1, 4, -2, 0, 8, 3]
tri_par_insertion(tab)
print(tab) # doit afficher [-2, 0, 1, 3, 4, 7, 8, 9]

tab = [2, 6, 7, -2, 0, -5, 1]
tri_par_insertion(tab)
print(tab) # doit afficher [-5, -2, 0, 1, 2, 6, 7]


# Exercice 6/ 1) ------------------------------------------------------------------------
tab = tableau_au_hasard(10**3)
# print(tab)


# Exercice 6/ 2) a) ------------------------------------------------------------------------

# À COMPLÉTER
# ...

temps_tri_par_insertion = 0 # À CHANGER

print("6/ 2) a) Le tri par insertion a pris %.3f secondes." % (temps_tri_par_insertion / (10**9))) # conversion nanosecondes en secondes
# print(tab)


# Exercice 6/ 2) b) ------------------------------------------------------------------------
tab = tableau_au_hasard(10**3)
# print(tab)

# À COMPLÉTER
# ...

temps_sort_python = 0  # À CHANGER
print("      b) Le tri \"sort\" de Python a pris %.3f secondes." % (temps_sort_python / (10**9)))
# print(tab)


# Exercice 6/ 3) ------------------------------------------------------------------------
tab = tableau_au_hasard(10**4)
# print(tab)

# À COMPLÉTER
# ...

temps_tri_par_insertion = 0  # À CHANGER
print("6/ 3) a) Le tri par insertion a pris %.3f secondes." % (temps_tri_par_insertion / (10**9)))
# print(tab)

tab = tableau_au_hasard(10**4)
# print(tab)

# À COMPLÉTER
# ...

temps_sort_python = 0  # À CHANGER
print("       b) Le tri \"sort\" de Python a pris %.3f secondes." % (temps_sort_python / (10**9)))
# print(tab)
