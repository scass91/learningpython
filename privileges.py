#July 24th 2018
#Write a seperate Privileges class. The class should have one attribute,
#privileges, that stores a list of strings as described in admin.py
#Move the show_privileges() method to this class. Make privleges instance
#as an attribute in the Admin class. Create a new instance of Admin and use
#your method to show its Privileges
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

class Admin(User):
    """Power user profile"""
    def __init__(self, first_name, last_name, age, location):
        """Initialise the admin"""
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()

class Privileges:
    """Shows privileges of an Admin profile"""

    def __init__(self, privileges=[]):
        """initialise the privileges"""
        self.privileges = privileges

    def show_privileges(self):
        """shows what additional privileges a user has"""
        print("\nPrivileges: ")
        if self.privileges:
            for privilege in self.privileges:
                print(" - " + privilege)
        else:
            print("User has no priveleges")


simon = Admin("simon", "cass", 27, "london")

simon.describe_user()

simon.privileges.show_privileges()
print("\nAdding privileges:")
simon_privileges = ["Ban user", "Unban user", "Post article", "Delete article"]

simon.privileges.privileges = simon_privileges
simon.privileges.show_privileges()
