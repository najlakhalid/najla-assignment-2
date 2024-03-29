import datetime # Importing the datetime module to work with dates and times
#Incremented integer Id for entities 
class Entity:
    last_id = 0  # Initializing the last_id attribute to track the last assigned ID

    def __init__(self):   # Constructor method to initialize an Entity object
        self.id = self.generate_id()   # Generating a unique ID for each Entity instance

      # Class method to generate a unique ID for each Entity instance
    @classmethod
    def generate_id(cls):
        cls.last_id += 1
        return cls.last_id
 #Date Time validator function
def validate_date(date_string):
    try:
        datetime.datetime.strptime(date_string, "%Y-%m-%d")  # It converts the string into a datetime object representing the parsed date
        return True  #returns True if the date string is successfully parsed into a datetime object,
    except ValueError:
        return False  # indicating that the date string is not in the correct format and does not represent a valid date.
