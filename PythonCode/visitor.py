from PythonCode.entity import Entity

class Visitor(Entity):
      # List to store instances of Visitor class
    visitors = []

      # Constructor method to initialize a Visitor object
    def __init__(self, name, age, visitor_type):
        self.id = self.generate_id()
        self.name = name
        self.age = age
        self.visitor_type = visitor_type
        self.tickets = []
        Visitor.visitors.append(self)
        
    @classmethod    # Class method to display all visitors
    def display_visitors(cls):
        if not cls.visitors:
            print("No visitors available.")
            return
        for visitor in cls.visitors:     # Displaying information for each visitor
            print(f"Visitor ID: {visitor.id}")
            print(f"Name: {visitor.name}")
            print(f"Age: {visitor.age}")
            print(f"Type: {visitor.visitor_type}")
            print("Tickets:")
            for ticket in visitor.tickets:
                print(f"    {ticket.exhibition.name} on {ticket.date}")
            print("-" * 20)
           
