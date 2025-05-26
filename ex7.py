print("Mary had a little lamb.")
# this prints the string which also has a format placeholder
# the .format() with 'snow' means that string will be in the placeholder
print("Its fleece was white as {}.".format('snow'))
# this would also work:
#print(f"Its fleece was white as {'snow'}.")
print("And everywhere that Mary went.")
print("." * 10) # this creates 10 times of "."
# so it will show ".........."

# this creates variables with a single lettered string for each
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
# this will print Cheese (from combining string variables together),
# it will also add a space at the end (from end=' ') instead of creating a new line
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
# this will combine into 'Burger'
print(end7 + end8 + end9 + end10 + end11 + end12)