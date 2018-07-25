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
        if mileage >= self.mileage:
            self.mileage = mileage
        else:
            print("You can't remove miles from an odometer")

    def increase_mileage(self, miles):
        """add a given amount to a vehicle mileage"""
        if miles >=0:
            self.mileage += miles
        else:
            print("You can't remove miles from an odometer!")

class Battery():
    """Simple battery modelling attempt"""

    def __init__(self, battery_size=70):
        """Initialise battery attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print statement describing battery size"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the mileage provided by this battery"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

class ElectricCar(Car):
    """Models aspects of a car, specific to EVs"""

    def __init__(self, make, model, year):
        """
        Initialise attributes of the parent class
        Then initialse attributes specific to EVs
        """
        super().__init__(make, model, year)
        self.battery = Battery()
