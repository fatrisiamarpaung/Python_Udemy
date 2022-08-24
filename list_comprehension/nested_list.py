
# Nested List
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Akses List
print(nested_list[0][1]) # akses list pertama dengan index 1 -> 2
print(nested_list[1][-1]) # akses list kedua dengan indek -1 -> 6
print(nested_list[-1][-2]) #8


# Printing Values
for l in nested_list:
    for val in l:
        print(val)

# Nested List Comprehension
[[print(val) for val in l] for l in nested_list]

# Another example
board = [[num for num in range(1,4)] for val in range(1,4)]
print(board)

print([["X" if num % 2 != 0 else "O" for num in range(1, 4)] for val in range(1, 4)])
