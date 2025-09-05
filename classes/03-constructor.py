class Dog:
    # self is the instance of the class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} says: Woof!")


dog = Dog("Buddy", 3)  # Creating an instance of Dog with the name "Buddy" and age 3
dog.speak()  # Calling the speak method of the Dog instance
