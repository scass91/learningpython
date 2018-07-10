###July 10th 2018
#Passing arguments - because a function definition can have multiple parameters
#a function call may need multiple arguments. POSITIONAL ARGUMENTS need to be
#in the same order the parameters were written. KEYWORD ARGUMENTS where each
#argument consists of a variable name and a value

#positional arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print("\nEmily has a " + animal_type + ".")
    print("Her " + animal_type + " is called " + pet_name + ".")

describe_pet("cat", "smudge")

#keyword arguments - name value pairs which are passed to a function
def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print("\nEmily has a " + animal_type + ".")
    print("Her " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type = "cat", pet_name = "smudge")


#default values - if an argument value is provided in the function call by
#default, you can exclude the dorresponding argument in the function called
#using default values can simplify function calls & clarify ways functions are
#used. These can be overwritten if, for example, a different animal_type is
#input
def describe_pet(pet_name, animal_type = "dog"):
    """Display information about a pet"""
    print("\nKatherine has a " + animal_type + ".")
    print("Her " + animal_type + " is called " + pet_name.title() + ".")

describe_pet(pet_name = "betty")
