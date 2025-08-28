# IMPORTS
from file import *

# CLASSES
class Pile():
    def __init__(self):
        self.f = File()
        self.f_bis = File() # doit rester vide
        
    def empile(self, element):
        assert self.f_bis.est_vide()
        self.f.enfile(element)
        
    def depile(self):
        assert self.f_bis.est_vide()
        assert self.f.taille() > 0, "Impossible de dépiler car la pile est vide"
        while self.f.taille() > 1:
            self.f_bis.enfile(self.f.defile())
            
        tete_pile = self.f.defile()
        
        while not self.f_bis.est_vide():
            self.f.enfile(self.f_bis.defile())
        
        return tete_pile
        
    def est_vide(self):
        assert self.f_bis.est_vide()
        return self.f.taille() == 0
    
    def taille(self):
        assert self.f_bis.est_vide()
        return self.f.taille()
    
    def __str__(self):
        data = self.f._get_data().copy()
        if data == [] :
            return "||"
        data.reverse()
        w = max([len(str(e)) for e in data])
        s = "-"*(w+4)+"\n"
        for e in data:
            s+= "| "+str(e).center(w)+" |\n"
        s += "-"*(w+4)
        return s
    

# SCRIPT

pile = Pile()
pile.empile(1)
pile.empile(2)
pile.empile(3)
pile.empile(4)
print(pile)