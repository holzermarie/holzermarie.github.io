# IMPORTS
from random import randint
from time import time_ns

# FONCTIONS

def tri_par_selection(lst):
    for i in range(len(lst)):
        i_min = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[i_min]:
                i_min = j
        lst[i], lst[i_min] = lst[i_min], lst[i]

def tri_par_insertion(lst):
    for i in range(1,len(lst)):
        el_courant = lst[i]
        j = i
        while j > 0  and lst[j-1] > el_courant:
            lst[j] = lst[j-1]
            j = j-1
        lst[j] = el_courant

def liste_au_hasard(n):
    return [randint(1, 10**6) for _ in range(n)]

# SCRIPT

# Exercice 2) ------------------------------------------------------------------------
lst = [9, 7, 1, 4, -2, 0, 8, 3]
tri_par_selection(lst)
print(lst) # doit afficher [-2, 0, 1, 3, 4, 7, 8, 9]
assert lst == [-2, 0, 1, 3, 4, 7, 8, 9]

lst = [2, 6, 7, -2, 0, -5, 1]
tri_par_selection(lst)
print(lst) # doit afficher [-5, -2, 0, 1, 2, 6, 7]

# Exercice 4) ------------------------------------------------------------------------
lst = [9, 7, 1, 4, -2, 0, 8, 3]
tri_par_insertion(lst)
print(lst) # doit afficher [-2, 0, 1, 3, 4, 7, 8, 9]

lst = [2, 6, 7, -2, 0, -5, 1]
tri_par_insertion(lst)
print(lst) # doit afficher [-5, -2, 0, 1, 2, 6, 7]

# Exercice 6/ 1) ------------------------------------------------------------------------
lst = liste_au_hasard(10**3)
# print(lst)

# Exercice 6/ 2) a) ------------------------------------------------------------------------
debut = time_ns()
tri_par_insertion(lst)
fin = time_ns()

temps_tri_par_insertion = fin - debut
print("6/ 2) a) Le tri par insertion a pris %.3f secondes." % (temps_tri_par_insertion / (10**9))) # nanoseconds to seconds
# print(lst)

# Exercice 6/ 2) b) ------------------------------------------------------------------------
lst = liste_au_hasard(10**3)
# print(lst)

debut = time_ns()
lst.sort()
fin = time_ns()

temps_sort_python = fin - debut
print("      b) Le tri \"sort\" de Python a pris %.3f secondes." % (temps_sort_python / (10**9)))
# print(lst)

# Exercice 6/ 3) ------------------------------------------------------------------------
lst = liste_au_hasard(10**4)
# print(lst)

debut = time_ns()
tri_par_insertion(lst)
fin = time_ns()

temps_tri_par_insertion = fin - debut
print("6/ 3) a) Le tri par insertion a pris %.3f secondes." % (temps_tri_par_insertion / (10**9)))
# print(lst)

lst = liste_au_hasard(10**4)
# print(lst)

debut = time_ns()
lst.sort()
fin = time_ns()

temps_sort_python = fin - debut
print("       b) Le tri \"sort\" de Python a pris %.3f secondes." % (temps_sort_python / (10**9)))
# print(lst)
