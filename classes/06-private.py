class Dog:

    # self is the instance of the class
    def __init__(self, name, age):
        self.__name = name  # __ makes the variable private
        self.age = age

    def speak(self):  # cls is the class itself
        print(f"{self.__name} says Woof!")

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    @classmethod
    def factory(cls):
        return cls("Buddy", 4)


dog1 = Dog.factory()  # Using the factory method to create an instance
dog1.speak()  # Calling the speak method of the Dog instance
print(dog1.get_name())
