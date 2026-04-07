# FONCTIONS
def rendu_glouton(somme, pieces):
    nb_pieces = 0
    i = 0
    while somme > 0 and i < len(pieces):
        if pieces[i] > somme:
            i = i + 1
        else:
            somme = somme - pieces[i]
            nb_pieces = nb_pieces + 1
    return nb_pieces

def rendu_recursif(somme, pieces):
    if somme == 0:
        return 0

    mini = somme
    for p in pieces:
        if p <= somme:
            nb = 1 + rendu_recursif(somme - p, pieces)
            if nb < mini:
                mini = nb
    return mini

def rendu_recursif_dyn(somme, pieces, memo = []):
    if memo == []:
        memo = [None for _ in range(somme+1)]

    if somme == 0:
        return 0
    
    if ..... != .....:
        return .....
    
    mini = somme
    for p in pieces:
        if p <= somme:
            nb = .....
            if nb < mini:
                mini = .....
                ..... = nb
    return .....

def rendu_ite_dyn(somme, pieces):
    memo = [0]
    for s in range(1, somme+1):
        ........
        for p in pieces:
            if p <= s:
                ........
    return ........


# SCRIPT
euro = [50, 20, 10, 5, 2, 1]
imperial = [30, 24, 12, 6, 3, 1]

assert rendu_glouton(48, euro) == 5
assert rendu_glouton(48, imperial) == 3

# Ces appels sont commentés car ils prennent trop de temps
# assert rendu_recursif(48, euro) == 5
# assert rendu_recursif(48, imperial) == 2
assert rendu_recursif(6, euro) == 2

assert rendu_recursif_dyn(48, euro) == 5
assert rendu_recursif_dyn(48, imperial) == 2
assert rendu_recursif_dyn(6, euro) == 2

assert rendu_ite_dyn(48, euro) == 5
assert rendu_ite_dyn(48, imperial) == 2
assert rendu_ite_dyn(6, euro) == 2



# ********************** n = 5 ***************************
# *** fibo_rec : 0.0 s***
# *** fibo_rec_memo : 0.0 s***
# *** fibo_ite_memo : 0.0 s***
# 
# ********************** n = 20 ***************************
# *** fibo_rec : 0.0 s***
# *** fibo_rec_memo : 0.0 s***
# *** fibo_ite_memo : 0.0 s***
# 
# ********************** n = 30 ***************************
# *** fibo_rec : 0.15 s***
# *** fibo_rec_memo : 0.0 s***
# *** fibo_ite_memo : 0.0 s***
# 
# ********************** n = 50 ***************************
# *** fibo_rec : 2218.25 s***
# *** fibo_rec_memo : 0.0 s***
# *** fibo_ite_memo : 0.0 s***
