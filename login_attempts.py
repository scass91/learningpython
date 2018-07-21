#July 21st 2018
#Add an attribute called login_attempts to User class in users.py
#Write a method called increment_login_attempts() which increments the number
#of login attempts by 1.
#Write another method called reset_login_attempts() which resets the value
#of login_attempts to 0
#Make an instance of the User class and call increment_login_attempts() several
#times. Print the value of login_attempts to make sure it was incremented
#properly, and then call reset_login_attempts(). print login_attempts again to
#ensure it has been reset to 0
class User:
    """Store attributes about a given users profile"""

    def __init__(self, first_name, last_name, age, location):
        """Initialise the user"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = str(age)
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Print a summary of the information on a user"""
        print(self.first_name + " " + self.last_name)
        print("\nLocation: " + self.location)
        print("Age: " + self.age)

    def greet_user(self):
        """print a personalised greeting"""
        print("\nWelcome back " + self.first_name + " " + self.last_name + ".")
        print("How are things in " + self.location + "?\n")

    def increment_login_attempts(self):
        """increases number of login attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """sets login attempts to 0"""
        self.login_attempts = 0

dave = User("dave", "davids", 53, "newcastle")

print("Login attempts: " + str(dave.login_attempts))
dave.increment_login_attempts()
dave.increment_login_attempts()
dave.increment_login_attempts()
print("Incorrect password, number of login attempts: "
                            + str(dave.login_attempts))
print("\nResetting login attempts... ")
dave.reset_login_attempts()
print("Login attempts: " + str(dave.login_attempts))

dave.describe_user()
dave.greet_user()
