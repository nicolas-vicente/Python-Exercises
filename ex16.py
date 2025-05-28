from sys import argv
# instead of hardcoding. I will use the module above
script, filename = argv


# filename = "test.txt"

print(f"We're going to erase {filename}.")
# let the user know they can cancel the script
print("If you don't want that, hit Ctrl-C (^C).")
print("If you do want that, hit RETURN.")
# this makes the program wait for the user's input (quit or not)
input("?")

print("Opening the file...")
# this will open the file in "write" mode; if the file entereed in the cli was different "w" creates that file instead
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
# makes sure the file is erased (this is redundant because this is what 'w' does), and starts the "read head" at the beginning
target.truncate()


print("Now I'm going to ask you for three lines.")

# taking input from user to later write into the file
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

# to make the writing into the file more simple:
target.write(f"{line1}\n{line2}\n{line3}\n")
print("And finally, we close it.")
target.close() # closes the file (you can end up leaking files later if you don't)

# Now I will have the script read the text file created again:
print(f"\nThis is what you inputted into the {filename} file:")
target = open(filename)
print(target.read())
target.close()