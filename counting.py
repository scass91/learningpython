###May 30th 2018
###I've read about for loops & list comprehensions, time to utlise them!
###Count from 1 to 20, inclusive.
for i in range(1,21):
    print(i)


###Make a list of the numbers from one, to one million, print with a for loop
###This takes a while! Commenting it out so as not to slow the whole file down when testing
a_million = list(range(1,1000001))
###for i in a_million:
###    print(i)


print(max(a_million))
print(min(a_million))
print(sum(a_million))


###increase each list by x, where x is list(range(#,#,x))
odd_numbers = list(range(1,20,2))
print(odd_numbers)

threes = list(range(3,31,3))
print(threes)


###exponentials use ** instead of *, i.e. 3 squared = 3 ** 2
###first 10 cubes
for i in range(1,11):
    print(i ** 3)

###as above but in a list comprehension
cubes = [i ** 3 for i in range(1,11)]
print(cubes)
