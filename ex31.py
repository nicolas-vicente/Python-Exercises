from dis import dis

people = 36
cars = 55
trucks = 32
# used dis() to disassmble the if-elif-else statement
# compares cars to people; if there are more cars print something, if there is less cars print something, and if not either print something
dis('''
if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")
''')
# if there are more trucks than cars,
if trucks > cars:
    print(">>>", trucks, cars)
    # print this
    print("That's too many trucks.")
    # if there are less trucks than cars
elif trucks < cars:
    # print this
    print("Maybe we could take the trucks.")
    # if neither, print this
else:
    print("We still can't decide.")

# if there are more people than trucks,
if people > trucks:
    # print this:
    print("Alright, let's just take the trucks.")
    # if not, then print this:
else:
    print("Fine, let's stay home then.")

# if there are more cars than people OR less trucks than cars,
if cars > people or trucks < cars:
    # print this:
    print("We should take the trucks.")
    # else, print this:
else:
    print("Maybe let's walk there.")