# tuple is a collection of items that are ordered and immutable
# tuples are defined using parentheses (1, 2, 3)
# they can contain mixed data types

numbers = (1, 2, 3, 4, 5) + (6, 7, 8, 9, 10)
print('numbers:', numbers)  # Tuple of numbers

point = tuple([1, 2])

# we can use all functions that we can use with lists 
# except we cannot modify the tuple

# point.pop() # This will raise an error because tuples are immutable

first, second, *others = numbers
print('first:', first)  # First element of the tuple
print('second:', second)  # Second element of the tuple

