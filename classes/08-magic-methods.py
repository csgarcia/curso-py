# magic methods are special methods in Python that start and end with double underscores
# and are used to define the behavior of objects in certain situations

class Dog:
    def __init__(self, name, age): # this is a magic method
        self.name = name
        self.age = age

    def __del__(self):
        print(f"{self.name} is being deleted")

    def __str__(self):
        return f"Class Dog: {self.name}, {self.age} years old"

    def speak(self):
        print(f"{self.name} says Woof!")


dog = Dog("Buddy", 5)
print(dog)  # Output: Class Dog: Buddy, 5 years old
text = str(dog)  # Convert to string
print(text)  # Output: Class Dog: Buddy, 5 years old

del dog  # This will call the __del__ method