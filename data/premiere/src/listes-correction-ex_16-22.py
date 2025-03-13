# ####### #
# IMPORTS #
# ####### #

import pygame
from math import sqrt


# ######### #
# FONCTIONS #
# ######### #

# EXERCICES EN VRAC

# Ex 16
def est_premier(n):
    if n<2 : 
        return False
    for d in range(2, n):
        if n%d==0:
            return False
    return True

def nombres_premiers(n):
    liste = []
    k = 0
    while len(liste)<n :
        if est_premier(k):
            liste.append(k)
        k += 1
    return liste

# Ex 17
def carre(lst):
    return [el**2 for el in lst]

# Ex 18
def fibonacci(n):
    suite = [1, 1]
    if n<3 :
        return suite[:n]
    for k in range(n-2) :
        l = len(suite)
        nouveau_terme = suite[l-1]+suite[l-2]
        suite.append(nouveau_terme)
    return suite

# Ex 19
def champs(s):
    lst = []
    mot = ""
    for c in s :
        if c!=";":
            mot += c
        else :
            lst.append(mot)
            mot = ""
    if mot != "":
        lst.append(mot)
    return lst

# Ex 20
def moyenne(lst):
    s = 0
    for n in lst:
        s += n
    return s/len(lst)

def ecart_type(lst):
    m = moyenne(lst)
    s = 0
    for n in lst :
        s += (n-m)**2
    return sqrt(s/len(lst))

# Ex 21
def frequences(lst):
    effectifs = [0]*6
    for lancer in lst :
        effectifs[lancer-1] += 1
    n = len(lst)
    return [ el/n for el in effectifs]
    
def histogramme(fenetre, freqs):
    x = 0
    bleu = (100, 100, 100)
    for f in freqs :
        h = 400*f
        r = pygame.Rect(x, 400-h, 100, h)
        pygame.draw.rect(fenetre, bleu, r) 
        x += 100
    
def main(nb):
    pygame.init()

    fenetre = pygame.display.set_mode((600, 400))

    sims = [randint(1,6) for n in range(nb)]
    freqs = frequences(sims)
    histogramme(fenetre, freqs)

    pygame.display.update()

    lock = True
    while lock:
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                lock = False

    pygame.quit()


# Ex 22
def pascal(n):
    ligne = [1]
    for k in range(n) :
        nouvelle_ligne = [1]
        for idx in range(k):
            terme = ligne[idx]+ligne[idx+1]
            nouvelle_ligne.append(terme)
        nouvelle_ligne.append(1)
        ligne = nouvelle_ligne
    return ligne


# ###### #
# SCRIPT #
# ###### #

print("*********** EXERCICES EN VRAC ***********")
print("------------ Ex 16 ------------")
print(nombres_premiers(30))

print("------------ Ex 17 ------------")
print(carre([2, 3, 4, 5]))

print("------------ Ex 18 ------------")
print(fibonacci(30))
print(fibonacci(3))
print(fibonacci(2))
print(fibonacci(1))
print(fibonacci(150))

print("------------ Ex 19 ------------")
s = "Lycée; Adresse; Code Postal; Ville\nLycée Buffon; 16 boulevard Pasteur; 75015; Paris\nLycée Fresnel; 31 boulevard Pasteur; 75015; Paris"
print(champs("Lycée Buffon; 16 boulevard Pasteur; 75015; Paris"))

print("------------ Ex 20 ------------")
notes = [12, 14, 2, 19, 15, 18, 15, 3, 15, 14]
print(moyenne(notes))
print(ecart_type(notes))

print("------------ Ex 21 ------------")
# main(150)

print("------------ Ex 22 ------------")
print(pascal(6))
