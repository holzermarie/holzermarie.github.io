# IMPORTS

# FONCTIONS

def fibo(n):
    if n <= 1: # condition d'arrêt
        return n
    return fibo(n-1)+fibo(n-2)

def fibo_iteratif(n):
    # on règle les deux premiers termes
    if n <= 1:
        return n
    
    n_moins_1 = 1
    n_moins_2 = 0
    
    for _ in range(2, n+1):
        total = n_moins_1 + n_moins_2
        n_moins_2 = n_moins_1 # attention à l'ordre des instructions !
        n_moins_1 = total

    return total  
     
# SCRIPT

assert fibo(0) == 0
assert fibo(1) == 1
assert fibo(2) == 1
assert fibo(3) == 2

# res = fibo(6)
# print(res)


assert fibo_iteratif(0) == 0
assert fibo_iteratif(1) == 1
assert fibo_iteratif(2) == 1
assert fibo_iteratif(3) == 2

# res = fibo_iteratif(6)
# print(res)


# res = fibo(12)
# print(res)