from dis import dis 

print('''You enter a dark room with three doors.
Do you go through door #1, door #2, or door #3?''')

door = input('> ')


if door == '1':
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")


    bear = input('> ')

    if bear == '1':
        print("The bear eats your face off. Good job!")
    elif bear == '2':
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
    print("Bear runs away")

elif door == '2':
    print("You stare into the endless abyss at Cthulhu's retina,")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input('> ')

    if insanity == '1' or insanity == '2':
        print("Your body survives powered by a mind of jello.")

        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

elif door == '3':
    print("You notice a skeleton with armor at the back of the room.")
    print("You decide to leave, thinking 'this place should be locked up.'")
    print("And as you leave, you hear whispers coming from door #3")

else:
    print("You stumble around and fall on a knife and die. Good job!")



dis('''
if door == '1':
    print('1')
    bear = input('> ')
    if bear == '1':
        print("bear 1")
    elif bear == '2':
        print("bear 2")
    else:
        print("bear 3:")
''')