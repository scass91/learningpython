#July 18th 2018
#Make a class called Restaurant. The __init__() method for Restaurant
#should store 2 attributes: a restaurant_name, and a cuisine_type
#Make a method called describe_restaurant() that prints these two pieces of
#information, and a method called open_restaurant() which prints a message
#indicating the restaurant is open. Make an instance called restaurant from
#your class. Print both attributes individually, then call both methods.

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
        message = self.restaurant_name.title() + " serves the best " + self.cuisine_type.title() + " food!"
        print("\n" + message)

restaurant = Restaurant("Nandos", "Peri-Peri")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()
