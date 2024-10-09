# IMPORTS

# FONCTIONS

def factorielle(n):
    """ factorielle(int) -> int
        Renvoie la factorielle de n, entier supérieur ou égal à 1 """
    
    assert type(n) == int and n>0, "n doit être un entier supérieur ou égal à 1" # pré-condition
    
    if n == 1:
        return 1
    
    return n*factorielle(n-1)

# SCRIPT

assert factorielle(1) == 1
assert factorielle(2) == 2
assert factorielle(3) == 6
assert factorielle(4) == 24
assert factorielle(5) == 120
assert factorielle(6) == 720
assert factorielle(7) == 5040

res = factorielle(4)
print(res)