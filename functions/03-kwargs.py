def get_product(**data):
    print(data)
    print(data["name"], data["id"])


get_product(name="Laptop", price=1200, brand="BrandX", id=101)


def sum(a, b):
    return a + b

result = sum(5, 10)
print(f"The sum is: {result}") 