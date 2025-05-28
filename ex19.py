# def print_one(arg1):
#     print(f"arg1: {arg1}")

# y = "First!"
# print_one(y)

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # this line is for debugging
#     print(">>> cheese_count=", cheese_count, "boxes_of_crackers=", boxes_of_crackers)
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")
#     print(">>> exit cheese_and_crackers") for debugging


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
amount_of_cheese = 15
amount_of_crackers = 30

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10 + 33, 5 + 10)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
