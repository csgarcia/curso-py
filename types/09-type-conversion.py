x = input("Enter a number: ")

# int() conversion
# str() conversion
# float() conversion
# bool() conversion
## Bool use false and truthy values
### false values: 0, '', [], {}, None
### truthy values: 1, 'text', [1, 2], {'key': 'value'}, True
print(bool(""))  # Output: False
print(bool("Hello"))  # Output: True
print(bool(0))  # Output: False
print(bool(None))  # Output: True
print(bool(" ")) # Output: True
print(bool([]))  # Output: False
