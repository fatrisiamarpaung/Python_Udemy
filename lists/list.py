

# This is how to use list in python
tasks = ["Install Python", "Learn Python", "Take a break"]
print(tasks)

# len() digunakan untuk melihat panjang list
print(len(tasks))

# cara lain membuat list menggunakan fungsi bawaan
r = range(1,10)
print(list(r))

print("---------------------------------------")

# Accessing Data in List
numbers = [1, 2, 3, 4]

print(numbers[0]) #1
print(numbers[1]) #2
print(numbers[2]) #3
print(numbers[3]) #4

print("---------------------------------------")

# Accessing all value in the list
for number in numbers :
	print(number)

print("---------------------------------------")

# Accessing value from the end
friends = ["Ashley", "Matt", "Michael"]

print(friends[-1]) #’Michael’
print(friends[-3]) #’Ashley’ 
# print(friends[-4]) #’IndexError’

print("---------------------------------------")

# Check if value is in a list
print("Ashley" in friends)
print("Colt" in friends)

# carts = ["Apple", "Kiwi", "Guava", "Banana", "Durian", "Orange"]

# user_list = input("Do you want to pick some fruits??? (Click q to quit)")
# user_list = carts
# if carts == user_list:
#     print("Here is your Groceries Lists: ")
#     for cart in user_list:
#         print(cart)






    

    
