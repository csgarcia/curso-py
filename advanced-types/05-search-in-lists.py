pets = ["dog", "cat", "fish", "bird", "dog"]

pets.index("cat")  # Find the index of "cat"
# print(pets.index("fish"))  # Find the index of "fish"

# print(pets.index("not_in_list"))  # This will raise a ValueError if "not_in_list" is not found
# if "not_in_list" in pets:
#     print("Found 'not_in_list'")

# see how many times "dog" appears in the list
print(pets.count("dog"))  # Count occurrences of "dog"