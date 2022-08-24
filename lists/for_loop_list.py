
# Use for loop to iterate a list
colors = ["purple", "teal", "magenta", True, 8.45]

for color in colors:
    print(color)

print("----------------------------------")

numbers = [1, 4, 5, 9, 8, 10]
for num in numbers :
    print(num)

print("----------------------------------")

# Using while loop
colors = ["purple", "teal", "magenta", "crimson", "emerald"]

index = 0
while index < len(colors):
    print(f"{index}: {colors[index]}")
    index += 1

print("----------------------------------")

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

# for data in sounds: # cara 1
#     result = data.upper()
#     print(result)

#cara 2
for s in sounds:
    result =''
    result += s.upper()
    print(result)
