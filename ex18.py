# using "def" ("define") will create a function
# def do_nothing():
#     pass # this tells Python the function is empty

# def do_something():
#     print("I did something")

# you can now call a function by its name:
# do_something()


# this is a function with arguments:
# def do_more_things(a, b):
#     a = "hello"
#     b = 1 
#     print("A IS", a, "B IS", b)

# this calls a function with arguments:
# do_more_things("ignored", "hello")

# this is like the other scripts with argv in it:
# *args is not very common to use unless specifically needed
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# *args is better used when you don't know how many arguments will be passed on, so instead this is better (and easier in this case):
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this will take one argument:
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments:
def print_none():
    print("I got nothin'.")

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()