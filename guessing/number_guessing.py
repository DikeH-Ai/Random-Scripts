from random import randint

# This is a number guessing game. The computer will generate a random number between 1 and 100. The player will have to guess the number. If the player guesses the number, they win. If they don't guess the number, they lose.


def main():
    introduction()


# This function will introduce the player to the game. It will ask for the player's name and ask if they would like to play the game. If the player chooses to play, the function will generate a random number between 1 and 100 and ask the player to guess the number. If the player guesses the number, they win. If they don't guess the number, they lose.


def introduction():
    """ Introduce the player to the game and ask if they would like to play. 
    If the player chooses to play, generate a random number between 1 and 100 and ask the player to guess the number.
    If the player guesses the number, they win. If they don't guess the number, they lose.
    """
    print("Welcome to the Number Guessing Game!")
    name = input("What is your name? ")
    print(f"Hello, {name}!")
    play = input("Would you like to play a game? (yes/no) ")
    if play == "yes":
        print("Great! Let's get started!")
        print("I'm thinking of a number between 1 and 100")
        secret_number = randint(1, 100)
        game(secret_number)
    else:
        print("That's okay. Have a great day!")
        exit()


def game(secret_number):
    guess = int(input("Guess the number: "))
    if guess == secret_number:
        print("Congratulations! You guessed the number!")
    elif guess < secret_number:
        print("Too low! Try again.")
        game(secret_number)
    else:
        print("Too high! Try again.")
        game(secret_number)


if __name__ == '__main__':
    main()
