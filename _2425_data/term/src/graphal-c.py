# CLASSES
class GraphAL:

    def __init__(self, adj_lst):
        self.adj_lst = adj_lst
        
    def parcours_prof(self, sommet, deja_vus=[]):
        if sommet in deja_vus:
            return []
        
        voisins = self.adj_lst[sommet]
        deja_vus.append(sommet)
        lst_parcours = [sommet]
        
        for voisin in voisins:
            lst_parcours += self.parcours_prof(voisin, deja_vus)
            
        return lst_parcours
        
    def parcours_prof_it(self, sommet):      
        lst_parcours = []
        deja_vus = [sommet]
        pile_a_traiter = [sommet]
        
        while len(pile_a_traiter) != 0:
            sommet_courant = pile_a_traiter.pop()
            lst_parcours.append(sommet_courant)
            for voisin in self.adj_lst[sommet_courant]:
                if not voisin in deja_vus:
                    deja_vus.append(voisin)
                    pile_a_traiter.append(voisin)
                    
        return lst_parcours
        
    def parcours_largeur(self, sommet):      
        lst_parcours = []
        deja_vus = [sommet]
        file_a_traiter = [sommet]
        
        while len(file_a_traiter) != 0:
            sommet_courant = file_a_traiter.pop(0) # seule différence ici, on utilise une "file"
            lst_parcours.append(sommet_courant)
            for voisin in self.adj_lst[sommet_courant]:
                if not voisin in deja_vus:
                    deja_vus.append(voisin)
                    file_a_traiter.append(voisin)
                    
        return lst_parcours
    
# SCRIPT

# les sommets sont rangés dans l'ordre lexicographique croissant
adj_lst = { "A" : list("BFG"),
             "B" : list("AG"),
             "C" : list("DG"),
             "D" : list("CGI"),
             "E" : list("IJ"),
             "F" : list("AG"),
             "G" : list("ABCDFH"),
             "H" : list("GI"),
             "I" : list("DEHJ"),
             "J" : list("EI")}

graphe = GraphAL(adj_lst)

print("Parcours en profondeur récursif")

# Attention de bien laisser les listes vides en deuxième paramètre

print(graphe.parcours_prof("A", [])) # A, B, G, C, D, I, E, J, H, F
print(graphe.parcours_prof("E", [])) # E, I, D, C, G, B, A, F, H, J
print(graphe.parcours_prof("H", [])) # H, G, A, B, F, C, D, I, E, J

assert graphe.parcours_prof("A", []) == ['A', 'B', 'G', 'C', 'D', 'I', 'E', 'J', 'H', 'F']
assert graphe.parcours_prof("E", []) == ['E', 'I', 'D', 'C', 'G', 'A', 'B', 'F', 'H', 'J']
assert graphe.parcours_prof("H", []) == ['H', 'G', 'A', 'B', 'F', 'C', 'D', 'I', 'E', 'J']

print("Parcours en profondeur itératif")

print(graphe.parcours_prof_it("A")) # A, G, H, I, J, E, D, C, F, B
print(graphe.parcours_prof_it("E")) # E, J, I, H, G, F, C, B, A, D
print(graphe.parcours_prof_it("H")) # H, I, J, E, D, C, G, F, B, A

assert graphe.parcours_prof_it("A") == ['A', 'G', 'H', 'I', 'J', 'E', 'D', 'C', 'F', 'B']
assert graphe.parcours_prof_it("E") == ['E', 'J', 'I', 'H', 'G', 'F', 'C', 'B', 'A', 'D']
assert graphe.parcours_prof_it("H") == ['H', 'I', 'J', 'E', 'D', 'C', 'G', 'F', 'B', 'A']

print("Parcours en largeur")

print(graphe.parcours_largeur("A")) # A, B, F, G, C, D, H, I, E, J
print(graphe.parcours_largeur("E")) # E, I, J, D, H, C, G, A, B, F
print(graphe.parcours_largeur("H")) # H, G, I, A, B, C, D, F, E, J

assert graphe.parcours_largeur("A") == ['A', 'B', 'F', 'G', 'C', 'D', 'H', 'I', 'E', 'J']
assert graphe.parcours_largeur("E") == ['E', 'I', 'J', 'D', 'H', 'C', 'G', 'A', 'B', 'F']
assert graphe.parcours_largeur("H") == ['H', 'G', 'I', 'A', 'B', 'C', 'D', 'F', 'E', 'J']