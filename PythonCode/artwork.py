from PythonCode.entity import Entity, validate_date

# Definition of the Artwork class, inheriting from the Entity class
class Artwork(Entity):
      # List to store all instances of artworks
    artworks = []

    def __init__(self, title, artist, date_of_creation, historical_significance, exhibition):  # Constructor method to initialize an Artwork object
        self.id = self.generate_id()
        self.title = title
        self.artist = artist
        self.date_of_creation = date_of_creation
        self.historical_significance = historical_significance
        self.exhibition = exhibition
        Artwork.artworks.append(self)  # Add the new artwork instance to the list of artworks

      # Class method to display information about all artworks
    @classmethod
    def display_artworks(cls):
        for artwork in cls.artworks:
            print(f"Artwork ID: {artwork.id}")
            print(f"Title: {artwork.title}")
            print(f"Artist: {artwork.artist}")
            print(f"Date of Creation: {artwork.date_of_creation}")
            print(f"Historical Significance: {artwork.historical_significance}")
            print(f"Exhibition: {artwork.exhibition.name}")
            print("-" * 20)  # Printing a separator line
            
