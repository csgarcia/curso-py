# list = list([1, 2, 3])

# list.append(4)
# list.insert(0, 0)

# print(list)   # Output: [0, 1, 2, 3, 4]

class List(list):
    def prepend(self, item):
        self.insert(0, item)

list = List([1, 2, 3])
list.append(4)

list.prepend(0)

print(list)   # Output: [0, 1, 2, 3, 4]