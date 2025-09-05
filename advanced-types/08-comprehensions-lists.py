users = [
    ['Carlos', 4],
    ['Alice', 2],
    ['Bob', 3],
    ['Jhon', 1]
]

# get a list of names based on the users list

# this is a good solution but not the most efficient
# names = []
# for user in users:
#     names.append(user[0])
# print(names)  # List of names

# a better way using list comprehension
# to transform also can use map function
names = [user[0] for user in users]
print('names:', names)  # List of names

# to filter we can also use filter function
# for example user with id greater than 2
filtered_users = [user for user in users if user[1] > 2]
# Filtered list of users with id greater than 2
print('filtered_users:', filtered_users)

# to filter and transform
filtered_users_names = [user[0] for user in users if user[1] > 2]
# Filtered list of names with id
print('filtered_users_names:', filtered_users_names)

# examples using map and filter functions
names_map = list(map(lambda user: user[0], users))
print('names_map:', names_map)  # List of names using map

names_filter = list(filter(lambda user: user[1] > 2, users))
print('names_filter:', names_filter)  # Filtered list of users with id greater than 2
