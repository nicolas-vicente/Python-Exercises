from sys import exit

def gold_room():
    print(">>>> gold_room")
    print("This room is full of gold. How much do you take?")

    try:
        how_much = int(input("> "))
    except:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")
    print("<<<< gold_room")

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        print(">>>> bear_moved=", bear_moved)
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        # if the player taunts the bear and the bear has not moved yet, the player can open the door
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            # changes the variable to True so the bear has moved.
            bear_moved = True
        # if the player taunts the bear and the bear has moved, the player will die
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:

            print("I got no idea what that means.")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")
    print("There is also a sword on the ground nearby, do you pick that up?")
    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    elif choice == "pickup":
        dead("The sword was enchanted with poison and you instantly die.")
    else:
        dead("You stumble around the room until you stave.")    


start()