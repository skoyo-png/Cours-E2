class Product:
    flat_tax = 0.2 
    def __init__(self, code, name, price):
        self.code = str(code)
        self.name = str(name)
        self.price = float(price)

    def get_price_it(self,tax):
        return self.price * (1 + tax)

    def get_price_it_flat(self):
        return self.price * (1 + Product.flat_tax)
    
    def __str__(self):
        return f"{self.code} - {self.name} - {round(self.get_price_it_flat(), 2)}"

from Product import Product

p1 = Product("FR0001", "Stylo Rouge", 10)
p2 = Product("FR0007", "Stylo Violet", 0.99)

print(f"{p1.code} - {p1.name} - {p1.get_price_it(0.2)}")
print(f"{p2.code} - {p2.name} - {p2.get_price_it(0.2)}")


Product.flat_tax = 0.5

print(f"{p1.code} - {p1.name} - {p1.get_price_it_flat()}")
print(p2)