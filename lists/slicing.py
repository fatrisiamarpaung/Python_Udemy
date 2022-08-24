
# Make new lists using slices of the old list

# First Parameter for slice:start
first_list = [1, 2, 3, 4]

print(first_list[1:]) # [2, 3, 4] : memotong dari index ke 1
print(first_list[3:]) # [4] : memotong dari index ke 3
print(first_list[-1:]) # [4]
print(first_list[-3:]) #[2, 3, 4]

print("--------------------------------------------")

# Second Parameter for Slice: end
first_list = [1, 2, 3, 4]

print(first_list[:2]) #[1, 2] : slices sampe index 2, tapi index  dikecualikan
print(first_list[:4]) # [1, 2, 3, 4] : bc there is no index 3, so it gives us everything in the list
print(first_list[1:3]) # [2, 3] : slicing from index of one to index three, tapi index 3 ga diikutkan karna exclusive

print("--------------------------------------------")

# Third Parameter for Slice: step
first_list = [1, 2, 3, 4, 5, 6]

print(first_list[1::2]) # [2, 4, 6] : there’s no end parameter, dimulai dari index ke 1 tapi dilangkahi 2
print(first_list[::2]) #[1, 3]

# with negative numbers, reverse the order
print(first_list[1::-1]) #[2, 1]
print(first_list[:1:-1]) #[6, 5, 4, 3]
print(first_list[2::-1]) # [3, 2, 1]

