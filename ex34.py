from dis import dis 
from sys import argv

i = 0
numbers = []


# while i < 6:
#     print(f"At the top i is {i}")
#     numbers.append(i)

#     # this increments 'i' which guarantees that the while-loop won't run forever
#     i += 1 

#     print("Numbers now: ", numbers)
#     print(f"At the bottom i is {i}")


# print("The numbers: ")

# for num in numbers:
#     print(num)

# let's make the while-loop into a function:
# also added a variable that allows you to change how much it increments by
def a_list(a,increment):
    i = 0
    while i < a:
        print(f"At the top i is {i}")
        numbers.append(i)

    # this increments 'i' which guarantees that the while-loop won't run forever
        i += increment

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


    print("The numbers: ")

    for num in numbers:
        print(num)

a_list(100, 20)


# using for-loop and range instead would be: 
# print("This is using a for-loop instead:")
# for i in range(0, 6):
#     print(f"At the top i is {i}")
#     numbers.append(i)

    # adding this will make the last bottom 'i' be 6 instead of 5
#     i += 1 

#     print("Numbers now: ", numbers)
#     print(f"At the bottom i is {i}")    

# print("This is the end of the for-loop.")




# how does a while-loop work?
# dis('''
# i = 0 
# while i < 6:
#     i += 1    
# ''')

