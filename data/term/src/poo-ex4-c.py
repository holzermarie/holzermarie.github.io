class Bim:
    def __init__(self, nature, surface, prix_moyen):
        """ Bim(str, int, float) -> Bim
            Classe représentant un bien immobilier """
        self.nature = nature
        self.surface = surface
        self.prix_moyen = prix_moyen
        
    def prev_estime_prix(self):
        """ estime_prix() -> float
            Estime le prix d'un bien immobilier en fonction de sa surface et du prix moyen. """
        return self.surface * self.prix_moyen
    
    def estime_prix(self):
        """ estime_prix() -> float
            Estime le prix d'un bien immobilier en fonction de sa surface et du prix moyen,
            pondéré par la nature du bien. """       
        coeff = 1
        if self.nature == 'maison':
            coeff = 1.1
        elif self.nature == 'bureau':
            coeff = 0.8
            
        return self.surface * self.prix_moyen * coeff

    def prev_modifie_prix_moyen(self, prix):
        """ modifie_prix_moyen(float) -> None
            Modifie le prix moyen d'un bien immobilier, c'est-à-dire indique son nouveau prix au métre carré. """
        self.prix_moy = float(prix)
        
    def modifie_prix_moyen(self, prix):
        """ modifie_prix_moyen(float) -> None
            Modifie le prix moyen d'un bien immobilier, c'est-à-dire indique son nouveau prix au métre carré. """
        self.prix_moyen = float(prix)

    def est_moins_cher(self, autre_bien):
        """ est_moins_cher(Bim) -> bool
            Renvoie 'True' si le prix estimé de 'self' est strictement inférieur à celui de 'autre_bien' et 'False' sinon. """
        return self.estime_prix() < autre_bien.estime_prix()
    

# La fonction est bien en dehors de la classe ! Elle ne s'applique pas à un objet.
def compte_maison(lst_biens):
    nb = 0
    for bien in lst_biens:
        if bien.nature == 'maison':
            nb += 1
    return nb
    
    
bim = Bim("appartement", 30, 8000.)
bien1 = Bim("maison", 70, 2000.)
# print(bien1.estime_prix_prev())
# print(bien1.estime_prix())
# print(bien1.prix_moyen)
bien1.modifie_prix_moyen(2500.0)
# print(bien1.prix_moyen)
# print(bien1.prix_moy)

print(bien1.est_moins_cher(bim))
print(compte_maison([bim, bien1]))