fruit = [
    ['Apples', 12, 'AAA'], ['Oranges', 1, 'B'], 
    ['Pears', 2, 'A'], ['Grapes', 14, 'UR']]

cars = [
    ['Cadillac', ['Black', 'Big', 34500]],
    ['Corvette', ['Red', 'Little', 1000000]],
    ['Ford', ['Blue', 'Medium', 1234]],
    ['BMW', ['White', 'Baby', 7890]]
]

languages = [
    ['Python', ['Slow', ['Terrible', 'Mush']]],
    ['JavaScript', ['Moderate', ['Alright', 'Bizarre']]],
    ['Perl6', ['Moderate', ['Fun', 'Weird']]],
    ['C', ['Fast', ['Annoying', 'Dangerous']]],
    ['Forth', ['Fast', ['Fun', 'Difficult']]],
]

# Fruit Challenge:
# 12
fruit[0][1]
# 'AAA'
fruit[0][2]
# 2
fruit[2][1]
# 'Oranges'
fruit[1][0]
# 'Grapes'
fruit[3][0]
# 14
fruit[3][1]
# 'Apples'
fruit[0][0]

# Cars Challenge:
# ‘Big’
cars[0][1][1]
# ‘Red’
cars[1][1][0]
# 1234
cars[2][1][2]
# ‘White’
cars[3][1][0]
# 7890
cars[3][1][2]
# ‘Black’
cars[0][1][0]
# 34500
cars[0][1][2]
# ‘Blue’
cars[2][1][0]

# Languages Challenge:
# ‘Slow’
languages[0][1][0]
# ‘Alright’
languages[1][1][1][0]
# ‘Dangerous’
languages[3][1][1][1]
# ‘Fast’
languages[4][1][0]
# ‘Difficult’
languages[4][1][1][1]
# ‘Fun’
languages[4][1][1][0]
# ‘Annoying’
languages[3][1][1][0]
# ‘Weird’
languages[2][1][1][1]
# ‘Moderate’
languages[2][1][0]

#Final Challenge:
#    cars[1][1][1] --> 'Little'
#    cars[1][1][0] --> 'Red'
#    cars[1][0] --> 'Corvette'
#    cars[3][1][1] --> 'Baby'
#    fruit[3][2] --> 'UR'
#    languages[0][1][1][1] --> 'Mush'
#    fruit[2][1] --> 2
#    languages[3][1][0] --> 'Fast'