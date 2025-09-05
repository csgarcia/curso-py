class Dog:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        print("Getting name")
        return self.__name

    @name.setter
    def name(self, name):
        print("Setting name")
        if name.strip():
            self.__name = name
        return


dog = Dog("Buddy")
# dog = Dog(True) # avoid this
print(dog.name)  # Output: Buddy
