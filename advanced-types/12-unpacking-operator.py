list = [1, 2, 3, 4, 5]
list2 = [6, 7, 8]
# unpacking operator (*) can be used to unpack elements of a list or tuple
print(*list)  # Output: 1 2 3 4 5

combined_list = [*list, *list2]
print(*combined_list)  # Output: 1 2 3 4 5 6 7 8

# for dictionaries, the unpacking operator can be used to merge dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

combined_dict = {**dict1, **dict2, "e": 5}
print(combined_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
