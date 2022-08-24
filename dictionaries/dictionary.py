cat = {"name": "blue", "age": 3.5, "is_cute" : True}
print(cat)

# have 1 information
cat2 = dict(name = "kitty")
print(cat2)

# if you want to have multiple information
cat3 = dict(name = "Pillo", color = "black and white")
print(cat3)

print("---------------------------------------")

instructor = {
	"name": "Colt",
	"owns_dog": True,
	"num_courses": 4,
	"favorite_language": "Python",
	"is_hilarious": False,
	44: "my favorite number"
}

# Accessing Individual Value
print(instructor["name"])
print(instructor["owns_dog"])

print("---------------------------------------")

# Accessing all values 
print(instructor.values())

print("---------------------------------------")

# Using for loop
for v in instructor.values():
    print(v)

print("---------------------------------------")

# Access all keys
for key in instructor.keys():
    print(key)

print("---------------------------------------")

# Accessing All Keys and Values
print(instructor.items())

print("---------------------------------------")

# using loop
for key, value in instructor.items() :
    print(f"key is {key} and value is {value}")

print("---------------------------------------")

# Check key with "in"
print("name" in instructor)
print("phone" in instructor)

print("---------------------------------------")

# using conditional
if instructor ["name"] :
    print("THERE IS A NAME KEY")

print("---------------------------------------")

# Check value with "in"
print("name" in instructor.values())

print("---------------------------------------")

# DICTIONARY METHODS
# clear : clear all the key and values in a dictionary
instructor = {
	"name": "Colt",
	"owns_dog": True,
	"num_courses": 4,
	"favorite_language": "Python",
	"is_hilarious": False,
	44: "my favorite number"
}

instructor.clear()
print(instructor)

print("---------------------------------------")

# copy : makes a copy of a dictionary
d = dict(a=1, b=2, c=3)
c = d.copy()
print(c)
print(c is d)

print("---------------------------------------")

# fromkeys : creates key-value pairs from comma separated values
new_user = {}.fromkeys(['name', 'score', 'email', 'profile bio'], 'unknown')
print(new_user)

print("---------------------------------------")

# membuat dictionary baru tanpa mempengaruhi atau mengubah yg sebelumnya
print(new_user.fromkeys(['phone'], 'unknown'))
print(new_user.fromkeys('phone', 'unknown'))
print(new_user.fromkeys(range(1, 10), 'unknown'))

print("---------------------------------------")

instructor = {
	"name": "Colt",
	"owns_dog": True,
	"num_courses": 4,
	"favorite_language": "Python",
	"is_hilarious": False,
	44: "my favorite number"
}

# get : Retieves a key in an object and return None instead of a KeyError if the key does not exist
print(instructor.get('name'))
print(instructor.get('email'))

result = instructor.get('email')
print(result)
print(result is None)

print("---------------------------------------")

# pop : takes a single argument corresponding to a key and removes that key-value pair from the dictionary. returns the value corresponding to the key that was removed
print(instructor.pop('owns_dog'))
print(instructor)
# print(instructor.pop('email'))

print("---------------------------------------")

# popitem : removes a random key in a dictionary
print(instructor.popitem())
print(instructor.popitem())
print(instructor)

print("---------------------------------------")

# update : update keys and values in a dictionary with another set of key value pairs
person = {"city" : "Antigua"}
person.update(instructor)

print("---------------------------------------")

#update to instuctor
person['name'] = "Evelia"
print(person)
person.update(instructor)
print(person)

print("---------------------------------------")

#key and value uppercase
instructor.pop('num_courses')
print(instructor)
yeiling_instrructor = {k.upper():v.upper() for k, v in instructor.items()}
print(yeiling_instrructor)


# # Exercise 1
# # This code picks a random food item:
# from random import choice #DON'T CHANGE!
# food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

# #DON'T CHANGE THIS DICTIONARY EITHER!
# bakery_stock = {
#     "almond croissant" : 12,
#     "toffee cookie": 3,
#     "morning bun": 1,
#     "chocolate chunk cookie": 9,
#     "tea cake": 25
# }

# # YOUR CODE GOES BELOW:
# # using IN
# if food in bakery_stock:
# 	print("{} left".format(bakery_stock[food]))
# else:
# 	print("We dont make that")

# # using get()
# quantity = bakery_stock.get(food)
# if quantity:
# 	print("{} left".format(quantity))
# else:
# 	print("We dont make that")


# # exercise 2
# #DO NOT TOUCH game_properties!
# game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"] 

# Use the game_properties list and dict.fromkeys() to generate a dictionary with all values set to 0. Save the result to a variable called initial_game_state
# game_properties= {}.fromkeys(["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"], 0)
# initial_game_state = game_properties
# print(initial_game_state)

# # atau
# initial_game_state = dict.fromkeys(game_properties, 0)



    
