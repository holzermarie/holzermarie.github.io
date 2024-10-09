####################
#### Exercice 2 ####
####################

# IMPORTS

from turtle import *
from math import sqrt

# FONCTIONS

def carre(cote):
    for _ in range(4):
        forward(cote)
        right(90)
        
def triangle(cote):
    for _ in range(3):
        forward(cote)
        right(120)
        
def carre_blanc(cote):
    begin_fill()
    color("white", "white")
    carre(cote)
    end_fill()
    
def disque_gris(cote):
    begin_fill()
    color("gray", "gray")
    circle(cote)
    end_fill()
    

def carres_imbriques(cote):
    if cote < 1:
        return
    
    # tracer le carré
    carre(cote)
    
    # déplacement
    forward(cote/2)
    right(45)
    
    # appel récursif
    carres_imbriques(cote/sqrt(2))
    
def triangles_imbriques(cote):
    if cote < 1:
        return
    
    # tracer le triangle
    triangle(cote)
    
    # déplacement
    forward(cote/2)
    right(60)
    
    # appel récursif
    triangles_imbriques(cote/2)
    
def cercles_carres_imbriques(cote):
    if cote < 1:
        return
    
    # tracer le carré blanc
    begin_fill()
    color("white", "white")
    carre(cote)
    end_fill()

    # déplacement position initiale cercle
    right(90)
    forward(cote/2)

    # trace le cercle gris
    begin_fill()
    color("gray", "gray")
    circle(cote/2)
    end_fill()
    
    # déplacement
    left(135)
    
    # OU
#     forward(-cote/2)
#     left(90)
#     
#     forward(cote/2)
#     right(45)
    
    # appel récursif
    cercles_carres_imbriques(cote/sqrt(2))

def cercles_carres_imbriques_compact(cote):
    if cote < 1:
        return
    
    # tracer le carré blanc
    carre_blanc(cote)

    # déplacement position initiale cercle
    right(90)
    forward(cote/2)

    # trace le cercle gris
    disque_gris(cote/2)
    
    # déplacement
    left(135)
    
    # appel récursif
    cercles_carres_imbriques(cote/sqrt(2))

# SCRIPT

setup(800, 600)
speed(10)

# carres_imbriques(100)
# triangles_imbriques(200)
# cercles_carres_imbriques(200)
cercles_carres_imbriques_compact(200)

# boucle maintenant la fenêtre ouverte
mainloop()