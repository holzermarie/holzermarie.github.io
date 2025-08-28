import sys
sys.path.append('../')

from modules.gmanager import display, display_from_adjacency_list

# FONCTIONS

def get_adjacency_matrix(adj_list):
    # tableau des étiquettes triées
    labels = [label for label in adj_list.keys()]
    labels.sort()
    
    # initialisation de la matrice
    n = len(labels)
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    # remplissage
    for i in range(n):
        label = labels[i]
        neighbors = adj_list[label]
        for j in range(n):
            if labels[j] in neighbors:
                matrix[i][j] = 1
                
    return matrix


def get_adjacency_list(adj_matrix):
    # tableau des étiquettes des sommets
    n = len(adj_matrix)
    labels = [chr(65 + i) for i in range(n)]
    
    # initialisation de la liste (un dictionnaire)
    dico = {}
    
    # remplissage
    for i in range(n):
        dico[labels[i]] = []
        neighbours = adj_matrix[i]
        print(neighbours)
        for j in range(len(neighbours)):
            if neighbours[j] == 1:
                dico[labels[i]].append(labels[j])
        
    return dico
    
# SCRIPT

# list -> matrix

adj_list = {"A": ["B", "E", "F", "G", "H"],
           "B": ["A", "E", "F", "G", "C", "D"],
           "C": ["B", "G", "H", "D"],
           "D": ["B", "C", "H"],
           "E": ["A", "B", "F"],
           "F": ["A", "E", "B", "G"],
           "G": ["A", "F", "B", "C", "H"],
           "H": ["A", "G", "C", "D"],
           }

adj_matrix = get_adjacency_matrix(adj_list)
for line in adj_matrix :
    print(line)


# lst_adj_complet = {"A": ["B", "C", "D"],
#                    "B": ["A", "C", "D"],
#                    "C": ["A", "B", "D"],
#                    "D": ["A", "C", "B"],
#            }
# 
# m = get_adjacency_matrix(lst_adj_complet)
# for l in m :
#     print(l)
    
###

# m = [[0, 1, 0, 0, 0, 1, 1, 0],
#      [1, 0, 1, 1, 0, 0, 0, 0],
#      [0, 1, 0, 0, 0, 0, 0, 1],
#      [0, 1, 0, 0, 1, 0, 0, 0],
#      [0, 0, 0, 1, 0, 1, 0, 0],
#      [1, 0, 0, 0, 1, 0, 1, 0],
#      [1, 0, 0, 0, 0, 1, 0, 1],
#      [0, 0, 1, 0, 0, 0, 1, 0]]

# matrix -> list

adj_matrix = [[0, 1, 0, 0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 0, 1, 1],
    [0, 1, 1, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 1, 0, 1, 0],
    [1, 1, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 0, 1, 0]]

adj_list = get_adjacency_list(adj_matrix)

print("{")
for label, neighbours in adj_list.items():
    print(f'\'{label}\': {neighbours}')
print("}")

display_from_adjacency_list(adj_list)

