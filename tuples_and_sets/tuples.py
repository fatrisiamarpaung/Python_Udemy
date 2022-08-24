alphabet = ('a', 'b', 'c', 'd')
# alphabet[0] = 'o' tuples is immutable
print(alphabet)

# Tuples are commonly used for UNCHANGING data
months = ('January', "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
print(months[-2])

# Creating and Accessing Tuples
first_tuple = (1, 2, 3, 3, 3)

print(first_tuple[1]) #2
print(first_tuple[2]) #3
print(first_tuple[-1]) #3

# second_tuple = tuple(5, 1, 2)
# second_tuple[0] #5


# Tuples can be use as keys in dictionaries:
location = {
    (35.6895, 39.6917) : "Tokyo Office",
    (40.7128, 74.0060) : "New York Office",
    (37.7749, 122.4194) : "San Francisco Office"
}

print(location[(37.7749, 122.4194)])

# Some dictionary methods like .items() return tuples
cat = {"name" : "biscuit", "age" : 0.5, "favorite toy" : "my chapstick"}
print(cat.items())
# when u print out the syntax you will found out that each items is tuples

# Looping in Tuples
months = ('January', "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

for month in months:
    print(month) 

# using while loop
i = len(months) - 1
while i >= 0:
    print(months[i])
    i -= 1

# count : Returns the number of times a value appears in a tuple
x = (1, 2, 3, 3, 3)
print(x.count(1)) #1
print(x.count(3)) #3

# index : Return the index at which a value is found in a tuple
t = (1, 2, 3, 3, 3)
print(t.index(1)) #0
# prinb t(t.index(5)) #ValueError: tuple.index(x): x not in tuple
print(t.index(3)) #2 - only the first matching index is returned


# Methods in Tuples & Nested Tuple
nums = (1, 2, 3, (4, 5), 6, 7)
print(nums[3])

# how to access index in nested tuples
print(nums[3][1])

# slice in tuples
print(nums[0:4]) #it will print 0,1,2,3 because non-inclusive

# Step in tuples
print(nums[0:4:2])
