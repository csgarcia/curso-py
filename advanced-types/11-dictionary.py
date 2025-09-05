# Dictionary is a collection of key-value pairs
# Each key is unique and maps to a value

point = {'x': 1, 'y': 2}
print(point)  # Output: {'x': 1, 'y': 2}
print(point['x'])  # Output: 1
print(point['y'])  # Output: 2

# Adding a new key-value pair
point['z'] = 3
print(point)  # Output: {'x': 1, 'y': 2, 'z': 3}

# accessing a non-existent key raises KeyError
# print(point['a'])  # Uncommenting this line will raise KeyError
if 'a' in point:
    print(point['a'])  # Output: None (does not raise error)

# accessing via get method
print(point.get('x'))  # Output: 1
print(point.get('a'))  # Output: None (does not raise error)
print(point.get('a', 'default_value'))  # Output: default_value

# delete a key-value pair
del point['x']
print(point)  # Output: {'y': 2, 'z': 3}
point['x'] = 1  # Re-adding key 'x'

# read via for loop
for key in point:
    print(f"{key}: {point[key]}")  # Output: y: 2, z: 3, x: 1

# point.items() converts the dictionary into a list of tuples (key, value)
for key, value in point.items():
    print(f"{key}: {value}")  # Output: y: 2, z: 3, x: 1

# Dictionary Example for users

users = [
    {"id": 1, 'name': 'Alice', 'age': 30, 'city': 'New York'},
    {"id": 2, 'name': 'Bob', 'age': 25, 'city': 'Los Angeles'},
    {"id": 3, 'name': 'Charlie', 'age': 35, 'city': 'Chicago'}
]

for user in users:
    print(user["name"])
