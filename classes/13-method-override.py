class Bird:

    def __init__(self):
        self.flying = "Yes it can fly"

    def fly(self):
        print("Flying")


class Duck(Bird):

    def __init__(self):
        super().__init__()
        self.swimming = "Yes it can swim"

    def fly(self):
        super().fly()  # Super is giving control to the parent class (Bird)
        print("Duck is flying")


duck = Duck()
duck.fly()  # Duck is flying, not using Bird's fly method
print(duck.flying)  # Yes it can fly
print(duck.swimming)  # Yes it can swim