#July 15th 2018
#start with a copy of magicians.py, write a function called make_great()
#which modifies the list
#of magicians by adding the phrase "the great" to each name.
#call show_magicians() to show the list has been modified

def show_magicians(magician_name):
    """prints a list of magicians in a list"""
    for magician_name in magician_names:
        print(magician_name.title())

def make_great(magician_name):
    """adds "the great" to each magician name"""
    #new list for the great magicians
    great_magicians = []

    while magician_names:
        magician = magician_names.pop()
        great_magician = magician + " the Great"
        great_magicians.append(great_magician)

    #adds great magicians back into magicians list
    for great_magician in great_magicians:
        magician_names.append(great_magician)

magician_names = ["paul daniels", "dynamo", "penn jillette" ]
show_magicians(magician_names)
print("\n")
make_great(magician_names)
show_magicians(magician_names)
