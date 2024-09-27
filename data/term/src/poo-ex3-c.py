# CLASSES
class Date:
    """ Date(int, int, int) -> Date (signature de la méthode/fonction)
        Classe représentant une date (jour, mois, année). """
    
    def __init__(self, jour, mois, annee):
        if jour < 1 or jour > 31 or not isinstance(jour, int):
            raise ValueError("Le jour doit être un entier compris entre 1 et 31.")
        elif mois < 1 or mois > 12 or not isinstance(mois, int):
            raise ValueError("Le mois doit être un entier compris entre 1 et 12.")
        elif not isinstance(annee, int):
            raise ValueError("L'année doit être un entier.")
        
        self.jour = jour
        self.mois = mois
        self.annee = annee

    def __str__(self):
        """ __str__() -> str
            Permet d'afficher un objet de type 'Date' sous forme d'une chaîne de caractères de type "25 mai 1999" """
        nom_mois = {1: "janvier", 2: "février", 3: "mars", 4: "avril", 5: "mai", 6: "juin",
                7: "juillet", 8: "aout", 9: "septembre", 10: "octobre", 11: "novembre",
                12: "decembre"}

        return f"{self.jour} {nom_mois[self.mois]} {self.annee}"

    def __lt__(self, date):
        """ __lt__(Date) -> bool
            Compare la date 'self' à la date 'date' passée en paramètre. Renvoie 'True' si 'self' est avant 'date', 'False' sinon. """
        if self.annee < date.annee:
            return True 
        
        if self.annee == date.annee:
            if self.mois < date.mois:
                return True
            
            if self.mois == date.mois:
                return self.jour < date.jour

        return False
    
    # OU
    def __lt__(self, date):
        # Exploitation de l'évaluation paresseuse des booléens en Python
        return self.annee < date.annee or \
            self.annee == date.annee and (self.mois < date.mois or \
            self.mois == date.mois and self.jour < date.jour)

# SCRIPT
# 1), 2) a) et b)
date1 = Date(14, 7, 1789)
date2 = Date(13, 7, 1789)

print(date1)
print(date2)

# 2) c)
print(date1.annee)

# TESTS <
assert Date(14, 7, 1789) < Date(15, 7, 1789)
assert Date(14, 7, 1789) < Date(14, 8, 1789)
assert Date(14, 7, 1789) < Date(14, 7, 1790)

assert not Date(14, 7, 1789) < Date(14, 7, 1789)

assert Date(14, 7, 1789) < Date(15, 8, 1790)
