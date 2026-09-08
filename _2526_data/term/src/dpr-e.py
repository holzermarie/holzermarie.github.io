def fusion_it(lst1, lst2):
    taille1 = len(lst1)
    taille2 = len(lst2)
    lst_trie = []
    i1 = 0
    i2 = 0
    while (i1 < taille1) and (............):
        if lst1[i1] < lst2[i2]:
            lst_trie.append(............[i1])
            i1 = ............
        else:
            lst_trie.append(lst2[............])
            i2 = ............
    while i1 < taille1:
        lst_trie.append(............)
        i1 = ............
    while i2 < taille2:
        lst_trie.append(............)
        ............
    return lst_trie

def fusion_rec(lst1,lst2):
    # premier cas de base, pour une valeur triviale de lst1
    if ............ 
        return lst2
    # deuxième cas de base, pour une valeur triviale de lst2
    elif ............ 
        return lst1
    elif lst1[0] < lst2[0]:
        # on place le bon élément en premier
        return [............] + fusion_rec(............, ............)    
    else:
        return [............] + fusion_rec(............, ............)
    
def tri_fusion(lst):

    if ....................     # cas de base
        return lst
    else:
        # on coupe le tableau en deux sous-tableaux
        lst1 = [lst[i] for i in range(............)]
        lst2 = [lst[i] for i in range(............)]

    return fusion_rec(tri_fusion(............), tri_fusion(............))