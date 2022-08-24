
#**kwargs dipakai buat parameter berupa dictionary
def fav_colors(**kwargs):
    print(kwargs)

fav_colors(colt="purple", ruby="red", ethel="teal")

print("----------------------------------------------------")

def fav_colors(**kwargs):
    for person, color in kwargs.items():
        print(f"{person}'s favorite color is {color}")

fav_colors(colt="purple", ruby="red", ethel="teal")
fav_colors(colt="purple", ruby="red", ethel="teal", ted="blue")

print("----------------------------------------------------")

def special_greeting(**kwargs):
    if "David" in kwargs and kwargs["David"] == "special":
        return "You get a special greeting David"
    elif "David" in kwargs:
        return f"{kwargs['David']} David!"
    
    return "Not sure who is this..."

print(special_greeting(David = "Hello"))
print(special_greeting(Bob ='Hello'))
print(special_greeting(David = 'special'))

print("----------------------------------------------------")

# exercise
# Define combine_words below:
def combine_words(word,**kwargs):
    
    if 'prefix' in kwargs:
        return kwargs['prefix'] + word
    elif 'suffix' in kwargs:
        return  word + kwargs['suffix']
    return word

