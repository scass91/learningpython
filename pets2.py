###July 10th 2018
#Passing arguments - because a function definition can have multiple parameters
#a function call may need multiple arguments. POSITIONAL ARGUMENTS need to be
#in the same order the parameters were written. KEYWORD ARGUMENTS where each
#argument consists of a variable name and a value

#positional arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print("\nEmily has a " + animal_type + ".")
    print("\nHer " + animal_type + " is called " + pet_name + ".")

describe_pet("cat", "smudge")
