class Coordinates:
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng

    def __eq__(self, other):
        return self.lat == other.lat and self.lng == other.lng

    def __ne__(self, other):
        return self.lat != other.lat or self.lng != other.lng

    def __lt__(self, other):  # less than
        return (self.lat + self.lng) < (other.lat + other.lng)

    def __le__(self, other):  # less than or equal
        return (self.lat + self.lng) <= (other.lat + other.lng)


coords = Coordinates(10, 20)
coords2 = Coordinates(10, 20)

print(coords == coords2)  # Output: True

print(coords != coords2)  # Output: False

print(coords < coords2)  # Output: False

print(coords <= coords2)  # Output: True

print(coords >= coords2)  # Output: True
