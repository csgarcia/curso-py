# set means group or collection of items
# set is unordered, unindexed, and does not allow duplicate items

test_set = {1, 1, 2, 2, 3, 4, 5 }
print(test_set)  # Output: {1, 2, 3, 4, 5}

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Convert list to set to remove duplicates
unique_numbers = set(numbers)
print(unique_numbers)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)  # Output: {1, 2, 3, 4, 5}

# intersection of two sets
print(set1 & set2)  # Output: {3}

# difference of two sets (opposite of intersection)
# this removes items in set2 from set1
print(set1 - set2)  # Output: {1, 2}

# symmetric difference of two sets
# this removes items that are in both sets
print(set1 ^ set2)  # Output: {1, 2, 4, 5}