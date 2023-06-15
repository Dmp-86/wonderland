# Write your code to expect a terminal of 80 characters wide and 24 rows high .
import os
import string
import colorama
from colorama import Fore, Back, Style
from places import PLACES
colorama.init(autoreset=True) #Resets colorama 

# def crossroads():
#     """
#     Define crossroads function
#     """
#     print ("You find yourself at a crossroads. You know you're close to Wonderland..")
#     print ("Which way would you like to go?")
#     print ("Left takes you to the talking owl. Right takes you to the Cave.")
#     print ("Forward brings you to sleepy Sasquatch")
#     print (Fore.RED + "Type left, right or forward to continue")
#     crossroads = (input("Which direction you would like to travel? \n"))
#     # if


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
        print (Fore.RED + "Invalid name! Please enter a valid name.")
    


CURRENT_LOCATION = "01"


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


def arrive_at_place():
    global CURRENT_LOCATION

    # lambda filter to find the place that the user is currently at
    current_location = next(filter(lambda place: place["id"] == CURRENT_LOCATION, PLACES))
    while True:
        print(f"You are currently at {current_location['location']}")
        print(current_location["story"])
        print(Fore.GREEN + "Which direction would you like to go next?\n")
        DIRECTIONS = []
        # loop the location's available directions
        for direction in current_location["directions"]:
            # append to the empty DIRECTIONS for validation
            DIRECTIONS.append(direction["command"])
            print(f"\tType \"{direction['command']}\" to go to the {direction['name']}")
        # ask the user where they want to go
        user_choice = input("\nType your direction:\n")
        clear()

        # check that the user's choice is in the available DIRECTIONS
        if user_choice.lower() in DIRECTIONS:
            # grab the matching place ID for the user's choice
            for direction in current_location["directions"]:
                if user_choice.lower() == direction["command"]:
                    # lambda filter to find the next location by the user's choice ID
                    next_location = next(filter(lambda place: place["id"] == direction["next"], PLACES))
                    CURRENT_LOCATION = next_location["id"]
                    # break out of the for-loop
                    break
            # break out of the while-loop
            break
        else:
            # user entered an invalid direction, ask again
            print(f"{user_choice} is invalid direction - Please try again!\n")

    # go to the next place selected
    arrive_at_place()

def wonderland():
    current_location == ["id"]


if __name__ == "__main__":
    greeting()
    # clear()
    arrive_at_place()
# crossroads()

