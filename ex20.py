from sys import argv

# input_file = "ex20_test.txt"
# instead of hard-coding, we're going to enter the txt file through the cli:
script, input_file = argv

# function that will read the file that is passed for the argument 
def print_all(f):
    # print(">>> print_all: f=", f)
    print(f.read())
    # print("<<< print_all: f=", f)

# this function will "rewind" to the beginning of the file passed
def rewind(f):
    # print(">>> rewind: f=", f)    
    f.seek(0) # seek is in bytes; it will change the position of the file hand to a specified position within a file, in this case "0"
    # print("<<< rewind: f=", f)    

def print_a_line(line_count, f):
#    print(">>> current_line=", current_line)
    # print(">>> print_a_line: f=", f)
    print(line_count, f.readline(), end="") # end="" will remove the extra \n when using readline()
    # print("<<< print_a_line: f=", f)
#    print(">>> line_count=", line_count)

# opens a file (given in the cli) to be passed (by reference) into the functions' argument (in this case: "f")
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape:")

rewind(current_file)

print("Let's print three lines:")
current_line = 1
# print(">>> current_line=", current_line)
print_a_line(current_line, current_file)

# use this: (instead of current_line = current_line + 1)
current_line += 1
# print(">>> current_line=", current_line)
print_a_line(current_line, current_file)

current_line += 1
# print(">>> current_line=", current_line)
print_a_line(current_line, current_file)

current_file.close()