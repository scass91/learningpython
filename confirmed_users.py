###July 4th 2018
#Start with list of users needing to be verified
#and one other empty list to hold confirmed users

unconfirmed_users = ['alice', 'brian', 'dave']
confirmed_users = []

#verify each user until no more unverified
#move verified into confirmed list

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user " + current_user.title())
    confirmed_users.append(current_user)

#display all confirmed users
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
