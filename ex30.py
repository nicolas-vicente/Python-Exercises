from dis import dis

people = 20
cats = 30
dogs = 15

dis('''
if people < cats:
    print("Too many cats! The world is doomed!")
''')
if people > cats:
    print(">> second if", people, cats)
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")



dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")


cats -= 1 

if people != cats:
    print("People are not cats :(")

if people >= cats:
    print("People need more cats.")

if people <= cats:
    print("Cats need more people :( please adopt")