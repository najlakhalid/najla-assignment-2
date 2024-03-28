from PythonCode.entity import Entity

class Visitor(Entity):
     #Create a Instance or Dummy data in it Dynamically
    visitors = []

    def __init__(self, name, age, visitor_type):
        self.id = self.generate_id()
        self.name = name
        self.age = age
        self.visitor_type = visitor_type
        self.tickets = []
        Visitor.visitors.append(self)
        
    @classmethod
    def display_visitors(cls):
        if not cls.visitors:
            print("No visitors available.")
            return
        for visitor in cls.visitors:
            print(f"Visitor ID: {visitor.id}")
            print(f"Name: {visitor.name}")
            print(f"Age: {visitor.age}")
            print(f"Type: {visitor.visitor_type}")
            print("Tickets:")
            for ticket in visitor.tickets:
                print(f"    {ticket.exhibition.name} on {ticket.date}")
            print("-" * 20)
            do the same with other files change  the
        i open them from where
