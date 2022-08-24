i =0
max = 5
for i in range(0, 5):
    for j in range(0, i+1):
        print("*", end=" ")
    print(" ")

print("\n")

l=0
for l in range(0,5):
    for m in range(5, l-1):
        print(" " , end="*")
    print(" ")