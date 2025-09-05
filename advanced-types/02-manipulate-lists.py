pets = ["dog", "cat", "fish", "bird"]
print(pets[0])  
pets[0] = "Big Dog"
print(pets)  # Updated list with "Big Dog"
print(pets[0:3]) # Slicing the first three elements
print(pets[-1])  # Accessing the last element
print(pets[::2]) # Every second element

numbers = list(range(21))  # List of numbers from 0 to 20
print(numbers[1::2])  # Slicing every second number starting from index 1