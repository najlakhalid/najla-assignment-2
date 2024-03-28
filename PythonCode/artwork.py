from PythonCode.entity import Entity, validate_date

class Artwork(Entity):
     #Create a Instance or Dummy data in it Dynamically
    artworks = []

    def __init__(self, title, artist, date_of_creation, historical_significance, exhibition):
        self.id = self.generate_id()
        self.title = title
        self.artist = artist
        self.date_of_creation = date_of_creation
        self.historical_significance = historical_significance
        self.exhibition = exhibition
        Artwork.artworks.append(self)
    
    @classmethod
    def display_artworks(cls):
        for artwork in cls.artworks:
            print(f"Artwork ID: {artwork.id}")
            print(f"Title: {artwork.title}")
            print(f"Artist: {artwork.artist}")
            print(f"Date of Creation: {artwork.date_of_creation}")
            print(f"Historical Significance: {artwork.historical_significance}")
            print(f"Exhibition: {artwork.exhibition.name}")
            print("-" * 20)
            
