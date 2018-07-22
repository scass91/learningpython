#July 22nd 2018
#An ice cream stand is a specific kind of restaurant. Write a class called
#IceCreamStand that inherits from the Restaurant class in restaurants.py
#Add an attribute called flavours, write a method which displays these
#flavours. Create an instance of IceCreamStand and call this method

class Restaurant():
    """A simple class describing restaurants and their cusisines"""

    def __init__(self, restaurant_name, cuisine_type):
        """initialise restaurant name and food type attributes"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def open_restaurant(self):
        """Let people know the restaurant is open!"""
        message = self.restaurant_name.title() + " is open!"
        print("\n" + message)

    def describe_restaurant(self):
        """Let people know what food is on offer"""
        message = self.restaurant_name.title() + " serves the best "
        + self.cuisine_type.title() + " food!"
        print("\n" + message)

class IceCreamStand(Restaurant):
    """Represents aspects of a restaurant, specific to an ice cream stand"""

    def __init__(self, restaurant_name, cuisine_type = "Ice_Cream"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = []

    def display_flavours():
        """Displays available flavours"""
        print("\nThe following flavours are available: ")
        for flavour in self.flavours:
            print(" - " + flavour.title())

ben_and_jerry = IceCreamStand("ben_and_jerry")
ben_and_jerry.flavours = ["cookie_dough", "phish_food", "baked_alaska"]

ben_and_jerry.describe_restaurant()
ben_and_jerry.display_flavours()
