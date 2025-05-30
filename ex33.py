from dis import dis

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    # variable named number is assigned to the value of each element
    print(f"This is count {number}")

for fruit in fruits:
    # variable named fruit is assigned to each element of fruits
    print(f"A fruit of type: {fruit}")

for i in change:
    print(f"I got {i}")

# this creates an empty list
elements = []

# uses the range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    # append is a function that lists understand
    elements.append(i)

# print(">>> after range: i=", i)
# print(">>>> elements=", repr(elements))

# now print out each item in the 'elements' list
for i in elements:
    print(f"Element was: {i}")


dis('''
for number in the_count:
    print(number)
''')