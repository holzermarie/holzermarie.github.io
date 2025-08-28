# FONCTIONS
# Question 1
def fois_deux(x):
    resultat = x * 2
#     print(resultat) # question 2
    return resultat # question 3

# Question 5
def multiplication(a, b):
#     print(a*b) # 5
    res = a*b
    return res # 8

# Question 10
def addition(a, b):
    return a + b

# SCRIPT
# Question 2 et 4
res = fois_deux(6)
print(res)

# Question 6 et 9
resultat = multiplication(4, 3)
print(resultat)
resultat = multiplication(4.0, 3.0)
print(resultat)
# Question 7 : la fonction renvoie un entier quand on lui passe deux entiers,
# et renvoie un flottant quand on lui passe deux flottants

# Question 10
print(addition(3, 4))