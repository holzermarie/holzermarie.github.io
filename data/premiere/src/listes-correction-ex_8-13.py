# ####### #
# IMPORTS #
# ####### #

from math import sqrt

# Ex 8
# 1)
def symetrie_axe_x(p):
    p[1] = -p[1]

# 2)
def symetrie_axe_y(p):
    p[0] = -p[0]

# 3)
def symetrie_origine(p):
    p[0] = -p[0]
    p[1] = -p[1]
    
# 4)
def symetrie_premiere_bissectrice(p):
    nouvel_y = p[0]
    p[0] = p[1]
    p[1] = nouvel_y
    
# 5)
def translation(p, u):
    p[0] = p[0] + u[0]
    p[1] = p[1] + u[1]

# Ex 9
# voir partie SCRIPT

# Ex 10
# voir partie SCRIPT

# Ex 11
def inserer(lst, el, idx):
    lst_debut = []
    for indice in range(0, idx):
        lst_debut.append(lst[indice])
    lst_fin = []
    for indice in range(idx, len(lst)):
        lst_fin.append(lst[indice])
        
    return lst_debut + [el] + lst_fin

# Ex 12
def truc(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    mx = (x1+x2)/2
    my = (y1+y2)/2
    return (mx, my)

# Ex 13
# 1)
def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return sqrt( (x2-x1)**2 + (y2-y1)**2 )

# 2)
def plus_proche_voisin(liste, p):
    distance_min = distance(liste[0], p)
    voisin = liste[0]
    for idx in range(1, len(liste)): # car on a déjà traité liste[0] 
        dist_bis = distance(p, liste[idx])
        if dist_bis < distance_min: # recherche de minimum
            distance_min = dist_bis
            voisin = liste[idx] # le plus proche pour le moment
    return voisin

# ###### #
# SCRIPT #
# ###### #

print("\n------------ Ex 8 ------------")
print("1)")
symetrie_axe_x([2, 3])
print("2)")
symetrie_axe_y([2, 3])
print("3)")
symetrie_origine([2, 3])
print("4)")
symetrie_premiere_bissectrice([2, 3])
print("5)")
translation([2, 3], [10, 20])

print("\n------------ Ex 9 ------------")
lst = []
for idx in range(5):
    lst = lst + [idx]*idx

print(lst)

print("\n------------ Ex 10 ------------")
# à faire plutôt sur papier ! Il s'agit de comprendre que ces trois fonctions
# font la même chose mais le programme est écrit de manières différentes

# print("a/")
# lst = []
# for n in range(50000):
#     lst.append(n)
# print(lst)
# 
# print("b/")
# lst = []
# for n in range(50000):
#     lst = lst+[n]
# print(lst)
#     
# print("c/")
# lst = []
# for n in range(50000):
#     lst += [n]
# print(lst)

print("\n------------ Ex 11 ------------")
une_liste = [45, 78, 98, 5, 9, 6]
print(inserer(une_liste, [66], 2))

print("\n------------ Ex 12 ------------")
print(truc((1, 5), (3, 9)))
# ce sont les coordonnées du milieu du segment dont les extrémités ont pour coordonnées p1 et p2

print("\n------------ Ex 13 ------------")
print("1)")
p1, p2 = ((1, 5), (3, 9))
print(distance(p1, p2))

print("2)")
liste = [(1, 5), (3, 9), (2, 5), (3, 12), (4, 5), (4, 13)]
print(plus_proche_voisin(liste, (4, 4)))
print(plus_proche_voisin(liste, (2, 8)))

