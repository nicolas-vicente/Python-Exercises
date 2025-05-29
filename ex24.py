fruit = [
    {'kind': 'Apples', 'count': 12, 'rating': 'AAA'},
    {'kind': 'Oranges', 'count': 1, 'rating': 'B'},
    {'kind': 'Pears', 'count': 2, 'rating': 'A'},
    {'kind': 'Grapes', 'count': 14, 'rating': 'UR'}
];

cars = [
    {'type': 'Cadillac', 'color': 'Black', 
     'size': 'Big', 'miles': 34500},
    {'type': 'Corvette', 'color': 'Red', 
     'size': 'Little', 'miles': 1000000},
    {'type': 'Ford', 'color': 'Blue', 
     'size': 'Medium', 'miles': 1234},
    {'type': 'BMW', 'color': 'White', 
     'size': 'Baby', 'miles': 7890}
];

languages = [
    {'name': 'Python', 'speed': 'Slow', 
     'opinion': ['Terrible', 'Mush']},
    {'name': 'JavaScript', 'speed': 'Moderate', 
     'opinion': ['Alright', 'Bizarre']},
    {'name': 'Perl6', 'speed': 'Moderate', 
     'opinion': ['Fun', 'Weird']},
    {'name': 'C', 'speed': 'Fast', 
     'opinion': ['Annoying', 'Dangerous']},
    {'name': 'Forth', 'speed': 'Fast', 
     'opinion': ['Fun', 'Difficult']}, 
];

# Fruit Challenge: 
# 12
fruit[0]['count']
# ‘AAA’
fruit[0]["rating"]
# 2
fruit[2]['count']
# ‘Oranges’
fruit[1]['kind']
# ‘Grapes’
fruit[3]['kind']
# 14
fruit[3]['count']
# ‘Apples’
fruit[0]['kind']

# Cars Challenge:
# ‘Big’
cars[0]['size']
# ‘Red’
cars[1]['color']
# 1234
cars[2]['miles']
# ‘White’
cars[3]['color']
# 7890
cars[3]['miles']
# ‘Black’
cars[0]['color']
# 34500
cars[0]['miles']
# ‘Blue’
cars[2]['color']


# Languages Challenge:
# ‘Slow’
languages[0]['speed']
# ‘Alright’
languages[1]['opinion'][0]
# ‘Dangerous’
languages[3]['opinion'][1]
# ‘Fast’
languages[3]['speed']
# ‘Difficult’
languages[4]['opinion'][1]
# ‘Fun’
languages[4]['opinion'][0]
# ‘Annoying’
languages[3]['opinion'][0]
# ‘Weird’
languages[2]['opinion'][1]
# ‘Moderate’
languages[1]['speed']

# Final Challenge:
# 'Little' --> cars[1]['size']
# 'Red' --> cars[1]['color']
# 'Corvette' --> cars[1]['type']
# 'Baby' --> cars[3]['size']
# 'UR' --> fruit[3]['rating']
# 'Mush' --> languages[0]['opinion'][1]
# 2 --> fruit[2]['count']
# 'Fast' --> languages[3]['speed']