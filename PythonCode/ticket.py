from PythonCode.entity import Entity, validate_date
from PythonCode.pricing_strategy import BasePricingStrategy  
import datetime
class Ticket(Entity):
     # List to store instances of Ticket class
    tickets = []
    def __init__(self, exhibition, visitor, date, ticket_type, pricing_strategy):    # Constructor method to initialize a Ticket object
        self.id = self.generate_id()
        self.exhibition = exhibition
        self.visitor = visitor
        self.date = date
        self.ticket_type = ticket_type
        self.price = pricing_strategy.calculate_price(visitor)
        self.purchase_time = datetime.datetime.now()
        Ticket.tickets.append(self)
    @classmethod
    def display_a_receipt(cls, visitor_id):
        # Find tickets for the given visitor
        visitor_tickets = [ticket for ticket in cls.tickets if ticket.visitor.id == visitor_id]
        if not visitor_tickets:
            print("No tickets found for this visitor.")
            return

        # Sort tickets by purchase time and group by transactions (if multiple purchases at the same time)
        visitor_tickets.sort(key=lambda ticket: ticket.purchase_time)
        
        print("--------- TICKET RECEIPT ---------")
        for ticket in visitor_tickets:
            print(f"Date of Purchase: {ticket.purchase_time.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Ticket ID: {ticket.id}")
            print(f"Visitor Name: {ticket.visitor.name}")
            print(f"Exhibition: {ticket.exhibition.name}")
            print(f"Date of Event: {ticket.date}")
            print(f"Type: {ticket.ticket_type}")
            print(f"Price: {ticket.price:.2f}")
            print("-" * 30)
        
        total_price = sum(ticket.price for ticket in visitor_tickets)
        print(f"Total Price: {total_price:.2f}")
        print(f"Included VAT: {(total_price * BasePricingStrategy.VAT_RATE):.2f}")
        print("Thank you for your purchase!")
        print("-------------------------------")
    @classmethod
    def display_tickets(cls):
        if not cls.tickets:
            print("No tickets available.")
            return
        
        for ticket in cls.tickets:
            print(f"Ticket ID: {ticket.id}, Visitor Name: {ticket.visitor.name}, Exhibition: {ticket.exhibition.name}, Date of Event: {ticket.date}, Type: {ticket.ticket_type}, Price: {ticket.price}")
            print("-" * 40)
