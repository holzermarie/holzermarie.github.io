# ####### #
# IMPORTS #
# ####### #



# ######### #
# FONCTIONS #
# ######### #

# Ex 4
def foo(lst):
    lst2 = []
    for el in lst :
        if el%2==0 :
            lst2.append(el)
    return lst2


# Ex 5
def bar(lst):
    idx = 0
    while idx<len(lst):
        el = lst[idx]
        if el%2==0 :
            lst.remove(el)
        else :
            idx = idx+1

# Ex 6
# 1)
def bonnes_notes(notes):
    lst = []
    for note in notes:
        if note >= 10:
            lst.append(note)
    return lst

# 2)
# Exemple qui ne marche justement pas !
def pas_bien_supprime_mauvaises_notes(notes):
    for note in notes:
        if note < 10:
            notes.remove(note) 

# Et la bonne version
def supprime_mauvaises_notes(notes):
    idx = 0
    while idx < len(notes):
        el = notes[idx]
        if el < 10 :
            notes.remove(el)
        else :
            idx = idx + 1
            
# ###### #
# SCRIPT #
# ###### #

print("\n------------ Ex 4 ------------")
print(foo([12, 5, 14, 17]))


print("\n------------ Ex 5 ------------")

lst = [12, 5, 14, 17]
bar(lst)
print(lst)


print("\n------------ Ex 6 ------------")
print("1)")
notes = [7, 5, 16, 8, 10, 6, 20, 16]
notes_restantes = bonnes_notes(notes)
print(notes_restantes)

print("2)")
pas_bien_supprime_mauvaises_notes(notes)
# print(notes)
notes = [7, 5, 16, 8, 10, 6, 20, 16]
supprime_mauvaises_notes(notes)
print(notes)

print("\n------------ Ex 7 ------------")
lst = [2, 4, 6, 8]
lst[0] = lst[3]*2
lst[1] = lst[0]-lst[1]
lst[2] += 20
print(lst)