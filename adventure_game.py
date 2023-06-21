import time
import random
import string

items = []
enemies = ['spirit', 'pirate', 'theif', 'villian']
random.choice(enemies)
enemies = enemies

def typewriter_simulator(message):
    for char in message:
        print(char, end='')
        if char in string.punctuation:
            time.sleep(.5)
        time.sleep(.03)
    print('')

def print_pause(message, delay=.5):
    typewriter_simulator(message)
    time.sleep(delay)

def intro():
    print_pause("Boom!")
    print_pause("There isn't much you can remember and everything feels like a blur. You begin to scan your surrondings.")
    print_pause("You find yourself stranded in an island, filled with sand and coconut trees. You hear animals in the distance so you begin looking for something to defend yourself with.")
    print_pause("As you start exploring, you find different paths you could take. Which one will you embark on? Please enter 1 to walk on the shoreline, 2 to peer into a cave or 3 to go in the forest.")  

def valid_input(prompt, option1, option2, option3):
    while True:
        response = input(prompt)
        if option1 == response:
            house(items)
        elif option2 == response:
            cave(items)
        elif option3 in response:
            forest(items)
        else:
            print_pause("Sorry, I don't understand.")

def fight(items):
    while True:
        if 'orb' in items and 'spear' in items:
            print_pause(f"You have defeated the {enemies} with the help of your new orb companion and your spear. The house is no longer in it's domain so you begin to call it your home! You've now settled by the beach. You won!")
            exit(1)
        elif [] in items:
            print_pause(f"The {enemies} attacks your soul and you are sent to the netherworlds. Please try again!")
            break
            play_again()

def cave(items):
    if 'orb' in items:
        print_pause("You've already been here and it seems to be empty.")
    else:
        print_pause("You enter the cave and find a glowing orb! It starts to orbit around you and becomes your companion!")
        items.append('orb')

def house(items):
    print_pause("You enter the house.")
    if 'orb' in items and 'spear' in items:
        fight(items)
    elif 'orb' in items:
        print_pause("My orb gets out of the house and heads to the forest.")
    elif not items:
        print_pause(f"Looks like there's an {enemies} lurking and I don't have any weapons. I should head back out and explore someplace else.")

def forest(items):
    if 'orb' in items:
        print_pause("My orb guided me to an ancient spear! I think I can defeat the evil spirit by the beach now!")
        items.append('spear')
    else:
        print_pause("I think I need something to activate the spear based on it's humming sounds.")

def map(items):
    area = valid_input("Please enter the number for the area you'd like to explore:",
    "1", "2", "3")  

def play_game():
    while True:
        intro()
        map(items)

play_game() 