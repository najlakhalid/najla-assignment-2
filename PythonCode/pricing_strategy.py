from PythonCode.visitor import Visitor
class BasePricingStrategy:  # BasePricingStrategy class representing the base pricing strategy for tickets
    VAT_RATE = 0.05  # VAT rate applied to ticket prices
    
  # Method to calculate the ticket price based on visitor type
    def calculate_price(self, visitor_type):
        if isinstance(visitor_type, Visitor):   # Checking if its an instance of the Visitor class
            visitor_type = visitor_type.visitor_type # Extracting the visitor type from the Visitor instance
            
        if visitor_type in ["child", "senior", "teacher", "student"]:   # Checking visitor type and returning the appropriate ticket price
            return 0  # Free ticket for them 
        elif visitor_type == "group":
            return 31.5  # Adjusted base price including VAT for groups
        return 63 * (1 + BasePricingStrategy.VAT_RATE)  # Base price including VAT for adults

class SpecialEventPricing(BasePricingStrategy):   # class inheriting from BasePricingStrategy representing pricing for special events
    def __init__(self, event_price):
        self.event_price = event_price

    def calculate_price(self, visitor_type):
        if isinstance(visitor_type, Visitor):
            visitor_type = visitor_type.visitor_type

        base_price = self.event_price if visitor_type == "special" else 0    # Determining the base price based on visitor type and event price
        return base_price * (1 + self.VAT_RATE)   # Applying VAT to the base price
class PricingStrategy:
    def calculate_price(self, visitor):
        if visitor.visitor_type in ["child", "senior", "teacher"]:
            return 0
        elif visitor.visitor_type == "group":
            return 10  # Example group price
        return 20  # Example base price for adults

class DiscountPricing(PricingStrategy):
    def calculate_price(self, visitor):
        base_price = super().calculate_price(visitor)
        return base_price * 0.5  # 50% discount
    
