import random
import sys
# If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
# If the guess is larger than that integer, the program should output Too large! and prompt the user again.
# If the guess is the same as that integer, the program should output Just right! and exit.
def main():
    x = lev()
    while True:
        y = guess_num()
        if y < x:
            print("Too small!")
        elif y > x:
            print("Too large!")
        else:
            print("Just right!")
            sys.exit()

# Prompts the user for a level, . If the user does not input a positive integer, the program should prompt again.
# Randomly generates an integer between 1 and , inclusive, using the random module.
def lev():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                x = random.randint(1,level + 1)
                return x
            else:
                continue
        except(ValueError):
            pass
# Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.

def guess_num():
    while True:
        try:
            guess = int(input("guess the number: "))
            if guess > 0:
                return guess
            else:
                continue
        except(ValueError):
                pass

main()

