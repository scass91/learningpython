#July 21st 2018
#start with restaurants.py. Add an attribute calld number_served and set it
#to a default value of 0. Create an instance called restaurant from this class
#Print the number of customers served by the restaurant, then change it this
#and reprint
#Add a method called set_number_served() that lets you set the number of
#customers that have been served. Call this method with a new number and print
#the value again
#Add a method called increment_number_served() that lets you increment the
#number of customers who have been served. Call this mthod with any number
#you like that coud represent how many customers were served in say, a day, of
#business
class Restaurant():
    """A simple class describing restaurants and their cusisines"""

    def __init__(self, restaurant_name, cuisine_type):
        """initialise restaurant name and food type attributes"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def open_restaurant(self):
        """Let people know the restaurant is open!"""
        message = self.restaurant_name.title() + " is open!"
        print("\n" + message)

    def describe_restaurant(self):
        """Let people know what food is on offer"""
        message = self.restaurant_name.title() + " serves the best " + self.cuisine_type.title() + " food!"
        print("\n" + message)

    def set_number_served(self, number_served):
        """set the number of customers served"""
        self.number_served = number_served

    def increment_number_served(self, number_served):
        """increase the number served"""
        if number_served >= 0:
            self.number_served += number_served

restaurant = Restaurant("Nandos", "Peri-Peri")

restaurant.describe_restaurant()
print("\nCustomers served: " + str(restaurant.number_served))
restaurant.number_served = 100
print("Customers served: " + str(restaurant.number_served))
restaurant.increment_number_served(1000)
print("Customers served: " + str(restaurant.number_served))
