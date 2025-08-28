# FONCTIONS
def est_numerique(car):
    return ord(car) >= 48 and ord(car) <= 57

def est_une_date_valide(chaine): # chaine de format jj/mm/aaaa
    if len(chaine) != 10:
        return False
    if chaine[2] != "/" or chaine[5] != "/":
        return False
    
    idx = 0
    while idx < 10: # parcourir la chaîne
        if idx != 2 and idx != 5:
            if not est_numerique(chaine[idx]):
                return False
        idx += 1
        
    jour = chaine[0] + chaine[1]
    # teste si jour ok
    if int(jour) < 1 or int(jour) > 31:
        return False
    # teste si mois ok
    mois = chaine[3] + chaine[4]
    if int(mois) < 1 or int(mois) > 12:
        return False
    return True

# SCRIPT
assert est_une_date_valide("16/02/2025")
assert not est_une_date_valide("16-02-2025")
assert not est_une_date_valide("16/13/2025")
assert not est_une_date_valide("toto")