# IMPORTS
from turtle import *   # import du module turtle
from math import pi

# FONCTIONS
def heptagone(c):
    for i in range(7):
        forward(c)
        right(360/7)
        
def polygone(n, c):
    for i in range(n):
        forward(c)
        right(360/n)
        
def cercle(r):
    perimetre = 2*pi*r
    polygone(360, perimetre/360)
    right(90)
    forward(r*2)


# SCRIPT
# taille de la fenetre
setup(800,600)
speed(10000)

heptagone(50)
# polygone(7, 100)
cercle(100)

mainloop()