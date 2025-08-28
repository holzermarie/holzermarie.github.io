#  Ex 7 : parcours

racine = Noeud("A")
racine.sag = Noeud("B")
racine.sag.sag = Noeud("C")
racine.sag.sad = Noeud("D")
racine.sag.sad.sag = Noeud("E")
racine.sag.sad.sad = Noeud("F")
racine.sad = Noeud("G")
racine.sad.sag = Noeud("H")

log(racine)

# print(parcours_prefixe(racine))
assert parcours_prefixe(None) == []
assert parcours_prefixe(racine) == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']


# print(parcours_infixe(racine))
assert parcours_infixe(None) == []
assert parcours_infixe(racine) == ['C', 'B', 'E', 'D', 'F', 'A', 'H', 'G']


# print(parcours_suffixe(racine))
assert parcours_suffixe(None) == []
assert parcours_suffixe(racine) == ['C', 'E', 'F', 'D', 'B', 'H', 'G', 'A']

# print(parcours_largeur(racine))
assert parcours_largeur(None) == []
assert parcours_largeur(racine) == ['A', 'B', 'G', 'C', 'D', 'H', 'E', 'F']