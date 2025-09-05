numbers = [5, 2, 9, 1, 5, 6]

# sort the list
# numbers.sort()
# print(numbers)  # Sorted list

# # sort in reverse order
# numbers.sort(reverse=True)
# print(numbers)  # Sorted list in reverse order

# order and return new list
numbers_sorted = sorted(numbers, reverse=True)
print(numbers)  # Original list remains unchanged
print(numbers_sorted)  # Sorted list without modifying the original

users = [[4, 'Jhon'], [2, 'Alice'], [3, 'Bob'], [1, 'Charlie']]
users.sort()
print(users)  # Sorted by the first element of each sublist


# sort by the second element of each sublist
users_2 = [['Carlos', 4], ['Alice', 2], ['Bob', 3], ['Jhon', 1]]
def sort_by_second(user):
    return user[1]

# users_2.sort(key=sort_by_second)
# print(users_2)  # Sorted by the second element of each sublist

# using lambda function to sort by the second element
users_2.sort(key=lambda el: el[1])
print(users_2)  # Sorted by the second element of each sublist