# Méthode à ajouter dans votre calsse File
def __str__(self):
    data = self.__data.copy()
    if data == [] :
        return "->||->"
    data.reverse()
    w = max([len(str(e)) for e in data])
    s = ""
    ligne = "-"* ((w*len(data)+ 3*len(data))-1)
    s = "   " + ligne +"\n->|"
    for e in data:
        s+= " "+str(e).center(w)+" |"
    s += "->\n   " + ligne
    return s
