import colorama
from colorama import Fore
import sys

from termcolor import colored, cprint
from colored import fg

color = fg('blue')
print(color + 'Hello World !!!')
text = colored('Hello, Joudi!', 'red', attrs=['reverse', 'blink'])
print(text)
print(Fore.RED + 'This text is red in color')
print("hi")
