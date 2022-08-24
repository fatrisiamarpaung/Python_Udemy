row = 5

for i in range(5,0,-1):   
    for j in range(0,i-1 ):
        print("*", end=" ")
    print(i)

row = 5
for i in range(0, 5):
    for j in range(0, i+1):
        print("*", end=" ")
    print()