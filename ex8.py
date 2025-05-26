# a variable that creates 4 format placeholders with {}'s in a single string
formatter = "{} {} {} {}"
# these prints use the format() function and places 4 things, each inside a placeholder of the "formatter" variable
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
# this prints the string of "formatter" variable 4 times
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
