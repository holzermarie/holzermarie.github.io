# Vous trouverez l'énoncé ici : https://e-nsi.gitlab.io/pratique/N1/119-recherche_indices/sujet/

# FONCTIONS
def indices(element, entiers):
    lst_indices = []
    for idx in range(len(entiers)):
        if entiers[idx] == element:
            lst_indices.append(idx)
    return lst_indices

# SCRIPT
lst = [3, 45, 56, 8, 56, 2]
res = indices(56, lst)
print(res) # doit afficher [2, 4]