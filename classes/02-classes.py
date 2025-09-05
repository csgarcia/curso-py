class Dog:  # Pascal case for class names
    def speak(self):  # these are methods
        print("Woof!")


dog = Dog()
# print(type(dog)) # This will show that dog is an instance of the Dog class
dog.speak()  # Calling the method of the Dog class
print(isinstance(dog, Dog))  # This checks if dog is an instance of Dog class
