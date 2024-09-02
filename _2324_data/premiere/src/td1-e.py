## DONNÉES EN TABLES # TD 1 ##

def split_str(string, sep):
    # ...
    # Ajouter du code ici :
    # ...
    
    return lst

def import_data():
    # lecture du fichier
    # (pour rappel, voir cours sur les chaînes de caractères, section « Les fichiers texte »)
    reader = open("indicateurs.csv", "r", encoding="utf-8")
    raw_data = reader.read()
    reader.close()
    
    # Compléter le code ici :
    # lines = split_str(..., ...)
    
    return lines

lst = import_data()