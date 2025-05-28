from sys import argv
from os.path import exists
# exists will return True/False if a file exists

# from_file = "test.txt"
# to_file = "new_test.txt"

# print(f"Copying from {from_file} to {to_file}")

# in_file = open(from_file)
# this type of message is for debugging purposes
# print(">>> in_file=", repr(in_file))
# indata = in_file.read()
# print(">>> in_file=", repr(indata))

# print(f"The input file is {len(indata)} bytes long")

# print(f"Does the output file exist? {exists(to_file)}")
# print(f"Ready, hit RETURN to continue, CTRL-C top abort.")
# input()

# out_file = open(to_file, 'w')
# out_file.write(indata)

# print("Alright, all done.")

# out_file.close()
# in_file.close()

# to make the script more simple, I could do this instead: 
# this will take the argument for a file (from_file) to be copied to another file (to_file)
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")
# with open() will automatically close the file once done
with open(from_file, 'r') as in_file:
    indata = in_file.read()

with open(to_file, 'w') as out_file:
    out_file.write(indata) 

print("Alright, all done.")
