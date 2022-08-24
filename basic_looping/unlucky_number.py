
# Loop through numbers 1-20
# For 4 and 13, print "x is unlucky"
# For even numbers, print "x is even"
# For odd numbers, print "x is odd"

for num in range(1, 21):
    if num == 4 or num == 13:
       print(f"{num} is unlucky")
    elif num % 2 == 0 :
       print(f"{num} is even")
    else:
        print(f"{num} is odd")

for num in range(1, 21):
    if num == 4 or num == 13:
       state = "unlucky"
    elif num % 2 == 0 :
       state = "even"
    else:
        state = "odd"
    print(f"{num} is {state}")

  


