class Chien:
    def __init__(self, nom, poids):
        self.... = nom
        self.... = poids

    def donne_nom(self):
        return self....

    def ...(self):
        return self....

    def machouille(self, jouet):
        resultat = ""
        for i in range(...):
            resultat += jouet[...]
        return ...

    def ...(self, ...):
        ...

    def ...(self, ration):
        if ...:
            ...
            return True
        else:
            return ...


# Tests
medor = Chien('Médor', 12.0)
assert medor.donne_nom() == 'Médor'
assert medor.donne_poids() == 12.0
assert medor.machouille('bâton') == 'bâto'
assert medor.aboie(3) == 'OuafOuafOuaf'
assert not medor.mange(2.0)
assert medor.mange(1.0)
assert medor.donne_poids() == 13.0
assert medor.mange(1.3)