# This program is a simple computer game where a user guesses a randomly
# generated number between 1 and 100.
# November 8, 2017
# CTI 110 - Random Number Guesssing Game
# Ilona Pelerin
#

import random

# Global variable for the numer of guesses.

guesses = 1

# Main function contains a loop

def main():
    # Initializing local variables
    again = "y"
    # Intro message
    print("Guess the number between 1 and 100 I am thinking of!")
    print()

    # The loop continues generating numbers for the user until
    # he/she no longer wants to play.

    while again.lower() == "y":
        play_game()
        again  = input("Would like to play the game again? (y/n): ")
        print()
        
    print("Thanks for playing!")

# The play_game function gets the number that the user has to guess
# promptes the user for a guess.  If the user guesse incorrectly,
# he/she is notified and is prompted to try again until the right guess.

def play_game():
    # Generating the randome number
    number = random.randint(1, 100)
    # local variable for the counter.
    count = 1

    # Loop for feedback about input and counter.
    while True:
        userGuess = int(input("Enter a number between 1 and 100: "))
        if userGuess > number:
            print("Your number is too high, try again.")
            count += 1

        elif userGuess < number:
            print("Your number is too low, try again.")
            count += 1

        elif userGuess == number:
            print("Congratulations! You guessed the right number in" , count, "guesses.")
            return 
        

# Call the main function
main()

    


