nums = [1, 2, 3]

# this means every number in nums will multiply by 10
print ([x * 10 for x in nums])

# this means every number in nums will divide by 2
print ([x / 2  for x in nums])

print("----------------------------------------------")

#for looping
numbers = [1, 2, 3, 4, 5]
doubled_numbers = [ ]

for num in numbers:
	doubled_number = num * 2
	doubled_numbers.append(doubled_number)

print(doubled_numbers) #[ 2, 4, 6, 8, 10 ]

print("----------------------------------------------")

#list comprehension
numbers = [1, 2, 3, 4, 5]
doubled_numbers = [num * 2 for num in numbers]
print(doubled_numbers) # [2, 4, 6, 8, 10]

print("----------------------------------------------")

#return every character in string in uppercase
name = "colt"
print ([char.upper() for char in name]) # [‘C’, ‘O’, ‘L’, ‘T’]

print("----------------------------------------------")

#return every first character in uppercase
friends = [ "ashley", "matt", "michael" ]
print ([friend[0].upper() for friend in friends]) #[‘A’, ‘M’, ‘M’]

print("----------------------------------------------")

#using range
number = [num*10 for num in range(1,6)] # [10, 20, 30, 40, 50]
print(number)

print("----------------------------------------------")

# using boolean data type
boolean = [bool(val) for val in [  0, [], ""  ]]  # [False, False, False]
print(boolean)

print("----------------------------------------------")

#convert number to string
numbers = [1, 2, 3, 4, 5]
string_list = [str(num) for num in numbers]
print(string_list) #['1', '2', '3', '4', '5']

string_list = [str(num)+ " HELLO" for num in nums] 
print(string_list)

print("----------------------------------------------")

# List comprehension with logic
numbers = [1, 2, 3, 4, 5, 6]
evens = [num for num in numbers if num % 2 == 0]
odds = [num for nums in numbers if num % 2 != 0]

print([num * 2 if num % 2 == 0 else num / 2 for num in numbers])
# [0.5, 4, 1.5, 8, 2.5, 12]

print("----------------------------------------------")

with_vowels = "This is so much fun!"
print ("".join(char for char in with_vowels if char not in "aiueo"))
#”Ths s s mch fn!”
print([char for char in with_vowels if char not in "aiueo"])

print(''.join(["cool", "dude"]))
print('...'.join(["cool", "dude"]))







