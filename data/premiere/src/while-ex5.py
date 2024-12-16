# FONCTIONS
def is_prime(n):
    d = 2
    stop = False
    while d < n and not stop :
        if n % d == 0:
            stop = True
        d = d + 1
    return stop

# SCRIPT
res = is_prime(77)
print(res)


res = is_prime(79)
print(res)