#July 18th 2018
#Put the functions for the example printing_models.py in a
#seperate file called printing_functions.py. Write an import statement at
#the top of printing_models.py, modify the file to use the imported functions

def print_models(unprinted_designs, completed_models):
    """Lists designs which need printing & completed prints after printing"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        #create a 3D print from the design
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_complete_models(completed_models):
    """Shows a list of completed models"""
    print("\nThe following modles have been printed:")
    for completed_model in completed_models:
        print(completed_model.title())
