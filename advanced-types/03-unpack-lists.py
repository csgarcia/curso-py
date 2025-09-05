numbers = [1, 2, 3, 4, 5]
a, b, c, d, e = numbers
print(a, b, c, d, e)

a, *others = numbers
print(a)  # First element
print(others)  # Remaining elements as list
first, *other_numbers, last = numbers
print(first)  # First element
print(other_numbers)  # Middle elements as list
print(last)  # Last element