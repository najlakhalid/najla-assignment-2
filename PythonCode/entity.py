import datetime
#Incremented integerId Id
class Entity:
    last_id = 0

    def __init__(self):
        self.id = self.generate_id()

    @classmethod
    def generate_id(cls):
        cls.last_id += 1
        return cls.last_id
 #Date Time validator 
def validate_date(date_string):
    try:
        datetime.datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False
