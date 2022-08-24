
# Logical AND & OR

#AND
age = 6

if age > 2 and age < 8:
    print("YOU PAY CHILD PRICE!!")
else:
    print("YOU PAY ADULT PRICE!")

print(age > 2 and age < 8)
print(age < 6 and age < 8)

# OR
city = input("Where do you live?")

if city == "los angeles" or city == "san francisco" :
    print("YOU LIVE IN CALIFORNIA!")
else:
    print("YOU LIVE SOMEWHERE ELSE")