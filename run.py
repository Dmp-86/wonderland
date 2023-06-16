# Write your code to expect a terminal of 80 characters wide and 24 rows high .
import os
import string
import pyfiglet
import colorama
from colorama import Fore, Back, Style
from places import PLACES
colorama.init(autoreset=True)  # Resets colorama


CURRENT_LOCATION = "01"
NAME = ""


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


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
    global NAME
    art_text = pyfiglet.figlet_format("Wonderland", font="utopiab")
    print(Fore.YELLOW + art_text)
    print(Fore.GREEN + "\tWelcome to Wonderland Quest!")
    print(
        "You're about to embark on a magical journey "
        "through a mystical land..."
    )
    print(Fore.MAGENTA + "\tCan you make it to Wonderland?")
    print("Follow the prompts and choose which direction you want to travel.")
    print(Fore.RED + "But BEWARE! Not everything is as it seems...\n")
    print("Let's start with your name. What shall we call you?")

    while True:
        NAME = input(Fore.CYAN + "Enter your name \n")
        clear()
        if validate_name(NAME):
            print(Fore.GREEN + "Welcome to the Quest, " + NAME)
            break
        else:
            print(
                Fore.RED +
                f"{NAME} is an invalid name! Please enter a valid name."
            )


def arrive_at_place():
    global CURRENT_LOCATION

    # lambda filter to find the place that the user is currently at
    current_location = next(filter(lambda place: place["id"] == CURRENT_LOCATION, PLACES))  # noqa
    next_location = None
    while True:
        print(
            f"You are now at {Fore.MAGENTA}{current_location['location']}{Fore.WHITE}"
        )
        print(current_location["story"])
        print(Fore.GREEN + "Which direction would you like to go next?\n")
        DIRECTIONS = []
        # loop the location's available directions
        for direction in current_location["directions"]:
            # append to the empty DIRECTIONS for validation
            DIRECTIONS.append(direction["command"])
            print(
                f"\tType {Fore.MAGENTA}{direction['command']} "
                f"{Fore.WHITE}to go to the {direction['name']}"
            )
        # ask the user where they want to go
        user_choice = input(Fore.RED + "\nType your direction:\n")
        clear()

        # check that the user's choice is in the available DIRECTIONS
        if user_choice.lower() in DIRECTIONS:
            # grab the matching place ID for the user's choice
            for direction in current_location["directions"]:
                if user_choice.lower() == direction["command"]:
                    # lambda filter to find next location by user's choice ID
                    next_location = next(filter(lambda place: place["id"] == direction["next"], PLACES))  # noqa
                    CURRENT_LOCATION = next_location["id"]
                    # break out of the for-loop
                    break
            # break out of the while-loop
            break
        else:
            # user entered an invalid direction, ask again
            print(
                Fore.RED +
                "{user_choice} is invalid direction - Please try again!\n"
            )

    # go to the next place selected
    if next_location["id"] == str(len(PLACES)):
        wonderland(next_location)
    elif next_location["id"] == str(len(PLACES[-1])):
        unlucky(next_location)
    else:
        arrive_at_place()


def wonderland(next_location):
    global CURRENT_LOCATION
    global NAME
    print(f"Congratulations, {NAME}")
    print(next_location["story"])
    while True:
        play_again = input("\nWould you like to play again? Y or N\n")
        if play_again.lower() == "y":
            CURRENT_LOCATION = "01"
            clear()
            arrive_at_place()
        elif play_again.lower() == "n":
            clear()
            print("Thanks for playing!")
            break
        else:
            clear()
            print(Fore.RED + f"{play_again} is invalid! Please enter Y or N.")


def unlucky(next_location):
    global CURRENT_LOCATION
    global NAME
    print(f"Poor, {NAME}, you didn't make it")
    print(next_location["story"])
    while True:
        play_again = input("\nWould you like to play again? Y or N\n")
        if play_again.lower() == "y":
            CURRENT_LOCATION = "01"
            clear()
            arrive_at_place()
        elif play_again.lower() == "n":
            clear()
            print("Thanks for playing!")
            break
        else:
            clear()
            print(Fore.RED + f"{play_again} is invalid! Please enter Y or N.")

if __name__ == "__main__":
    clear()
    greeting()
    arrive_at_place()
