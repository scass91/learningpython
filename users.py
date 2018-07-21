#July 21st 2018
#make a class called User. Create 2 attributes, called first_name and last_name
#then create several other attributes which would be stored in a profile
#Make a method called describe_user() that prints a summary of the information
#Make another method called greet_user() that prints a personalised greeting
#Create several instances representing different users, call both methods for
#each user

class User:
    """Store attributes about a given users profile"""

    def __init__(self, first_name, last_name, age, location):
        """Initialise the user"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = str(age)
        self.location = location.title()

    def describe_user(self):
        """Print a summary of the information on a user"""
        print(self.first_name + " " + self.last_name)
        print("\nLocation: " + self.location)
        print("Age: " + self.age)

    def greet_user(self):
        """print a personalised greeting"""
        print("\nWelcome back " + self.first_name + " " + self.last_name + ".")
        print("How are things in " + self.location + "?\n")

simon = User("simon", "cass", 27, "london")
dave = User("dave", "davids", 53, "newcastle")

simon.describe_user()
simon.greet_user()

dave.describe_user()
dave.greet_user()
