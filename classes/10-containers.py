class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Producto: {self.name}, Precio: {self.price}"


class Category:
    products = []

    def __init__(self, name, products):
        self.name = name
        self.products = products

    def add_products(self, product):
        self.products.append(product)

    def print(self):
        for product in self.products:
            print(product)


kayak = Product("Kayak", 250)
bycicle = Product("Bicicleta", 150)
surfboard = Product("Tabla de Surf", 300)

sports = Category("Deportes", [kayak, bycicle])
sports.add_products(surfboard)

sports.print()
