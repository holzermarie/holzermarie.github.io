from time import time_ns, sleep

debut = time_ns()

print("Ici, on fait des trucs")
print("On attend un peu...")
sleep(1)
print("...")
sleep(3)
print("Voilà")

fin = time_ns()

duree_nanosecondes = fin - debut
duree_secondes = duree_nanosecondes / (10**9)
print("\n-> Tout ceci nous a pris %.3f secondes." % duree_secondes)