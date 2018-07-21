#July 21st 2018

class Car():
    """simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """initialise attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_mileage(self):
        """Print a statment showing vehicle mileage"""
        print("This car has " + str(self.mileage) + " miles on it.")
#modify attribute values through a method
    def update_mileage(self, mileage):
        """Set milage to a given value"""
        self.mileage = mileage

my_new_car = Car("mercedes-benz" ,"a-class", 2018)
print(my_new_car.get_descriptive_name())
my_new_car.update_mileage(23)
my_new_car.read_mileage()
