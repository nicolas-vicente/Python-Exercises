def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b 

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b 

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

def same_answer(a, b):
    return print(f"Does the random formula and the function formula of it give the same answer? {a == b}")

print("Let's do some math with just functions!")

age = add(30, 5)
# print(">>> age=", age)
height = subtract(78, 4)
# print(">>> height=", height)
weight = multiply(90, 2)
# print(">>> weight=", weight)
iq = divide(100, 2)
# print(">>> iq=", iq)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

# print("That becomes: ", what, "Can you do it by hand?")
normal = 30 + 5 + ( 78 - 4 - (((100 / 2) / 2) * (90 * 2)))
print("This is the formula using functions: add(age, subtract(height, multiply(weight, divide(iq, 2))))")
print("This is how the formula would look without functions: 30 + 5 + ( 78 - 4 - (((100 / 2) / 2) * (90 * 2)))")
same_answer(what, normal)

# this is a random formula I came up with 
random =  (8 + 4) * (10 - 3) / 2
print("This is the random formula with normal operations: (8 + 4) * (10 - 3) / 2")
random_with = divide(multiply(add(8, 4), subtract(10, 3)), 2)
print("This is the random formula with functions: divide(multiply(add(8, 4), subtract(10, 3)), 2)")
same_answer(random, random_with)