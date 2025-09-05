class Animal:
    def eat(self):
        print("El animal está comiendo")


class Dog(Animal):
    def walk(self):
        print("El perro está caminando")


class Pig(Dog):
    def run(self):
        print("El cerdo está corriendo")


dog = Dog()
dog.eat()  # Inherited from Animal
dog.walk()  # Defined in Dog

pig = Pig()
pig.eat()  # Inherited from Animal
pig.walk()  # Inherited from Dog
pig.run()  # Defined in Pig