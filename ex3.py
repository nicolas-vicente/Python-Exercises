# Order of Operations:
# PEMDAS: Parantheses Exponents Multiplication Division Addition Subtraction
# it is more like: PE(M&D)(A&S)

print("I will now count my chickens:")

# this will 30 / 6 first which is 5 and then add 25 = 30.0
# because division was used, the output is a float number
print("Hens", 25 + 30 / 6) 

# this will first multiply 25 and 3 which is 75 then get the remainder from 75/4 which is 3, so the end will be 100 - 3 = 97
print("Roosters", 100 - 25 * 3 % 4) 

print("Now I will count the eggs:")

# first divide 1/4 which is 0.25
# then 4%2 which leaves 0 
# now it is 3 + 2 + 1 - 5 + 0 - 0.25 + 6
# adding it all together = 6.75
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print("Is it true that 3 + 2 < 5 - 7?")
# 3 + 5 = 8, 5 - 7 = -2
# since 8 is not less than -2 the answer will be False
print(3 + 2 < 5 - 7)

print("What is 3 + 2?", 3 + 2)
print("What is 3 - 7?", 5 - 7)

print("Oh, that's why it's False.")

print("How about some more.")

print("Is it greater?", 5 > -2)
print("Is it greater or equal", 5 >= -2)
print("Is it less or equal?", 5 <= -2)

print("This is a random calculation I chose:")
print(51 * 90 - 100 + 29 % 7)

# Re-writing the above using floating point numbers (more accurate)
print("Now this is the same from above but as floating point numbers.")
print("I will now count my chickens:")

print("Hens", 25.0 + 30.0 / 6.0) 

print("Roosters", 100.0 - 25.0 * 3.0 % 4.0) 

print("Now I will count the eggs:")

print(3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0)

print("Is it true that 3.0 + 2.0 < 5.0 - 7.0?")
print(3.0 + 2.0 < 5.0 - 7.0)

print("What is 3.0 + 2.0?", 3.0 + 2.0)
print("What is 3.0 - 7.0?", 5.0 - 7.0)

print("Oh, that's why it's False.")

print("How about some more.")

print("Is it greater?", 5.0 > -2.0)
print("Is it greater or equal", 5.0 >= -2.0)
print("Is it less or equal?", 5.0 <= -2.0)

print("This is a random calculation I chose:")
print(51.0 * 90.0 - 100.0 + 29.0 % 7.0)