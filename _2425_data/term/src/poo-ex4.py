class Bim:
    """ Bim(str, int, float) -> Bim
    Classe représentant un bien immobilier
    """
    def __init__(self, nature, surface, prix_moyen):
        # à compléter
        
    def estime_prix(self):
        return self.surface * self.prix_moyen

    def modifie_prix_moyen(self, prix):
        """ modifie_prix_moyen(float) -> None
        Modifie le prix au métre carré
        """
        self.prix_moy = prix

    def est_moins_cher(self, autre_bien):
        """ est_moins_cher(Bim) -> bool
        param: autre_bien est un objet, instance la classe Bim
        Renvoie True si le prix estimé de self est strictement inférieur à celui de autre_bien et False sinon
        """
        return # à compléter