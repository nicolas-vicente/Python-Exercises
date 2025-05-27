# this is one way you can get input from a user
print("How old are you", end=' ')
# this variable "saves" what the user input
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()
# this will print out the user's answers
print(f"So, you're {age} old, {height} tall and {weight} heavy.")


# another example of getting user's input 
print("What is your SSN?", end=' ') # hehe
ssn = input()
print("What is your mother's maiden name?", end=' ') # don't be suspicous
maiden = input()
print("What is your full legal name?", end=' ') # for no reasonnn
legal_name = input()
print(f"{legal_name}, there is no particular reason for this form at all. Have a nice day.")


# to get an integer from user input; default from input() is to get a string no matter what the input is
# age = int(input())