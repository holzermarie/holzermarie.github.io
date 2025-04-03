# FONCTIONS
def est_present(tab, v):
    for elmt in tab:
        if elmt == v:
            return True 
    return False

def trouve_maximum(t):
    maxi = 0
    for val in t:
        if val > maxi:
            maxi = val
    return maxi

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
    
def vainqueur(d):
    nb_vote_max = 0
    elu = ""
    for candidat, nb_voies in d.items():
        if nb_voies > nb_vote_max:
            nb_vote_max = nb_voies
            elu = candidat
    return elu

# SCRIPT
candidats = ["Alan Turing", "Ada Lovelace", "George Boole"]
occurrences = {"Nul": 0, "Blanc": 0}
for candidat in candidats:
    occurrences[candidat] = 0
print(occurrences)

tab = [3, 5, 7, 9, 1]
print(est_present(tab, 5))
assert est_present(tab, 5)
print(est_present(tab, 22))
assert not est_present(tab, 22)

assert trouve_maximum(tab) == 9

candidats = ["Alan Turing", "Ada Lovelace", "George Boole"]
votes = ["Alan Turing", "Ada Lovelace", "Ada Lovelace", "", "George Boole", "Mark Zukerberg", ""]
res_election = depouillement(candidats, votes)
assert res_election == {'Alan Turing': 1, 'Ada Lovelace': 2, 'George Boole': 1, 'Blanc': 2, 'Nul': 1}
print(res_election) # doit afficher {'Alan Turing': 1, 'Ada Lovelace': 2, 'George Boole': 1, 'Blanc': 2, 'Nul': 1}

resultat = vainqueur(res_election)
print(resultat) # doit afficher "Ada Lovelace"
assert resultat == "Ada Lovelace"