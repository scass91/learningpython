###list of guests, comment out original invites as it turns out one can't attend
dinner_guests = ["stir", "paul bohill", "jake peralta"]
###print(dinner_guests[0].title() + ", merrrrrrr, I'm throwing a sweet tea, can you come?")
###print(dinner_guests[1].title() + ", if you can't make this dinner party, i'll take it away!")
###print(dinner_guests[2].title() + ", I've got so many recommendations from Boyle!")

###Peralta cannot attend
print(dinner_guests[2].title() + ", I'm sorry to hear you won't be able to make it!\n")

###replace Peralta
dinner_guests[2] = "mark noble"
print(dinner_guests[0].title() + ", merrrrrrr, I'm throwing a sweet tea, can you come?")
print(dinner_guests[1].title() + ", if you can't make this dinner party, i'll take it away!")
print(dinner_guests[2].title() + ", now it's post-season, come for dinner!")
