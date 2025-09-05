animal = " happY Dog "
print(animal.upper())  # Convert to uppercase
print(animal.lower())  # Convert to lowercase
print(animal.strip().capitalize()) # Remove leading and trailing whitespace, then capitalize the first letter
print(animal.title())  # Capitalize the first letter of each word
print(animal.strip()) # Remove leading and trailing whitespace
print(animal.lstrip())  # Remove leading whitespace
print(animal.rstrip())  # Remove trailing whitespace
print(animal.find('Dog'))  # Find the index of the substring 'Dog'
print(animal.find('Cat')) # Find the index of the substring 'Cat' (not found, returns -1)
print(animal.replace('Dog', 'Cat'))  # Replace 'Dog' with 'Cat
print("Dog" in animal)  # Check if 'Dog' is in the string (returns True)
print("Dog" not in animal)  # Check if 'Dog' is not in the string (returns False)