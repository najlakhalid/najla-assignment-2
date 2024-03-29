from PythonCode.entity import Entity

# Location class representing different locations in the museum
class Location(Entity):
    locations = [] # List to store instances of locations
    
# Constructor method to initialize a Location object
    def __init__(self, name, capacity):
        super().__init__()  # Calling the constructor of the base class Entity
        self.name = name # Setting the name of the location
        self.capacity = capacity # Setting the capacity of the location
        Location.locations.append(self) # Adding the location instance to the list of locations

# Class method to create a new location
    @classmethod
    def create_location(cls):
        name = input("Enter location name: ")
        capacity = int(input("Enter capacity: "))
        return Location(name, capacity)
        
# Class method to display information about all locations
    @classmethod
    def display_locations(cls):
        for location in cls.locations:
            print(f"Location ID: {location.id}")
            print(f"Name: {location.name}")
            print(f"Capacity: {location.capacity}")
            print("-" * 20)
#These represent as an example as I show in my  UML
class PermanentGallery(Location):
    pass

class ExhibitionHall(Location):
    pass

class OutdoorSpace(Location):
    pass
