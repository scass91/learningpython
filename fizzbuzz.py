###June 27th 2018
###fizzbuzz attempt #1

for i in range(1,101):
    if i % 15 == 0:
        print("Fizzbuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
