class Identite:
    """ Identite(str, str, int) -> Identite
        Classe représentant l'identité d'une personne """

    def __init__(self, nom, prenom, annee):
        self.nom = nom
        self.prenom = prenom
        self.naissance = annee

    def age(self, annee):
        """ age(int) -> int
            Calcule l'âge de la personne 'self' au cours de l'année 'annee'. """
        return annee - self.naissance

# Exécution
hugo = Identite('Bonneau', 'Jean', 1970)
print(hugo.age(2020))