# FONCTIONS
def calcule_table_derniere_occurrence(chaine):
    table_derniere_occurrence = {}
    for j in range(len(chaine)):
        table_derniere_occurrence[chaine[j]] = j
    return table_derniere_occurrence

def correspondance(sequence, motif, idx_sequence, table_derniere_occurrence):
    """ ......... """
    pass

def recherche_bmh(sequence, motif):
    table_derniere_occurrence = calcule_table_derniere_occurrence(motif)
    idx_sequence = 0
    while idx_sequence + len(motif) <= len(sequence):
        decalage = correspondance(sequence, motif, idx_sequence, table_derniere_occurrence)
        # si on a trouvé le motif à l'indice idx_sequence de la séquence :
        if decalage == 0:
            return idx_sequence
        idx_sequence = idx_sequence + decalage
    return -1

# SCRIPT
assert calcule_table_derniere_occurrence("HELLO") == {'H': 0, 'E': 1, 'L': 3, 'O': 4}

assert recherche_bmh('abracadabra', 'dab') == 6
assert recherche_bmh('abracadabra', 'abra') == 0
assert recherche_bmh('abracadabra', 'obra') == -1
assert recherche_bmh('abracadabra', 'bara') == -1
assert recherche_bmh('maman est là', 'maman') == 0
assert recherche_bmh('bonjour maman', 'maman') == 8
assert recherche_bmh('bonjour maman', 'papa') == -1

