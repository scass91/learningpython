#July 12th 2018
#Return values - a function doesn't always have to display its output directly
#instead it can process some data then return a value or set of numbers
#This value is called a return value - the return statment takes a value from
#inside a function & sends it back to the line that called the function
#return values help simplify programs by moving much of the grunt work into
#functions, which can simplify the body of a program

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = first_name + " " + last_name
    return full_name.title()

musician = get_formatted_name("dave", "grohl")
print(musician)
