###list of guests, comment out original invites as it turns out one can't attend
dinner_guests = ["stir", "paul bohill", "jake peralta"]
###print(dinner_guests[0].title() + ", merrrrrrr, I'm throwing a sweet tea, can you come?")
###print(dinner_guests[1].title() + ", if you can't make this dinner party, i'll take it away!")
###print(dinner_guests[2].title() + ", I've got so many recommendations from Boyle!")

###Peralta cannot attend
print(dinner_guests[2].title() + ", I'm sorry to hear you won't be able to make it!\n")

###replace Peralta, comment out old code - new longer list is now possible
dinner_guests[2] = "mark noble"
###print(dinner_guests[0].title() + ", merrrrrrr, I'm throwing a sweet tea, can you come?")
###print(dinner_guests[1].title() + ", if you can't make this dinner party, i'll take it away!")
###print(dinner_guests[2].title() + ", now it's post-season, come for dinner!")

###added new guests - found a bigger table
###add jimothy into index position 1
dinner_guests.insert(1, "jimothy lacoste")
###add new guest to end of list
dinner_guests.append("smudge the cat")
###add new guest to start of list
dinner_guests.insert(0,"james")

###new guestlist
print(dinner_guests[0].title() + ", we're having a vegan night - come join?")
print(dinner_guests[1].title() + ", merrrrrrr, I'm throwing a sweet tea, can you come?")
print(dinner_guests[2].title() + ", dinner, then listen to subway systems?")
print(dinner_guests[3].title() + ", if you can't make this dinner party, i'll take it away!")
print(dinner_guests[4].title() + ", now it's post-season, come for dinner!")
print(dinner_guests[5].title() + ", you're only invited to chase mice!")
