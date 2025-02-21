from random import choice
# play rock paper scissors with the computer


def main():
    intro()
    status = True
    points = {
        'player': 0,
        'computer': 0
    }
    while status:
        play(points)
        print(f"Player: {points['player']} Computer: {points['computer']}")
        status = input(
            "Do you want to play again? [Y]es or [N]o: ").upper() == 'Y'

    print("Thanks for playing!")


def intro():
    print("Welcome to Rock Paper Scissors!")
    print("You will be playing against the computer.")
    print("Rock beats scissors, scissors beats paper, paper beats rock.")


def play(points: dict):
    print("ROCK PAPER SCISSORS shoot!")
    player = input("Chose your wepon [R]ock [P]aper [S]cissors: ").upper()
    weapons = ['R', 'P', 'S']
    if player not in weapons:
        print("Invalid choice.")
    computer = choice(weapons)
    print(f"Computer chose {computer}")
    if player == computer:
        print("It's a tie!")
    elif player == 'R' and computer == 'S':
        points['player'] += 1
        print("You win!")
    elif player == 'P' and computer == 'R':
        points['player'] += 1
        print("You win!")
    elif player == 'S' and computer == 'P':
        points['player'] += 1
        print("You win!")
    else:
        points['computer'] += 1
        print("You lose!")


if __name__ == '__main__':
    main()
