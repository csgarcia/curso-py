class Animal:
    def eat(self):
        print("comiendo")


class Dog():
    def walk(self):
        print("caminando al Perro")


class Pig(Dog, Animal):
    def run(self):
        print("corriendo")


pig = Pig()
pig.eat()  # Inherited from Animal
pig.walk()  # Inherited from Dog
