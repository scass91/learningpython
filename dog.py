#July 18th 2018
#Classes for the first time

#classes have capitalised names, """ docstring is used to describe the class
class Dog():
    """A simple attempt at modelling a dog"""
#a function which is part of a class is called a method
    def __init__(self, name, age):
        """initialise name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """simulate a dog sitting when commanded"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """simulate rolling over when commanded"""
        print(self.name.title() + " rolled over!")

my_dog = Dog("toe", 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()
