
# len
#This is how to use len in python
import math
from operator import le


print(len('awesome'))
print(len((1, 2, 3, 4)))
print(len([1, 2, 3, 4]))
print(range(0, 10))

print(len({1, 2, 3, 4}))
print(len({'a':1, 'b':2, 'c':2}))

print("----------------------------------------")

#abs
print(abs(-5))
print(abs(5))
print(abs(3.444))
print(abs(-3.444))
print(math.fabs(-4))

print("--------------------------------------------")

#sum
print(sum([1, 2, 3]))
print(sum([1, 2, 3], 10))
print(sum([1, 2, 3], -6))

print("------------------------------------------------")

#round
print(round(10.2)) #10
print(round(1.212121,3)) #1.21  ,3 -> ngambil 3 angka dibelakang koma

print("----------------------------------------------------")

#zip
first_zip = zip([1, 2, 3], [4, 5, 6])
print(list(first_zip))
print(dict(first_zip))

five_by_two = [(0, 1), (1, 2), (2, 3), (3,4), (4,5)]