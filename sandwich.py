#July 15th 2018
#write a function which accepts a list of items someone would want in a
#sandwich. The function should have a parameter which collects as many items
#as the function call provides, and it should print out a summary of the
#sandwich which is being ordered

def sandwich(*fillings):
    """Return a summary of a sandwich which is being made"""
    print("\nMaking a sandwich with the following fillings: ")
    for filling in fillings:
        print("- " + filling)

sandwich("cheese")
sandwich("cheese", "ham")
sandwich("chicken", "mayonnaise", "lettuce")
