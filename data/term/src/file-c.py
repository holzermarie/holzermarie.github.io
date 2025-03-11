# IMPORTS
from file import *

# FONCTIONS
def passe_ton_tour(f):
    premier = f.defile()
    f.enfile(premier)  

def nb_occurences(f, val):
    compteur = 0
    f_auxiliaire = File()
    
    while not f.est_vide():
        element = f.defile()
        if val == element:
            compteur += 1
        f_auxiliaire.enfile(element)
        
    while not f_auxiliaire.est_vide():
        f.enfile(f_auxiliaire.defile())
            
    return compteur

def last_is_first(f):
    f_auxiliaire = File()
    
    while f.taille() > 1:
        element = f.defile()
        f_auxiliaire.enfile(element)
        
    dernier = f.defile()
        
    f.enfile(dernier)
    while not f_auxiliaire.est_vide():
        f.enfile(f_auxiliaire.defile())

def permute_prochains(f):
    prochain = f.defile()
    prochain_prochain = f.defile()
    
    f_auxiliaire = File()
    f_auxiliaire.enfile(prochain_prochain)
    f_auxiliaire.enfile(prochain)
    
    while not f.est_vide():
        f_auxiliaire.enfile(f.defile())
    
    while not f_auxiliaire.est_vide():
        f.enfile(f_auxiliaire.defile())

def permute_derniers(f):
    f_auxiliaire = File()
    
    while f.taille() > 2:
        f_auxiliaire.enfile(f.defile())
    avant_dernier = f.defile()
    dernier = f.defile()
    
    while not f_auxiliaire.est_vide():
        f.enfile(f_auxiliaire.defile())
    f.enfile(dernier)
    f.enfile(avant_dernier)

def est_dans_la_file(f, val):
    f_auxiliaire = File()
    est_dedans = False
    
    while not f.est_vide():
        element = f.defile()
        f_auxiliaire.enfile(element)
        if val == element:
            est_dedans = True
    
    while not f_auxiliaire.est_vide():
        f.enfile(f_auxiliaire.defile())
        
    return est_dedans

def supprime_doublons(f):
    f_resultat = File()
    
    while not f.est_vide():
        element = f.defile()
        if not est_dans_la_file(f_resultat, element):
            f_resultat.enfile(element)
            
    while not f_resultat.est_vide():
        f.enfile(f_resultat.defile())

# sans la fonction de la question d'avant
# def supprime_doublons_bis(f):
#     f_resultat = File()
#     while not f.est_vide():
#         f_auxiliaire = File()
#         premier = f.defile()
#         f_resultat.enfile(premier)
#         
#         while not f.est_vide():
#             element = f.defile()
#             if element != premier:
#                 f_auxiliaire.enfile(element)
#                 
#         while not f_auxiliaire.est_vide():
#             f.enfile(f_auxiliaire.defile())
#         
#     while not f_resultat.est_vide():
#         f.enfile(f_resultat.defile())

def vin_first(f):
    f_vin = File()
    f_auxiliaire = File()
    
    while not f.est_vide():
        element = f.defile()
        if element % 12 == 0:
            f_vin.enfile(element)
        else:
            f_auxiliaire.enfile(element)
        
    while not f_vin.est_vide():
        f.enfile(f_vin.defile())
        
    while not f_auxiliaire.est_vide():
        f.enfile(f_auxiliaire.defile())

# SCRIPT

# # réfléchir au swap
# fa = File()
# fa.enfile("a")
# fa.enfile("b")
# fa.enfile("c")
# # print(fa)
# 
# f =  File()
# f.enfile("n")
# f.enfile("s")
# f.enfile("i")
# # print(f)
# 
# f, fa = fa, f
# # print(fa)
# # print(f)
# 
# # Ex 1
# f =  File()
# f.enfile("n")
# f.enfile("s")
# f.enfile("i")
# # print(f)
# x = f.defile()
# f.defile()
# f.enfile(x)
# # print(f)
# 
# # Ex 2
# # 1)
# f = File()
# f.enfile("a")
# f.enfile("b")
# f.enfile("c")
# f.enfile("d")
# # print(f)
# # passe_ton_tour(f)
# # print(f)
# 
# # 2) et 3)
# f.enfile("a")
# f.enfile("z")
# assert nb_occurences(f, "a") == 2
# assert nb_occurences(f, "b") == 1
# assert nb_occurences(f, "z") == 1
# assert nb_occurences(f, "w") == 0
# exit(0)
# # 4)
# print(f)
# last_is_first(f)
# print(f)
# 
# 
# # Ex 3
# f = File()
# f.enfile("a")
# f.enfile("b")
# f.enfile("c")
# f.enfile("d")
# f.enfile("e")
# f.enfile("f")
# print(f)

# 1)
f = File()
f.enfile("a")
f.enfile("b")
f.enfile("c")
f.enfile("d")
print(f)
permute_prochains(f)
print(f)

# 2)
permute_derniers(f)
print(f)

# Ex 4
f = File()
f.enfile("a")
f.enfile("b")
f.enfile("a")
f.enfile("c")
f.enfile("d")
f.enfile("d")
f.enfile("e")
f.enfile("f")
f.enfile("a")
# print(f)

# 1)
assert est_dans_la_file(f, "d")
assert not est_dans_la_file(f, "z")
print(f)

# 2)
supprime_doublons(f)
# print(f)

# Ex 5
f = File()
for nb in range(50):
    f.enfile(nb)
    
vin_first(f)
print(f)