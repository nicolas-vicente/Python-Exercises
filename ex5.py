name = 'Zed A. Shaw'
age = 35 
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

# if I were to use centimeters and kilograms instead of inches and pounds
centimeters = 2.54
kilograms = 0.4535924
height_to_cm = round(height * centimeters)
weight_to_kg = round(weight * kilograms)
#print(f"{name}'s height is {height_to_cm} centimeters (rounded).")
#print(f"{name}'s weight is {weight_to_kg} kilograms (rounded).")

# This also works:
print(f"{name}'s height is {round(height * centimeters)} centimeters (rounded).")
print(f"{name}'s weight is {round(weight * kilograms)} kilograms (rounded).")