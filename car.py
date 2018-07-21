#July 21st 2018

class Car():
    """simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """initialise attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 10

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_mileage(self):
        """Print a statment showing vehicle mileage"""
        print("This car has " + str(self.mileage) + " miles on it.")
#modify attribute values through a method
    def update_mileage(self, mileage):
        """
        Set mileage to a given value.
        Reject mileage if lower than current"""
        self.mileage = mileage

    def increase_mileage(self, miles):
        """add a given amount to a vehicle mileage"""
        if miles >=0:
            self.mileage += miles
        else:
            print("You can't remove miles from an odometer!")
my_used_car = Car("toyota", "yaris", 2012)
print(my_used_car.get_descriptive_name())

my_used_car.update_mileage(23000)
my_used_car.read_mileage()

my_used_car.increase_mileage(100)
my_used_car.read_mileage()
