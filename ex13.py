# import a Python module/library (feature) into this script:
from sys import argv
# "argv" will "hold" the arguments you pass to your .py script
# but instead of holding all the arguments, we will unpackl it annd assign it to 4 variables to work with:
script, first, second, third = argv
# these prints will show the user what their arguments where when they ran the script 
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third varaible is:", third)

likes = input("Did you like this lesson? ")
print("I wonder what the next lesson will be...")

