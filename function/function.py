def sing_happy_birthday():
    print("Happy Birthday To You")
    print("Happy Birthday To You")
    print("Happy Birthday Dear You")
    print("Happy Birthday To You")

sing_happy_birthday()

# function with return value

nums = [1,2,3,4]
length = len(nums)
print(length) #the function doesnt print anything, but actually returning

def print_square_of_7():
    print(7**2) #without return

print_square_of_7() 

#with return
def square_of_7():
    print("I AM BEFORE THE RETURN!")
    return 7**2
    print("I AM AFTER THE RETURN!")


result = square_of_7()
print(result)

# Naming Parameters
