# ####### #
# IMPORTS #
# ####### #

from math import pi
from random import randint


# ######### #
# FONCTIONS #
# ######### #

def notes_au_hasard(nb):
    return [randint(0, 20) for _ in range(nb)]


# ###### #
# SCRIPT #
# ###### #

# Ex 14
print("------------ Ex 14 ------------")
lst = [2*n+1 for n in range(5)] # lst  = [1, 3, 5, 7, 9]
print(lst)
lst = [n for n in range(10) if n%3==1] # lst  = [1, 4, 7]
print(lst)
lst = [n for n in range(1, 12) if 12%n==0] # lst  = [1, 2, 3, 4, 6]
print(lst)
lst = [(n, n**2) for n in range(5)] 
    # lst  = [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)]
print(lst)
lst = [c for c in str(pi)] 
    # lst  = ['3', '.', '1', '4', '1', '5', '9', '2', '6', '5', '3', '5', '8', '9', '7', '9', '3']
print(lst)
lst = [chr(n) for n in range(97, 123)]
    # lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(lst)

# Ex 15
print("------------ Ex 15 ------------")
print(notes_au_hasard(5))
