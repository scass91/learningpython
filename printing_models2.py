#July 15th 2018

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left
    Move each design to completed_models after printing
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        #create a 3D print from the design
        print("Printing model: " + current_design.title())
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all models which were printed"""
    print("\nThe following models were printed: ")
    for completed_model in completed_models:
        print(completed_model.title())

unprinted_designs = ["iphone case", "dodecahedron", "robot pendant"]
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
