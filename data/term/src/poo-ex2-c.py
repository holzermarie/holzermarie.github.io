# CLASSES
class CompteBancaire:        
    def __init__(self, numero_compte, nom, prenom, solde):
        """ CompteBancaire(int, str, str, int) -> CompteBancaire
        Classe représentant un compte bancaire. """
        self.numero_compte = numero_compte
        self.nom = nom
        self.prenom = prenom
        self.solde = solde
        
    def __str__(self):
        return f"N° Compte : {self.numero_compte} | Prénom : {self.prenom} | Nom : {self.nom} | Solde : {self.solde}"
        
    def depot(self, somme):
        """ depot(int) -> int
            Ajouter le montant 'somme' au compte bancaire. """
        self.solde += somme # self.solde = self.solde + somme
        return self.solde
    
    def retrait(self, somme):
        """ retrait(int) -> int
            Ajouter le montant 'somme' au compte bancaire. """
        self.solde -= somme
        return self.solde
        
# FONCTIONS
# BONUS !!!!!!
def virement(compte_source, compte_destination, somme):
    """ virement(CompteBancaire, CompteBancaire, int) -> None
        Fait un virement dumontant somme du compte source vers le comte destination. """
    compte_source.retrait(somme)
    compte_destination.depot(somme)
        
# SCRIPT
# 1
mon_compte = CompteBancaire(1234, "Holzer", "Marie", 99999999999999)
# 2
print(mon_compte)
# 3
compte_ines = CompteBancaire(123, "Si", "Inès", 10000)
compte_jordi = CompteBancaire(321, "Nateur", "Jordi", 5000)
print(compte_ines)
print(compte_jordi)
# 4
# a
mon_compte.depot(100)
print(mon_compte)
mon_compte.retrait(100)
print(mon_compte)
# b
compte_ines.retrait(100)
compte_jordi.depot(100)
print(compte_ines)
print(compte_jordi)

# BONUS !!!!!!
virement(compte_ines, compte_jordi, 100)
print(compte_ines)
print(compte_jordi)