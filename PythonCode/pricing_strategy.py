from PythonCode.visitor import Visitor
class BasePricingStrategy:
    VAT_RATE = 0.05

    def calculate_price(self, visitor_type):
        if isinstance(visitor_type, Visitor):
            visitor_type = visitor_type.visitor_type
            
        if visitor_type in ["child", "senior", "teacher", "student"]:
            return 0
        elif visitor_type == "group":
            return 31.5  # Adjusted base price including VAT for groups
        return 63 * (1 + BasePricingStrategy.VAT_RATE)  # Base price including VAT for adults

class SpecialEventPricing(BasePricingStrategy):
    def __init__(self, event_price):
        self.event_price = event_price

    def calculate_price(self, visitor_type):
        if isinstance(visitor_type, Visitor):
            visitor_type = visitor_type.visitor_type

        base_price = self.event_price if visitor_type == "special" else 0
        return base_price * (1 + self.VAT_RATE)
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
    
