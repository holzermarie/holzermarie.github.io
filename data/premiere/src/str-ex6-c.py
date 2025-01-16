ch = "abcdef"
taille_ch = len(ch) # vaut 6
dernier_indice = taille_ch - 1 # vaut 5
x = ch[dernier_indice]
print(x) # affiche "f"

# on aurait pu moins détailler et écrire directement :
x = ch[len(ch) - 1]
print(x) # affiche "f"

# En Python, on peut aussi accéder au dernier élément grâce à l'indice -1 :
x = ch[-1]
print(x) # affiche "f"

# D'autres exemples :
ch2 = "ghijklmnop"
x = ch2[len(ch2) - 1]
print(x) # affiche "p"

ch3 = "sfuvbsuvbuuyvgsqyvgqivbqyibqylevbqlyevbqivbqmivgqievgqeivbquevbuqbvuqebvuqevbquvqvbqbvdl"
x = ch3[len(ch3) - 1]
print(x) # affiche "l"