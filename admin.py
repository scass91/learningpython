#July 23rd 2018
#An administrator is a special kind of user. Write a class called Admin
#that inherets from the User class in users.py. Add an attribute Privileges
#that stores a list of strings like 'can add post', 'can delete post'
#Write a method called show_privileges() that lists the admins set of
#privileges, create a new instance of Admin and use your method to show its
#privileges

#for some reason this wont work on atom, works using IDLE though...
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
        self.privileges = []

    def show_privileges(self):
        """shows what additional privileges a user has"""
        print("\nPrivileges: ")
        for privilege in self.privileges:
            print(" - " + privilege)

simon = Admin("simon", "cass", 27, "london")
dave = User("dave", "davids", 52, "newcastle")
simon.describe_user()

simon.privileges = ["Ban user", "Unban user", "Post article", "Delete article"]
simon.show_privileges()

simon.greet_user()

dave.describe_user()
dave.greet_user()
