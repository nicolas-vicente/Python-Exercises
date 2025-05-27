from sys import argv
# this will get a filename at the command line
script, filename = argv
# this variable is set which opened the file given and returns a file object
txt = open(filename) # if you get some encoding error use: txt = open(filename, encoding="utf-8")
# prints the filename given at the cli
print(f"Here's your file {filename}:")
# prints the contents from reading (read()) the file object in "txt"
print(txt.read())
# closes the file from "txt"
txt.close()
# this prints out a prompt for the user to type the same filename they gave in the cli 
print("Type the filename again:")
# this variable has an input to keep the filename stored
file_again = input('> ')
# creates a variable that stores the file object from the file given in "file_again" variable
txt_again = open(file_again)
# reads the file object from "txt_again"
print(txt_again.read())
# closes the file from "txt_again"
txt_again.close()