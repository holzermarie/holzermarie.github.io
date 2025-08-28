class Fraction:
    """ Fraction(int, int) -> Fraction
        Représente une fraction. """
    
    def __init__(self, numerateur, denominateur):
        if denominateur <= 0:
            raise ValueError("Le dénominateur doit être strictement positif.")

        self.numerateur = numerateur
        self.denominateur = denominateur

    def __str__(self):
        """ __str__() -> str
            Affiche la fraction sous la forme 'numerateur/denominateur' ou 'numerateur' si le dénominateur vaut 1. """
        if self.denominateur == 1:
            return str(self.numerateur)
        else:
            return f"{self.numerateur}/{self.denominateur}"
        
    def __eq__(self, frac):
        """ __eq__(Fraction) -> bool
            Renvoie True si les fractions 'self' et 'frac' sont égales. """
        return self.numerateur * frac.denominateur == self.denominateur * frac.numerateur

    def __lt__(self, frac):
        """ __lt__(Fraction) -> bool
            Renvoie True si la fraction 'self' est strictement inférieure à 'frac'. """
        return self.numerateur * frac.denominateur < self.denominateur * frac.numerateur

    def __add__(self, frac):
        """ __add__(Fraction) -> Fraction
            Renvoie un objet 'Fraction' résulat de la somme de la fraction 'self' et de la fraction 'frac'. """
        if self.denominateur == frac.denominateur:
            return Fraction(self.numerateur + frac.numerateur, self.denominateur)
        else:
            return Fraction(self.numerateur * frac.denominateur + frac.numerateur * self.denominateur, self.denominateur * frac.denominateur)

    def __mul__(self, frac):
        """ __mult__(Fraction) -> Fraction
            Renvoie un objet Fraction résulat du produit de la fraction 'self' et de la fraction 'frac'. """
        return Fraction(self.numerateur * frac.numerateur, self.denominateur * frac.denominateur)

    # BONUS, pas obligatoire !
    def rendre_irreductible(self):
        """ rendre_irreductible(Fraction) -> None
            Fonction bonus qui modifie un objet Fraction en l'écrivant sous forme irréductible. """
        if self.numerateur < self.denominateur:
            min = self.numerateur
        else:
            min = self.denominateur
        for i in range(2, min + 1):
            if self.numerateur % i == 0 and self.denominateur % i == 0:
                self.numerateur = self.numerateur // i
                self.denominateur = self.denominateur // i
                
f1 = Fraction(1, 2)
f2 = Fraction(1, 2)
f3 = Fraction(1, 3)
f4 = Fraction(2, 4)
f5 = Fraction(5, 1)

print(f1)

# BONUS
print(f4)
f4.rendre_irreductible()
print(f4)
print(f5)

print(f1 == f2)