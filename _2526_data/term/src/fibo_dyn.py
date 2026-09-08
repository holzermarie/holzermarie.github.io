# IMPORTS
import timeit

# FONCTIONS

def fibo_rec(n):
    # ...
    pass

def fibo_rec_memo(n, memo=[]):
    # ...
    pass

def fibo_ite_memo(n):
    # ...
    pass


# SCRIPT

# Tests
assert fibo_rec(5) == 5
assert fibo_rec(0) == 0
assert fibo_rec(1) == 1

assert fibo_rec_memo(5) == 5
assert fibo_rec_memo(0) == 0
assert fibo_rec_memo(1) == 1

assert fibo_ite_memo(5) == 5
assert fibo_ite_memo(0) == 0
assert fibo_ite_memo(1) == 1

# Mesures des temps d'exécution
# if __name__ == '__main__':
#     # n_lst = [5, 20, 30, 50, 100, 1000, 10000]
#     n_lst = [5, 20, 30]
#     for n in n_lst:
#         print(f"********************** n = {n} ***************************")
#         temps = timeit.timeit(f'fibo_rec({n})', setup='from __main__ import fibo_rec', number=1)
#         print(f"*** fibo_rec : {round(temps, 2)} s***")
#         
#         temps = timeit.timeit(f'fibo_rec_memo({n})', setup='from __main__ import fibo_rec_memo', number=1)
#         print(f"*** fibo_rec_memo : {round(temps, 2)} s***")
#         
#         temps = timeit.timeit(f'fibo_ite_memo({n})', setup='from __main__ import fibo_ite_memo', number=1)
#         print(f"*** fibo_ite_memo : {round(temps, 2)} s***")
#         
#         print() # saute une ligne


