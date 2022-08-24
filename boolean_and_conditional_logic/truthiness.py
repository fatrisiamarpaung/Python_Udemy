
#Truthiness
#Example 01
if 0:
    print("YAY!!") #gaada output karena 0 itu falsey 

if 1:
    print("YAY!!")

color = 'teal'
print(color != 'purple')

print("-------------------------------------------------------------------")

#Example02
animal = input("enter your favorite animal")

if animal:
    print(animal + " is my favorite too!")
else:
    print("YOU DIDNT SAY ANYTHING!")