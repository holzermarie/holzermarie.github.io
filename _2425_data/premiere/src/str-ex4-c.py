# Ex 4
s = "abn\nn\\\""
print(len(s)) # affiche 7

# Pour vérifier, on affiche s
print(s)
# On constate que \n fait passer à la ligne, ceci compte comme un caractère
# \\ affiche un antislash, ceci compte comme un caractère
# \" affiche des guillemets (si pas de \, ils sont
# interprétés comme une fin de chaîne), ceci compte comme un caractère
