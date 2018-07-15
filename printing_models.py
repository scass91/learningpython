#July 15th 2018
#Modify lists in a function

#start with designs which need printing

unprinted_designs = ["iPhone case", "dedecahedron", "robot pendant"]
completed_models = []

#simulate printing each design until none are left
#move each completed design after printing

while unprinted_designs:
    current_design = unprinted_designs.pop()

    #create a 3D print from the design
    print("Printing model: " + current_design)
    completed_models.append(current_design)

#display completed completed models
print("\nThe following modles have been printed:")
for completed_model in completed_models:
    print(completed_model.title())
