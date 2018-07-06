###July 6th 2018
###Fill a dictionary using user input

responses = {}

#flag used to indicate active polling

polling_active = True

while polling_active:
    # Prompt for the persons name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb one day? ")

    #store response in dictionary
    responses[name] = response

    #Find out if someone else will take the poll
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

#Polling complete, show results
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
