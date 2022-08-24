from pyfiglet import figlet_format
from termcolor import colored

valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")

# result = pyfiglet.figlet_format("Hi")
# print(result)

def print_art(msg, color):
    if color not in valid_colors:
        color = "magenta"
    ascii_art = figlet_format(msg)
    colored_ascii = colored(ascii_art, color=color)

msg = input("What would you like to print? ")
color = input("What color? ")
print_art(msg, color)