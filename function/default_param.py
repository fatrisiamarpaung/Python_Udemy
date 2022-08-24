from regex import P


def exponent(num, power=2):
    """ exponent(num, power) raises num to specified power. Power default to ."""
    return num ** power

print(exponent(2, 3))
print(exponent(3))
print(exponent(7))
print(exponent.__doc__)

# keyword arguments
print(exponent(power=3, num=4))
print(exponent( num=4, power=3))

# Multiple default parameter
def show_information(first_name="Fatrisia", is_instructor=False):
    if first_name == "Fatrisia" and is_instructor:
        return "Welcome back instructor Fatrisia!"
    elif first_name == "Fatrisia":
        return "I really thought you were an instructor..."
    return f"Hello {first_name}!"

print(show_information())
print(show_information(is_instructor=True))
print(show_information('Molly'))

# another example
def add(a,b):
       return a+b

def math(a,b, fn=add):
       return fn(a,b)

def subtract(a,b):
       return a-b

print(math(2, 2)) #4
print(math(2, 2, subtract)) #0
