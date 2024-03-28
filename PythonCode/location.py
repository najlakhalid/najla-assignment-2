from PythonCode.entity import Entity

class Location(Entity):
    locations = [] #Create a Instance or Dummy data in it Dynamically

    def __init__(self, name, capacity):
        super().__init__()
        self.name = name
        self.capacity = capacity
        Location.locations.append(self)

    @classmethod
    def create_location(cls):
        name = input("Enter location name: ")
        capacity = int(input("Enter capacity: "))
        return Location(name, capacity)

    @classmethod
    def display_locations(cls):
        for location in cls.locations:
            print(f"Location ID: {location.id}")
            print(f"Name: {location.name}")
            print(f"Capacity: {location.capacity}")
            print("-" * 20)
#These represent as an example as I show In UML
class PermanentGallery(Location):
    pass

class ExhibitionHall(Location):
    pass

class OutdoorSpace(Location):
    pass
