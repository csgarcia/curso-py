pets = ["dog", "cat", "fish", "bird", "hamster"]

pets.insert(1, "rabbit")  # Insert "rabbit" at index 1
print(pets)  # Updated list with "rabbit"

# adding at the end
pets.append("turtle")
print(pets)  # Updated list with "turtle"

# remove via element
pets.remove("fish")  # Remove "fish" from the list
print(pets)  # Updated list without "fish"

# remove last element
pets.pop()  # Remove the last element
print(pets)  # Updated list without the last element

# remove via index
pets.pop(2)  # Remove the element at index 2
# del pets[2]  # Another way to remove the element at index 2
print(pets)  # Updated list without the element at index 2

# clear the list
pets.clear()  # Remove all elements from the list
print(pets)  # Empty list
