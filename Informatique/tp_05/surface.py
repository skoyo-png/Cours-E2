class Rectangle:
    def __init__(self, longueur, largeur, nom):
        self.longueur = longueur
        self.largeur = largeur
        self.nom = str(nom)

    def methode_affichage_surface(self):
        return (f"La surface du {self.nom} est {self.longueur}cm * {self.largeur}cm =")

    def methode_calcul_surface(self):
        return (f"{self.longueur * self.largeur}cm²")

#test = Rectangle(5, 10, "Rectangle")
#print(test.methode_affichage_surface(),  test.methode_calcul_surface())

class Carre(Rectangle):
    def __init__(self, cote, nom):
        super().__init__(cote, cote, nom)

#test_carre = Carre(5, "Carré")
#print(test_carre.methode_affichage_surface(), test_carre.methode_calcul_surface())