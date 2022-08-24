print({num: num**2 for num in [1, 2, 3, 4, 5]})

str1 = "ABC"
str2 = "123"
combo = {str1[i] : str2[i] for i in range(0, len(str1))}
print(combo)

# conditional logic with dictionaries
num_list = [1, 2, 3, 4]
print({ num:("even" if num %2 == 0 else "odd") for num in num_list })
print({ num:("even" if num %2 == 0 else "odd") for num in range(1, 100) })

instructor = {'name': 'colt', 'city': 'san francisco', 'color':'purple'}

yeilling_instructor = {(k.upper() if k is 'color' else k) :v.upper() for k, v in instructor.items()}
print(yeilling_instructor)

# exercise
# make sure your solution is assigned to the answer variable so the tests can work!
answer = {count: chr(count) for count in range(65, 91)}