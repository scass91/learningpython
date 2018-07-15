#July 15th 2018
#make a list of magician's names, pass the list to a function called
#show_magicians(), which prints the name of each magician in the list

magician_names = ["paul daniels", "dynamo", "penn jillette" ]
def show_magicians(magician_name):
    """prints a list of magicians in a list"""
    for magician_name in magician_names:
        print(magician_name.title())

show_magicians(magician_names)
