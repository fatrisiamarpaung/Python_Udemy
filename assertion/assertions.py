# def add_positive_numbers(x, y):
# 	assert x > 0 and y > 0, "Both numbers must be positive!"
# 	return x + y

# add_positive_numbers(1, 1) #2
# add_positive_numbers(1, -1) #AssertionError: Both numbers must be positive!


# def eat_junk(food):
#     assert food in [
#         "pizza", 
#         "burger", 
#         "ice cream", 
#         "candy", 
#         "fried butter"
#     ], "food must be a junk food!" 
#     return f"NOM NOM NOM I am eating {food}"


# food = input("ENTER A FOOD PLEASE: ")
# print(eat_junk(food))

def do_something_bad(user):
	assert user.is_admin, "Only admins can do bad things!"
	return "Mua ha ha ha!"

user = input("What is ur position? ")
print(do_something_bad(user))
