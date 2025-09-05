class Model():
    table = False

    def __init__(self):
        if not self.table:
            print("Table does not exist")

    def save(self):
        print(f"Saving in the table {self.table}")

    @classmethod
    def search_by_id(self, id):
        print(f"Searching in the table {self.table} for id {id}")


class User(Model):
    table = "users"


user = User()
user.save()
user.search_by_id(1)
