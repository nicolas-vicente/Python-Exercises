# assigns a variable with a string that has the horizontal tab escape sequence (\t)
tabby_cat = "\tI'm tabbed in."
# another variable but this time with a new line escape sequence (\n)
persian_cat = "I'm split\non a line."
# another variable assigned but now with an escape sequence for the backslash (\\)
backslash_cat = "I'm \\ a \\ cat."

# this variable contains a multi-line string using tripe-single-quote (makes it easier to recognize)
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# this is my random code showing more escape sequences:
print("This will show as {}, even though I used \"\\101\".".format("\101"))
print("\nUsing \"\\U0001F600\" in the code will show you a grinning face like this: {}\n".format("\U0001F600"))