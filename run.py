# Write your code to expect a terminal of 80 characters wide and 24 rows high .

def greet():
    """
    Greeting for main menu. Gathers user name for game
    """
    name = (input("What is your name? \n"))
    print ("Welcome to Wonderland Quest, " + name)
    print ("")


greet()
