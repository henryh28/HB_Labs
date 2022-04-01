from curses import beep
from dis import dis
from json.tool import main
from pickle import TRUE
import random

print('===== Hello! Welcome to the number guessing game. =====')
name = input("Type in your name: ")

# Helper function to help validate user input and convert it to an integer
def get_user_input_as_digit(prompt_string):
    variable_name = input(prompt_string)
    while not variable_name.isdigit():
        variable_name = input(f"Only integer values are acceptable. {prompt_string}")
    return int(variable_name)

# Main game loop
def main_game():
    # Validate and ensure user input is a valid number
    game_active, best_guess_count = True, float('inf')

    while game_active:
        currest_guess_count = 1

        # Validate user input for bottom and top number range from which to play the game
        bottom_range = get_user_input_as_digit("Select minimum number allowed for current round: ")
        top_range = get_user_input_as_digit("Select maximum number allowed for current round: ")

        if bottom_range > top_range:
            bottom_range, top_range = top_range, bottom_range
        secret_number = random.randint(bottom_range, top_range)

        # Validate user input for number_of_guesses
        number_of_guesses = get_user_input_as_digit("How many guesses would you like? ")

        # validate user input for user_guess
        user_guess = get_user_input_as_digit(f'Choose a number between {bottom_range} and {top_range}: ')

        # Check if user guess matches secret number, provides feedback for user
        while user_guess != secret_number:
            currest_guess_count += 1
            number_of_guesses -= 1

            if number_of_guesses < 0:
                print ("You are out of guesses, round over!")
                break

            if user_guess != secret_number:
                print (f"Your guess is too {'low' if user_guess < secret_number else 'high'}, try again. (You have {number_of_guesses} guesses left") 

            # Validate User input 
            user_guess = get_user_input_as_digit(f'Choose a number between {bottom_range} and {top_range}: ')

        if user_guess == secret_number:
            best_guess_count = min(best_guess_count, currest_guess_count)
            print (f"Well done {name}! You found my answer in {currest_guess_count} tries!")

        # Ask the user if they want to keep playing
        while game_active != "y" or game_active != "n" or game_active!= "Y" or game_active != "N":
            game_active = input(f"Do you want to keep playing (y/n)? ")
            if game_active.lower() == "n":
                game_active = False
                return best_guess_count
            elif game_active.lower()  == "y":
                break
                
# Display user game statistics at the end of the game
def display_results(high_score):
    if high_score != float('inf'):
        print (f"congrats {name}, your best score is {high_score} guesses!")
    else:
        print (f"You were not able to guess successfully. :(")

display_results(main_game())



