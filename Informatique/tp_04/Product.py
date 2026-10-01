class Product:
    def __init__(self, code, name, price):
        self.code = str(code)
        self.name = str(name)
        self.price = float(price)

    def __str__(self):
        return f"{self.code} - {self.name} - {self.price}"

taxe = float(input("Entrez le taux de taxe (en pourcentage) : "))
def get_price_it(self):
    return self.price + (self.price * taxe / 100)


name_products = [("001", "Clavier", 50) , ("002", "Souris", 30), ("003", "Ecran", 200), ("004", "Ordinateur", 1000)]

def create_products(name_products):
    return [Product(code, name, price) for code, name, price in name_products]

products = create_products(name_products)
print(products[0])
for p in products:
    print(p)