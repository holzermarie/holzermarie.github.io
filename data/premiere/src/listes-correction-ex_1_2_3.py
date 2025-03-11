# IMPORTS

# FONCTIONS

# Ex 2) 1. 
def moyenne(liste_notes):
    somme = 0
    for note in liste_notes :
        somme = somme + note
    nb_notes = len(liste_notes)
    return somme/nb_notes


# Ex 2) 2.
def meilleure_note(liste_notes):
    meilleure = 0
    for note in liste_notes :
        if note > meilleure :
            meilleure = note
    return meilleure


# Ex 3) 1.
def contient(lst, el):
    for item in lst:
        if item == el:
            return True
    return False


# Ex 3) 2.
def position_de(lst, el):
    last_idx = -1
    taille = len(lst)
    for idx in range(taille):
        if lst[idx] == el:
            last_idx = idx
    return last_idx

# SCRIPT

# Ex 1

notes = [12, 18, 14, 20]

print("------------ Ex 1 ------------")
print(notes[1]) # affiche 18
n = len(notes)
x = notes[n-1]
print(x) # affiche 20
x = 15
print(notes) # affiche [12, 18, 14, 20]

# Ex 2
print("------------ Ex 2 ------------")
print("1)")
print(moyenne(notes))
print("2)")
print(meilleure_note(notes))

# Ex 3
print("------------ Ex 3 ------------")
print("1)")
une_liste = [34, 56, 87, 66]
print(contient(une_liste, 66))
print(contient(une_liste, 6))

print("2)")
print(position_de(une_liste, 66))
print(position_de(une_liste, 6))
# on teste qu'on renvoie bien la position de la 1ère occurrence
une_autre_liste = [34, 56, 87, 66, 56, 87]
print(position_de(une_autre_liste, 56))

