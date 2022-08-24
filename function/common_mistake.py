import re


def sum_odd_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total #return harus dilakukan setelah proses perulangan (diluar loop)


# OLD VERSION
#  def sum_odd_numbers(numbers):
#     total = 0
#     for num in numbers:
#         if num % 2 != 0:
#             total += num
#         return total #wrong indetation bikin outputnya ga sesuai

print(sum_odd_numbers([1, 2, 3, 4, 5, 6, 7]))


# def is_odd_number(num):
#     if num % 2 != 0:
#         return True
#     else: #this unecessary else
#         return False

# You can do this instead
def is_odd_number(num):
    if num % 2 != 0:
        return True
    return False

print(is_odd_number(2))
print(is_odd_number(3))