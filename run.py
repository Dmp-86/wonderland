# Write your code to expect a terminal of 80 characters wide and 24 rows high .
import string
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def crossroads():
    """
    
    """


def validate_name(name):
    """
    Validate a name entry to only allow names with valid letters.
    """
    
    for char in name:
        if char not in string.ascii_letters:
            return False

    return True


def greeting():
    """
    Greeting for main menu. Gathers user name for game
    """
    
    print ("Welcome to Wonderland Quest!")
    print ("You're about to embark on a magical journey through a mystical land...")
    print ("Can you make it to the forest to .....?")
    print ("Follow the prompts and choose which direction you want to travel.")
    print ("But BEWARE! Not everything is as it seems...\n")
    print ("Let's start with your name. What shall we call you?")
    name = (input("Enter your name \n"))
    if validate_name(name):
        print (Fore.GREEN + "Welcome to the Quest, " + name)
    else:
        print(Fore.RED + "Invalid name! Please enter a valid name.")
    

greeting()
