
# Built-in Function

#all : Return True if all elements of the iterable are truthy (or if the iterable is empty)
all([0,1,2,3]) #False
print(all([char for char in 'eio' if char in 'aeiou']))
print(all([num for num in [4,2,10,6,8] if num % 2 == 0]))

print("------------------------------------------------------")

people = ["Charlie", "Casey", "Cody", "Carly", "Christina"]

print(all([name[0] == 'C' for name in people]))
print([name[0]=='C' for name in people])

people.append("Kristin")

print([name[0]=='C' for name in people])
print(all([name[0] == 'C' for name in people]))

nums = [2, 60, 26, 18]
print(all([num % 2 == 0 for num in nums]))

print("------------------------------------------------------")

# any
print(any([0, 1, 2, 3])) #True
print(any([val for val in [1, 2, 3] if val > 2]))
print(any([val for val in [1, 2, 3] if val > 5])) 

print("------------------------------------------------------")

# sorted
more_numbers = [6, 1, 8, 2]
print(sorted(more_numbers))
print(more_numbers)
