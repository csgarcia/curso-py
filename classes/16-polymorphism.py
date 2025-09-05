class User():
    def save(self):
        print("User saved")


class Session():
    def save(self):
        print("Session saved")


def save(entities):
    for entity in entities:
        entity.save()


user = User()
session = Session()
save([user, session])  # User saved Session saved
