#_name : this is supposed to be a private variable or private property
#__name
#__name__ : the other convention you should respect, you can define your owwn, but you shouldnt

class Person:
    def __init__(self):
        self.name = "Tony"
        self._secret = "Hi!"
        self.__msg = "I like turtles!" #we can print out this one coz of name mangling
        self.__lol = "HAHAHAHHA"
    # def doorman(self,guess):
    #     if guess == self._secret:
    #         let them in

p = Person()

print(p.name)
print(p._secret)
# print(dir(p))

# if we want to print out
print(p._Person__msg)
print(p._Person__lol)

