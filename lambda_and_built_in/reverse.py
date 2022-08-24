from audioop import reverse


nums = [1, 2, 3, 4]
nums.reverse()
print(nums)
print(reversed(nums))

# print(reversed("hello"))
for char in reversed("hello world"):
    print(char)

print("hello"[::-1])

print(list(reversed("hello")))

print(''.join(list(reversed("hello"))))