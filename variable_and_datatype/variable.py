
# This is how to assign a variable
x = 100
fruit = "Apple"
print(fruit)

# Assigned a variable to other variables
python_is_awesome = 100
just_another_var = python_is_awesome
print(just_another_var)

# Reassigned value of a variable
python_is_awesome = 1337 #so python_is_awesome is no longer 100
print(python_is_awesome)

# Assigned at the same time as other variables
all, at, once = 5, 10, 15
print(all)
print(all, at, once)

print("-------------------------------------------------------------------")

# Data Types 
is_boolean = True #Boolean
#is_boolean = true -> error
print(is_boolean)

is_string = "I am a string" #String
print(is_string)

is_integer = 1000 #Integer
print(is_integer)

is_double = 1.9 #Double
print(is_double)

is_list = [1, 2, 3, 4] #List
print(is_list)

is_dict = {"1":"is one", "2":"is two"} #Dict
print(is_dict)

print("-------------------------------------------------------------------")

#Dynamic Typing : flexible to reassigning variables to different types
awesomeness = True
print(awesomeness) #True

awesomeness = "a dog"
print(awesomeness) #a dog

awesomeness = None 
print(awesomeness) #None

awesomeness = 22 / 7
print(awesomeness) # 3.14

print("-------------------------------------------------------------------")

#None : way of represent nothing
is_none = None
print(is_none)

print("-------------------------------------------------------------------")

#String literals in Python can be declared with either single or double quotes
my_other_str = 'a hat'
my_str = "a cat"
print(my_other_str)
print(my_str)

#If u want to make quote inside a quotes
msg = "he said 'hello there!' " 
msg2 = 'I am "funny"'
# msg3 = "I am "funny"" -> error
print(msg)
print(msg2)

print("-------------------------------------------------------------------")

#String Escape in Python
# \n : to make new line 
new_line = "hello \nworld"  
print(new_line)

# \\ : to make backslash
str = "this is a backslash: \\"
print(str)

#\b for delete 1 character behind
str = "hel\blo"
print(str)

# \' : to make single quote
str = "this is a \'Banana\'"
print(str)

# \' : to make double quote
str = "this is a \"Banana\""
print(str)

print("-------------------------------------------------------------------")

# String Concatenation
str_one = "your"
str_two = "face"
str_three = str_one + " " + str_two
print(str_three)

str_one = "ice"
str_one += " cream"
print(str_one)

print("-------------------------------------------------------------------")

#Formatting String
x = 10
formatted = f"I've told you {x} times already!"
formatted2 = f"I've told you {x + 10} times already!"
formatted3 = "I've told you {} times already!".format(x)

print(formatted)
print(formatted2)
print(formatted3)

print("-------------------------------------------------------------------")

# Strings & Indexes
name = "Chuck"

print(name[0])
print(name[1])
print(name[2])
print(name[-1])

print("-------------------------------------------------------------------")

#Converting Data Types
decimal = 12.5634
integer = int(decimal) #12
print(integer)

print("-------------------------------------------------------------------")

#User Input
name = input("Enter your name here: ") 
print(f"Hi {name}")

data = "What's your favorite color?"
data = input()
print("you said " + data)










