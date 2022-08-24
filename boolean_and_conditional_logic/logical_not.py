
#Logical NOT
age = 78

#Rules:
#2-8 : 2 dollar ticket
#65 : 5 dollar ticket
# 10 dollar for everyone else

if not ((age >= 2 and age <= 8) or age >= 65) :
    print("YOU PAY 10 dollars and are not a child or senior!")
else :
    print("YOU ARE A CHILD OR SENIOR!")

print("-------------------------------------------------------")

# is vs "=="
a = 1
print(a == 1) #True
print(a is 1) #True

a = [1, 2, 3] # a list of numbers
b = [1, 2, 3]
print(a == b) #True ngecek datanya sama atau ngga
print(a is b) #false ngecek posisi di memori nya sama atau engga

