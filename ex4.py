# how many cars there are:
cars = 100 
# how many seats are available in each car:
space_in_a_car = 4.0 
# how many drivers there are:
drivers = 30 
# how many passengers there are:
passengers = 90 
# finds out how many cars will be left without drivers:
cars_not_driven = cars - drivers 
# the number of drivers is how how many cars can be driven:
cars_driven = drivers 
# calculate the number of spots open for carpool (for transportation):
carpool_capacity = cars_driven * space_in_a_car 
# calculate the average of how many people should be in each car considering the number of drivers (which is also cars_driven):
average_passengers_per_car = passengers / cars_driven 

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")