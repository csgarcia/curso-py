class Dog:
    legs = 4  # Class variable or attribute

    # self is the instance of the class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} says: Woof!")


Dog.legs = 3  # Changing the class variable for the Dog class
# Creating an instance of Dog with the name "Buddy" and age 3
dog = Dog("Buddy", 3)
dog.legs = 5  # Changing the instance variable for this specific instance
print(dog.legs)  # Accessing the instance variable
# dog.speak()  # Calling the speak method of the Dog instance
dog_2 = Dog("Max", 5)  # Creating another instance of Dog with the name "Max" and age 5
print(dog.legs)  # Accessing the instance variable
print(dog_2.legs)  # Accessing the class variable