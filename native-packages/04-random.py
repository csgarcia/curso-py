import random
import string

print(random.random())  # float: 0.0 <= x < 1.0
print(random.randint(1, 10))  # int: 1 <= x <= 10 (inclusive)
list = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
random.shuffle(list)
print(list)  # shuffle list in place

print(random.choice(list2))  # choose one element from the list

# choose k elements from the list (with replacement)
print(random.choices(list2, k=3))

# choose k elements from the list (without replacement)
print("".join(random.sample("abcdefghijk,.@", k=5)))

# Generate a random password
chars = string.ascii_letters
digits = string.digits
selection = random.choices(chars + digits, k=16)
password = "".join(selection)
print("Password:", password)
