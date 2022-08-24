# Create a new sets
s = {1, 4, 5, 4, 5}
print(s)

# print(s[0]) #set gabisa diakses melalui index

print("-------------------------------------------")

# Test each element in a set
print(4 in s) #True
print(6 in s) #False

print("-------------------------------------------")

# Accessing all values in sets using loop
for number in s:
    print(number)

print("-------------------------------------------")

# Convert into a set
cities = ["Los angeles", "Boulder", "Kyoto", "Florence", "Santiago", "Los Angeles", "Shanghai", "Boulder", "San Franscisco", "Oslo", "Tokyo"]
print(set(cities))
print(list(set(cities)))
print(len(set(cities)))

e = set(cities)
print(e)

print("-------------------------------------------")

# Set Method
# add: adds an element to a set. If the element is already in the set, the set does not change
cities = {"Los angeles", "Boulder", "Kyoto", "Florence", "Santiago", "Los Angeles", "Shanghai", "Boulder", "San Franscisco", "Oslo", "Tokyo"}
cities.add("Vancouver")
# nothing happen when u added same value to set
cities.add("Vancouver")
print(cities)

print("-------------------------------------------")

# remove : removes a value from the set -returns a KeyError if the value is not found
cities = {"Los angeles", "Boulder", "Kyoto", "Florence", "Santiago", "Los Angeles", "Shanghai", "Boulder", "San Franscisco", "Oslo", "Tokyo"}
cities.remove("Kyoto")
print(cities)
cities.discard("Moskow")
print(cities)

print("-------------------------------------------")

# Set Math
# Suppose I teach two classes:
math_students = {"Matthew", "Helen", "Prashant", "James", "Aparna"}
biology_students = {"Jane", "Matthew", "Charlotte", "Mesut", "Oliver", "James"}

print("-------------------------------------------")

# this is how to union or join 2 variables without any duplicate value
print(math_students | biology_students)

print("-------------------------------------------")

# select_intersection is how to select all the same students who join in both courses
print(math_students & biology_students)
