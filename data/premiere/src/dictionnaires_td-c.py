# FONCTIONS
def est_present(tab, v):
    for elmt in tab:
        if elmt == v:
            return True 
    return False

def depouillement(candidats, votes):
    occurences = {cle:0 for cle in candidats}
    occurences["Blanc"] = 0
    occurences["Nul"] = 0
    for v in votes:
        if est_present(candidats, v):
            occurences[v] += 1
        elif v == "":
            occurences["Blanc"] += 1
        else:
            occurences["Nul"] += 1
    return occurences
    

# SCRIPT
tab = [3, 5, 7, 9, 1]
print(est_present(tab, 5))
print(est_present(tab, 22))

candidats = ["Alan Turing", "Ada Lovelace", "George Boole"]
votes = ["Alan Turing", "Ada Lovelace", "Ada Lovelace", "", "George Boole", "Mark Zukerberg", ""]
print(depouillement(candidats, votes))