from PythonCode.entity import Entity, validate_date
from PythonCode.location import Location
class Exhibition(Entity): # Exhibition class representing exhibitions in the museum
    
     # List to store all instances of exhibitions
    exhibitions = []

    def __init__(self, name, start_date, end_date, location):  # Constructor method to initialize an Exhibition object
        self.id = self.generate_id()  # Assigning a unique ID to each exhibition
        self.name = name  # Setting the name of the exhibition
        self.start_date = start_date # Setting the start date of the exhibition
        self.end_date = end_date # Setting the end date of the exhibition
        self.location = location  # Setting the location of the exhibition
        self.artworks = [] # List to store artworks in the exhibition
        Exhibition.exhibitions.append(self)  # Adding the new exhibition instance to the list of exhibitions

      # Method to display information about all exhibitions
    @classmethod
    def display_exhibition(cls):
         # Checking if there are any exhibitions available
        if not cls.exhibitions:
            print("No exhibitions available.")
            return
             # Iterating through each exhibition instance and printing its details
        for exhibition in cls.exhibitions:
            print(f"Exhibition ID: {exhibition.id}")
            print(f"Name: {exhibition.name}")
            print(f"Start Date: {exhibition.start_date}")
            print(f"End Date: {exhibition.end_date}")
            print(f"Location: {exhibition.location.name}")
            print("Artworks:")
             # Iterating through each artwork in the exhibition and displaying its title and artist
            for artwork in exhibition.artworks:
                print(f"    {artwork.title} by {artwork.artist}")
            print("-" * 20) # Line separator
