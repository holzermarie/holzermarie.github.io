class Pile :
    def __init__(self):
        self.__data = []
        
    def empile(self, el):
        self.__data.append(el)
        
    def depile(self):
        assert len(self.__data)>0, "Impossible de dépiler car la pile est vide"
        return self.__data.pop()
        
    def est_vide(self):
        return self.__data == []
        
    def __str__(self):
        data = self.__data.copy()
        if data == [] :
            return "||"
        data.reverse()
        w = max([len(str(e)) for e in data])
        s = "-"*(w+4)+"\n"
        for e in data:
            s+= "| "+str(e).center(w)+" |\n"
        s += "-"*(w+4)
        return s

