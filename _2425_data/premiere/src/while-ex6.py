# somme des carrés des 100 premiers entiers
somme = 0
nb = 0

while nb < 100: # 0 à 99 => 100 nombres différents
    carre = nb**2
    somme = somme + carre
    nb = nb + 1
    
print(somme)
    