###June 18th 2018

current_users = ['dave', 'tom', 'steve', 'john', 'tim']
new_users = ['DAVE', 'tim', 'larry', 'gary', 'barry']

for new_user in new_users:
    ###used.lower() to ensure case insensitivity
    if new_user.lower() in current_users:
        print("Hi " + new_user + " you need to choose a new name.")
    else:
        print("Hi " + new_user + " that name is available.")
