# in function
string = "sequoia"
def are_all_vowels_in_string(string):
	return len({char for char in string if char in 'aeiou'}) == 5

print(are_all_vowels_in_string(string))
print({char for char in string if char in 'aeiou'})

set = {1, 2, 3, 2, 1, 4, 5}
print(set)

#example of set comprehension
set = {x**2 for x in range(10)}
print(set)

# we get a dictionary
set = {x:x**2 for x in range(10)}
print(set)

print({char.upper() for char in 'hello'})



