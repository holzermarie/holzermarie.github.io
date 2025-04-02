# FONCTIONS
def compte_occurrences(chaine):
    dico_occur = {}
    for carac in chaine:
        if carac not in dico_occur.keys(): # ou dico_occur tout court
            dico_occur[carac] = 0
        dico_occur[carac] += 1
    return dico_occur

# SCRIPT
assert compte_occurrences("bonjour") == {'b': 1, 'o': 2, 'n': 1, 'j': 1, 'u': 1, 'r': 1}
assert compte_occurrences("ratatouille") == {'r': 1, 'a': 2, 't': 2, 'o': 1, 'u': 1, 'i': 1, 'l': 2, 'e': 1}