#July 15th 2018
#start with a copy of great_magicians.py, call make_great() wirh a copy of
#th list of magicians names. Because the original list will be unchanged,
#return a new list and store it in a seperate list. Call show_magicians() to
#show you jave on elist of the original names and one list with great names

def show_magicians(magician_names):
    """prints a list of magicians in a list"""
    for magician_name in magician_names:
        print(magician_name.title())

def make_great(magician_names):
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

    return magician_names

magician_names = ["paul daniels", "dynamo", "penn jillette"]
show_magicians(magician_names)

print("\nGreat magicians: ")
great_magicians = make_great(magician_names[:])
show_magicians(great_magicians)

print("\nOriginal magicians: ")
show_magicians(magician_names)
