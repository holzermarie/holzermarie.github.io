# FONCTIONS
# Ex 3
def rang(l):
    return ord(l) - 97

def lettre(r):
    return chr(r + 97)

# SCRIPT
assert rang("a") == 0
assert rang("z") == 25

assert lettre(2) == "c"