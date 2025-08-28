# FONCTIONS
# 1)
def somme_inverses(n):
    somme = 0
    denominateur = 1
    while denominateur <= n:
        somme = somme + 1/denominateur
        denominateur = denominateur + 1
    return somme
        
    
# SCRIPT
# tests
assert somme_inverses(1) == 1
assert somme_inverses(2) == 1 + 1/2
assert somme_inverses(4) == 1 + 1/2 + 1/3 + 1/4

# 2) plus petit entier n tel que Hn > 10
n = 0
while somme_inverses(n) < 10:
    n = n + 1
print(n)