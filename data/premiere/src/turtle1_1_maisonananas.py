from turtle import *   # import du module turtle
import math

# taille de la fenetre
setup(800,600)

# maison simple
# for i in range(4):
#     forward(100)
#     right(90)
#     
# left(60)
# forward(100)
# right(120)
# forward(100)

def toit(c):
    color("black", "orange")
    begin_fill()
    forward(c)
    right(120)
    forward(c)
    end_fill()

def maison(c):
    color("black", "yellow")
    begin_fill()
    for i in range(4):
        forward(c)
        right(90)
    end_fill()
    penup()
    forward(c)
    right(30)
    pendown()
    toit(c)

def toit_simple(c):
    forward(c)
    right(120)
    forward(c)
    
def maison_simple(c):
    for _ in range(4):
        forward(c)
        right(90)
    penup()
    forward(c)
    right(30)
    pendown()
    toit_simple(c)

# __main__
c = 100
speed(10)

maison_simple(100)

# left(90)
# for i in range(6):
#     maison(c)
#     backward(c)
#     left(90)
#     
# right(90)
# 
# # nouvelle position pour le nouvel ananas à droite
# penup()
# forward(c+c*math.sqrt(3))
# left(90)
# pendown()
# 
# for i in range(6):
#     maison(c)
#     backward(c)
#     left(90)
# 
# # nouvelle position pour l'ananas du bas
# penup()
# right(90)
# forward(c)
# right(30)
# pendown()
# 
# for i in range(6):
#     maison(c)
#     backward(c)
#     left(90)

# boucle maintenant la fenêtre ouverte
mainloop()