# FONCTIONS
def calcule_table_derniere_occurrence(chaine):
    table_derniere_occurrence = {}
    for j in range(len(chaine)):
        table_derniere_occurrence[chaine[j]] = j
    return table_derniere_occurrence

def correspondance(sequence, motif, idx_sequence, table_derniere_occurrence):
    """correspondance(str, str, int, dict) -> int
    Calcule le décalage à appliquer pour faire correspondre deux lettre de sequence et motif"""
    for idx_motif in range(len(motif)-1,-1, -1): # recule dans le motif
        lettre_sequence = sequence[idx_sequence + idx_motif]
        if lettre_sequence != motif[idx_motif]:
            if lettre_sequence not in table_derniere_occurrence.keys():
                # on décale le motif juste après la lettre courante de la séquence :
                return idx_motif + 1 
            # sinon la lettre de la séquence est dans le motif et on les fait coïncider,
            # mais si ça fait reculer ou stagner, on préfère juste avancer de 1
            return max(idx_motif - table_derniere_occurrence[lettre_sequence], 1)
    return 0 # on a trouvé la correspondance

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

