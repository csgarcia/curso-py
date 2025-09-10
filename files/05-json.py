import json
from pathlib import Path

# products = [
#     {"id": 1, "name": "Product 1", "price": 10.5},
#     {"id": 2, "name": "Product 2", "price": 20.0},
#     {"id": 3, "name": "Product 3", "price": 30.99},
# ]

# data = json.dumps(products)  # convert to JSON string
# Path("files/products.json").write_text(data)

# read json
data = Path("files/products.json").read_text("utf-8")
products = json.loads(data)  # convert JSON string to Python object
print(products)

# modify json
products[0]["name"] = "Modified Product 1"
Path("files/products.json").write_text(json.dumps(products))
