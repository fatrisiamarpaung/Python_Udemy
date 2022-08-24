
# append : Add an item to the end of the list
first_list = [1, 2, 3, 4]
first_list.append(5)
print(first_list)  # [1, 2, 3, 4, 5]

print("-----------------------------------------")

# extend : menambah banyak data sekaligus ke akhir list
first_list = [1, 2, 3, 4]

first_list.append([5, 6, 7, 8])
print(first_list) #[1, 2, 3, 4,   [5, 6, 7, 8]]

correct_list = [1, 2, 3, 4]

correct_list.extend([5, 6, 7, 8])
print(correct_list) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("-----------------------------------------")

# insert : Menambah data ke posisi yg diinginkan
first_list = [1, 2, 3, 4]

first_list.insert(2, 'Hi!') #: maksudnya menambah String 'Hi'  di index ke 2
print(first_list) # [1, 2, 'Hi', 3, 4]
first_list.insert(-1, 'The end!')
print(first_list) # [1, 2, 'Hi!', 3, 'The end!', 4] 

nums = [1, 2, 3, 4]
nums.insert(len(nums), "LAST")
print(nums) # [1, 2, 3, 4, 'LAST']

print("-----------------------------------------")

# clear : menghapus semua elemen di list
first_list = [1, 2, 3, 4]

first_list.clear()
print(first_list) # [ ]

print("-----------------------------------------")

# pop : Menghapus elemen yg ingin dihapus, if no index is specified, removes and return last item in the list
first_list = [1, 2, 3, 4]
first_list.pop() #4 : yg dihapus index terakhir yaitu 4
first_list.pop(1) #2 : yg dihapus index ke 1 yaitu 2

print("-----------------------------------------")

# remove: remove the first item from the list whose value is x, throws a ValueError if the item is not found
first_list = [1, 2, 3, 4, 4, 4]
first_list.remove(2) #: menghapus elemen yg valuenya = 2
print(first_list) # [1, 3, 4, 4, 4] 
first_list.remove(4) #: karna 4 ada banyak, yg dihapus yg paling depan
print(first_list) # [1, 3, 4, 4]

print("-----------------------------------------")

# index : return the index of the specified item in the list
numbers = [6, 7, 8, 9, 10]

numbers.index(6) #1 : nyari tau elemen 6 ada di index keberapa, dan elemen 6 ada di index ke 1
numbers.index(9) #4

# Can specify start and end
numbers = [5, 5, 6, 7, 5, 8, 8, 9, 10]

numbers.index(5) #0 : elemen 5 yg paling awal ada di index ke -0
numbers.index(5, 1) #1 : elemen 5 yg kedua ada di index ke -1
numbers.index(5, 2) #4 : : elemen 5 yg ketiga ada di index ke -4

numbers.index(8, 6, 8) #6 : mencari elemen 8 yg ada diantara elemen 8 dan 6


print("-----------------------------------------")

# count : return the number of times x appears in the list
numbers = [1, 2, 3, 4, 3, 2, 1, 4, 10, 2]

numbers.count(2) #3 : elemen 2 muncul sebanyak 3 kali di list
numbers.count(21) #0 : elemen 21 tidak ada didalam list
numbers.count(3) #2: elemen 3 muncul sebanyak 2 kali di list

print("-----------------------------------------")

# reverse : reverse the element of the list (in-place)
first_list = [1, 2, 3, 4]
first_list.reverse()
print(first_list) #[4, 3, 2, 1]

print("-----------------------------------------")

# sort : sort the items of the list (in-place)
another_list = [6, 4, 1, 2, 5]
another_list.sort()
print(another_list) # [1, 2, 4, 5, 6]

print("-----------------------------------------")

# join : is commonly used to convert lists to strings
words = ['Coding', 'Is', 'Fun!']
print(' '.join(words)) # ‘Coding is Fun!’

# another example
name = ['Mr', 'Steele']
print('.   '.join(name)) #’Mr.  Steele’





