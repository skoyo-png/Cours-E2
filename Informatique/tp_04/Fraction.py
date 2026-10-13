class Fraction:
    def __init__(self, numerateur, denominateur):
        self.numerateur = numerateur
        self.denominateur = denominateur
        if denominateur == 0:
            return ValueError("Le dénominateur ne peut pas être nul.")

        if denominateur < 0:
            self.numerateur = -numerateur
            self.denominateur = -denominateur

        def __str__(self):
            return f"{self.numerateur}/{self.denominateur}"

        def addition(self, other):
            if isinstance(other, Fraction):
                numerateur = self.numerateur * other.denominateur + other.numerateur * self.denominateur
                denominateur = self.denominateur * other.denominateur
                return Fraction(numerateur, denominateur)
            else:
                return TypeError("L'opération n'est pas définie pour ce type.")

        def soustraction(self, other):
            if isinstance(other, Fraction):
                numerateur = self.numerateur * other.denominateur - other.numerateur * self.denominateur
                denominateur = self.denominateur * other.denominateur
                return Fraction(numerateur, denominateur)
            else:
                return TypeError("L'opération n'est pas définie pour ce type.")

        def multiplication(self, other):
            if isinstance(other, Fraction):
                numerateur = self.numerateur * other.numerateur
                denominateur = self.denominateur * other.denominateur
                return Fraction(numerateur, denominateur)
            else:
                return TypeError("L'opération n'est pas définie pour ce type.")

        def division(self, other):
            if isinstance(other, Fraction):
                if other.numerateur == 0:
                    return ValueError("Division par zéro.")
                numerateur = self.numerateur * other.denominateur
                denominateur = self.denominateur * other.numerateur
                return Fraction(numerateur, denominateur)
            else:
                return TypeError("L'opération n'est pas définie pour ce type.")

        def inferieur(self, other):
            if isinstance(other, Fraction):
                return self.numerateur * other.denominateur < other.numerateur * self.denominateur
            else:
                return TypeError("L'opération n'est pas définie pour ce type.")

        def superieur(self, other):
            if isinstance(other, Fraction):
                return self.numerateur * other.denominateur > other.numerateur * self.denominateur
            else:
                return TypeError("L'opération n'est pas définie pour ce type.")

        def inferieur_ou_egal(self, other):
            if isinstance(other, Fraction):
                return self.numerateur * other.denominateur <= other.numerateur * self.denominateur
            else:
                return TypeError("L'opération n'est pas définie pour ce type.")

        def superieur_ou_egal(self, other):
            if isinstance(other, Fraction):
                return self.numerateur * other.denominateur >= other.numerateur * self.denominateur
            else:
                return TypeError("L'opération n'est pas définie pour ce type.")
            
        def strictement_egal(self, other):
            if isinstance(other, Fraction):
                return self.numerateur * other.denominateur == other.numerateur * self.denominateur
            else:
                return TypeError("L'opération n'est pas définie pour ce type.")

        def différent_ou_egal(self, other):
            if isinstance(other, Fraction):
                return self.numerateur * other.denominateur != other.numerateur * self.denominateur
            else:
                return TypeError("L'opération n'est pas définie pour ce type.")