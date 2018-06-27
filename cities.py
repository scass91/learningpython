###June 27th 2018
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)
###break kills the program when a criteria is met
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city + "!")
