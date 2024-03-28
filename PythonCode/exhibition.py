from PythonCode.entity import Entity, validate_date
from PythonCode.location import Location
class Exhibition(Entity):
    #Create a Instance or Dummy data in it Dynamically
    exhibitions = []

    def __init__(self, name, start_date, end_date, location):
        self.id = self.generate_id()
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.location = location
        self.artworks = []
        Exhibition.exhibitions.append(self)
    
    @classmethod
    def display_exhibition(cls):
        if not cls.exhibitions:
            print("No exhibitions available.")
            return
        for exhibition in cls.exhibitions:
            print(f"Exhibition ID: {exhibition.id}")
            print(f"Name: {exhibition.name}")
            print(f"Start Date: {exhibition.start_date}")
            print(f"End Date: {exhibition.end_date}")
            print(f"Location: {exhibition.location.name}")
            print("Artworks:")
            for artwork in exhibition.artworks:
                print(f"    {artwork.title} by {artwork.artist}")
            print("-" * 20)
