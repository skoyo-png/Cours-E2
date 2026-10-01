class Product:
    def __init__(self, code, name, price):
        self.code = str(code)
        self.name = str(name)
        self.price = float(price)

    def __str__(self):
        return f"Product(code={self.code}, name={self.name}, price={self.price})"

def get_price_it(self):
    taxe = float(input("Entrez le taux de taxe (en pourcentage) : "))
    return self.price + (self.price * taxe / 100)

print(Product("0001", "Produit", 5.0))
print(get_price_it(Product("0001", "Produit", 5.0)))