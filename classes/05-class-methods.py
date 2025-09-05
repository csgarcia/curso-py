class Dog:
    legs = 4  # Class variable or attribute

    # self is the instance of the class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def speak(cls): # cls is the class itself
        print("Woof!")

    @classmethod
    def factory(cls):
        return cls("Buddy", 4)


Dog.speak()  # Calling the class method of the Dog class
dog = Dog.factory()  # Using the factory method to create an instance
print(dog.name, dog.age)  # Accessing the name and age attributes of the Dog instance