from PythonCode.exhibition import Exhibition
from PythonCode.artwork import Artwork
from PythonCode.visitor import Visitor
from PythonCode.ticket import Ticket
from PythonCode.location import Location
from PythonCode.pricing_strategy import BasePricingStrategy,SpecialEventPricing
from PythonCode.entity import validate_date

def create_or_select_location():
    # Display existing locations if any
    if Location.locations:
        print("Available locations:")
        Location.display_locations()
        choice = input("Choose a location by ID, or type 'new' to create a new one: ")
        if choice.lower() == 'new':
            return Location.create_location()
        else:
            location_id = int(choice)
            location = next((locations for locations in Location.locations if locations.id == location_id), None)
            if location:
                return location
            else:
                print("Invalid selection. Creating a new location.")
                return Location.create_location()
    else:
        print("No existing locations. Please create a new one.")
        return Location.create_location()

def create_a_exhibition():
    location = create_or_select_location()
    name = input("Enter exhibition name: ")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    while not validate_date(start_date):
        start_date = input("Invalid date format. Please enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    while not validate_date(end_date):
        end_date = input("Invalid date format. Please enter end date (YYYY-MM-DD): ")
    
    exhibition = Exhibition(name, start_date, end_date, location)
    print(f"Exhibition '{name}' created successfully with location '{location.name}'.")


def create_artwork():
    if not Exhibition.exhibitions:
        print("No exhibitions available to add artwork to.")
        return
    Exhibition.display_exhibition()
    exhibition_id = int(input("Enter the exhibition ID to add artwork to: "))
    exhibition = next((ex for ex in Exhibition.exhibitions if ex.id == exhibition_id), None)
    if not exhibition:
        print("Exhibition not found.")
        return
    title = input("Enter artwork title: ")
    artist = input("Enter artist's name: ")
    date_of_creation = input("Enter date of creation (YYYY-MM-DD): ")
    while not validate_date(date_of_creation):
        date_of_creation = input("Invalid date format. Please enter date of creation (YYYY-MM-DD): ")
    historical_significance = input("Enter historical significance: ")
    Artwork(title, artist, date_of_creation, historical_significance, exhibition)

def create_visitor():
    name = input("Enter visitor's name: ")
    age = int(input("Enter visitor's age: "))
    visitor_type = input("Enter visitor type (adult, child, senior, group, special): ")
    while visitor_type not in ["adult", "child", "senior", "group", "special"]:
        visitor_type = input("Invalid visitor type. Please enter visitor type (adult, child, senior, group, special): ")
    Visitor(name, age, visitor_type)
def display_pricing_info():
    print("Ticket pricing:")

    # Display price for regular visitors
    regular_price = BasePricingStrategy().calculate_price("adult")
    print(f"Regular: ${regular_price:.2f} (including VAT)")

    # Display price for group visitors
    group_price = BasePricingStrategy().calculate_price("group")
    print(f"Group: ${group_price:.2f} (for groups, including VAT)")

    # Assume a base price for special events and display it
    special_event_base_price = 120  # This might be dynamically determined based on the event
    special_price = SpecialEventPricing(special_event_base_price).calculate_price("special")
    print(f"Special: ${special_price:.2f} (for special events, including VAT)")
def buy_ticket():
    if not Visitor.visitors:
        print("No visitors available.")
        return

    if not Exhibition.exhibitions:
        print("No exhibitions available.")
        return
    # Display dynamic pricing information
    display_pricing_info()
    # Display all visitors
    Visitor.display_visitors()
    # Get visitor ID input and validate
    visitor_id = int(input("Enter the visitor ID to buy a ticket for: "))
    visitor = next((v for v in Visitor.visitors if v.id == visitor_id), None)
    if not visitor:
        print("Visitor not found.")
        return

    # Display all exhibitions
    Exhibition.display_exhibition()
    # Get exhibition ID input and validate
    exhibition_id = int(input("Enter the exhibition ID to visit: "))
    exhibition = next((ex for ex in Exhibition.exhibitions if ex.id == exhibition_id), None)
    if not exhibition:
        print("Exhibition not found.")
        return

    # Get visit date input and validate
    date = input("Enter visit date (YYYY-MM-DD): ")
    while not validate_date(date):
        date = input("Invalid date format. Please enter visit date (YYYY-MM-DD): ")

    # Get ticket type input
    ticket_type = input("Enter ticket type (regular, group, special): ")
    # Define a pricing strategy (you could enhance this to choose different strategies)
    pricing_strategy = BasePricingStrategy()  # Simplified for this example; might choose based on context

    # Create the ticket
    new_ticket = Ticket(exhibition, visitor, date, ticket_type, pricing_strategy)

    # Display the receipt the visitor
    Ticket.display_a_receipt(visitor_id) 

def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Add an Exhibition")
        print("2. Add an Artwork")
        print("3. Add an Visitor")
        print("4. Buy a Ticket")
        print("5. Display a Exhibitions")
        print("6. Display a Artworks")
        print("7. Display a Visitors")
        print("8. Display a Purchase Tickets")
        print("9. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            create_a_exhibition()
        elif choice == '2':
            create_artwork()
        elif choice == '3':
            create_visitor()
        elif choice == '4':
            buy_ticket()
        elif choice == '5':
            Exhibition.display_exhibition()
        elif choice == '6':
            Artwork.display_artworks()
        elif choice == '7':
            Visitor.display_visitors()
        elif choice == '8':
            visitor_id = input("Enter the visitor ID to display tickets for: ")
            try:
                visitor_id = int(visitor_id)
                Ticket.display_a_receipt(visitor_id)
            except ValueError:
                print("Invalid input. Please enter a numeric visitor ID.")
        elif choice == '9':
            print("Exiting the program.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main_menu()
    
