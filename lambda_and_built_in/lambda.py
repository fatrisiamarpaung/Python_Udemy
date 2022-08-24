
#function
from regex import B


def square(num): return num * num

#Using lambda
square2 = lambda num: num * num
add = lambda a,b : a + b

print(square2(7))
print(add(3,20))

print(square.__name__)
print(square2.__name__)
print(add.__name__)

print("--------------------------------------------")

#map
nums = [2, 4, 6, 8, 10]
doubles = list(map(lambda x: x*2, nums))

print(doubles)
# print(type(doubles))

people = ["Darcy", "Christina", "Dana", "Annabel"]

peeps = map(lambda name: name.upper(), people)

print(list(peeps))

print("--------------------------------------------")

names = [
    {'first':'Rusty', 'last':'Stelee'},
    {'first':'Colt', 'last':'Stelee', },
    {'first':'Blue', 'last':'Stelee', }

]

first_names = list(map(lambda x: x['first'], names))
print(first_names) #['Rusty', 'Colt', 'Blue']

print("--------------------------------------------")

#filter
l = [1, 2, 3, 4]
evens = list(filter(lambda x: x % 2 == 0, l))
print(evens) # [2, 4]

names = ["austin", "penny", "anthony", "angel", "billy"]
a_names = filter(lambda n: n[0]=='a', names)
print(list(a_names))

