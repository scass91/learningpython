#July 21st 2018
#Start with restaurants.py - create three different instances from the
#class, call describe_restaurant() for each instance
class Restaurant():
    """A simple class describing restaurants and their cusisines"""

    def __init__(self, restaurant_name, cuisine_type):
        """initialise restaurant name and food type attributes"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
#this isn't used in this case but I have carried it over from restaurants.py
    def open_restaurant(self):
        """Let people know the restaurant is open!"""
        message = self.restaurant_name.title() + " is open!"
        print("\n" + message)

    def describe_restaurant(self):
        """Let people know what food is on offer"""
        message = self.restaurant_name.title() + " serves the best " + self.cuisine_type.title() + " food!"
        print("\n" + message)

Nandos = Restaurant("Nandos", "Peri-Peri")
Bills = Restaurant("Bills", "American")
Bodeans = Restaurant("Bodeans", "BBQ")

Nandos.describe_restaurant()
Bills.describe_restaurant()
Bodeans.describe_restaurant()
