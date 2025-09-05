search_number = 10
# range corresponds to a iterable of numbers
# there is more iterables like lists, tuples, strings, etc.
for number in range(5):  # range returns numbers from 0 to 4
    print(number)  # This will print each number in the range on a new line
    if number == search_number:
        print(f"Number found: {search_number}")
        break
else:
    print(f"Number {search_number} was not found")

# iterate a char
for char in "This is a python course":
    print(char)
