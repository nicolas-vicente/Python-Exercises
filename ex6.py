# assigns 10 to types_of_people
types_of_people = 10
# creates a variable that formats a string to include the variable types_of_people
x = f"There are {types_of_people} types of people."

# assigns values to variables
binary = "binary"
do_not = "don't"
# a variable that formats a string to include binary and do_not
y = f"Those who know {binary} and those who {do_not}."

# prints the x and y variables (which are both formatted strings)
print(x)
print(y)

# prints x variable within a formatted string
print(f"I said: {x}")
# prints the y variable within a formatted string and also '' it to provide a clearer context
print(f"I also said: '{y}'")

# assigns False to this variable
hilarious = False
# assigns a variable that is a string and has a {} format placeholder for something to be added
joke_evaluation = "Isn't that joke so funny?! {}"
# prints the joke evaluation with a format that puts the hilarious variable into the {} placeholder
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."
# adds the w and e together (which are both strings) 
# this means they will be joined together (concatenate) since they are both strings
print(w + e)