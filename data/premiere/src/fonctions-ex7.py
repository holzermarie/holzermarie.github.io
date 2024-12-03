def distance_au_carre(x1, y1, x2, y2):
    return (x2-x1)**2+(y2-y1)**2
  
def est_rectangle(xa, ya, xb, yb, xc, yc):
    ab2 = distance_au_carre(xa, ya, xb, yb)
    ac2 = distance_au_carre(xa, ya, xc, yc)
    bc2 = distance_au_carre(xb, yb, xc, yc)
    if ab2 == ac2+bc2 :
        return True
    if ac2 == ab2+bc2 :
        return True
    if bc2 == ab2+ac2 :
        return True
    return False

# Variante avec produits scalaires
def produit_scalaire(ux, uy, vx, vy):
    return ux*vx + uy*vy
    
def est_angle_droit(xa, ya, xb, yb, xc, yc):
    """ renvoie True ssi l'angle en A est droit"""
    ux = xb-xa
    uy = yb-ya
    vx = xc-xa
    vy = yc-ya
    return produit_scalaire(ux, uy, vx, vy)==0
    
def est_rectangle_bis(xa, ya, xb, yb, xc, yc):
    return (    est_angle_droit(xa, ya, xb, yb, xc, yc)
            or  est_angle_droit(xc, yc, xa, ya, xb, yb)
            or  est_angle_droit(xb, yb, xc, yc, xa, ya,)
           )


print(est_rectangle(5, 2, 2, 2, 2, 6)) 

print(est_rectangle_bis(5, 2, 2, 2, 2, 6))