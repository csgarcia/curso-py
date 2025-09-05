from abc import ABC, abstractmethod


class Model(ABC):
    def __init__(self):
        if not self.table:
            print("Table does not exist")

    @property
    @abstractmethod
    def table(self):
        pass

    @abstractmethod
    def save(self):
        print(f"Saving in the table {self.table}")

    @classmethod
    def search_by_id(self, id):
        print(f"Searching in the table {self.table} for id {id}")


class User(Model):
    table = "users"

    def save(self):
        print("User saved")


# model = Model()  # Table does not exist
# model.save()  # Table does not exist
# Model.search_by_id(1)  # Table does not exist

user = User()  # No output, as table exists
user.save()  # Saving in the table users
User.search_by_id(1)  # Searching in the table users for id 1
