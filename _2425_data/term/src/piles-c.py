# IMPORTS
from pile import *

# FONCTIONS

# Ex 2
def echange(p):
    dernier = p.depile()
    avant_dernier = p.depile()
    p.empile(dernier)
    p.empile(avant_dernier)

# Ex 3
def inverse(p):
    p_inverse = Pile()
    p_auxiliaire = Pile()
    while not p.est_vide():
        x = p.depile()
        p_inverse.empile(x)
        p_auxiliaire.empile(x)

    # p est maintenant vide
    # on rempile les éléments de p_auxiliaire sur p
    while not p_auxiliaire.est_vide():        
        p.empile(p_auxiliaire.depile())
        
    return p_inverse

# Ex 4
def copie(p):
    p_copie = Pile()
    p_auxiliaire = Pile()
    while not p.est_vide():
        p_auxiliaire.empile(p.depile())

    while not p_auxiliaire.est_vide():
        x = p_auxiliaire.depile()
        p.empile(x)
        p_copie.empile(x)
        
    return p_copie

def copie_maline(p):
    p_inverse = inverse(p)
    p_copie = inverse(p_inverse)
    return p_copie

# Ex 5
# 1
def fond(p):
    p_aux = Pile()
    while not p.est_vide():
        tmp = p.depile()
        p_aux.empile(tmp)

    el_fond = p_aux.depile()
    
    while not p_aux.est_vide():
        p.empile(p_aux.depile())
    
    return el_fond

# 2
def rotation(p):
    pile_aux = Pile()
    futur_fond = p.depile()
    while not p.est_vide():
        pile_aux.empile(p.depile())
    futur_haut = pile_aux.depile()
    
    p.empile(futur_fond)
    while not pile_aux.est_vide():
        p.empile(pile_aux.depile())
    p.empile(futur_haut)
    
# Ex 6
def test_parenthesage(expression):
    pile = Pile()
    for caractere in expression:
        if caractere in "([{":
            pile.empile(caractere)
        if caractere in ")]}":
            if pile.est_vide():
                return False
            caractere_deja_lu = pile.depile()
            if caractere_deja_lu=="(" and caractere!=")" \
               or caractere_deja_lu=="[" and caractere!="]" \
               or caractere_deja_lu=="{" and caractere!="}":
                return False
    return pile.est_vide()

# Ex 7
def ranger(p):
    pile_assiettes_blanches = Pile()
    pile_assiettes_vertes = Pile()

    while not p.est_vide():
        assiette = p.depile()
        couleur = assiette[0]
        if couleur == "blanc":
            pile_assiettes_blanches.empile(assiette)
        else:
            pile_assiettes_vertes.empile(assiette)
            
    while not pile_assiettes_blanches.est_vide():
        p.empile(pile_assiettes_blanches.depile())

    while not pile_assiettes_vertes.est_vide():
        p.empile(pile_assiettes_vertes.depile())

# SCRIPT
# Ex 2
pile = Pile()
pile.empile(1)
pile.empile(2)
pile.empile(3)
pile.empile(4)
print(pile)
echange(pile)
print(pile)

# Ex 3
pile_inverse = inverse(pile)
print(pile_inverse)

# Ex 4
pile_copie = copie(pile)
print(pile_copie)
pile_copie_maline = copie_maline(pile)
print(pile_copie_maline)

# Ex 5
assert fond(pile) == 1
print(pile)
# réinitialisation de la pile
pile = Pile()
pile.empile(1)
pile.empile(2)
pile.empile(3)
pile.empile(4)
pile.empile(5)
pile.empile(6)
print(pile)
rotation(pile)
print(pile) # doit avoir 6 tout en bas et 1 tout en haut

# Ex 6
assert test_parenthesage("(a)(b)(((c)(d)))")==True
assert test_parenthesage("([b]){((c))[d]}")==True
assert test_parenthesage("(")==False
assert test_parenthesage("(a))")==False
assert test_parenthesage("((a))}")==False
assert test_parenthesage("[[a]")==False
assert test_parenthesage("[(a])")==False
assert test_parenthesage("{((a)})")==False

# Ex 7
pile_assiettes = Pile()
pile_assiettes.empile(("blanc", 3))
pile_assiettes.empile(("vert", 3))
pile_assiettes.empile(("vert", 4))
pile_assiettes.empile(("blanc", 5))
pile_assiettes.empile(("blanc", 6))
pile_assiettes.empile(("vert", 7))
pile_assiettes.empile(("blanc", 8))
pile_assiettes.empile(("vert", 9))
print(pile_assiettes)

ranger(pile_assiettes)
print(pile_assiettes)