# Prompts the user for a level,n. If the user does not input 1, 2, or 3, the program should prompt again.
# Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with
# digits.
# No need to support operations other than addition (+).
# Prompts the user to solve each of those problem. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total. If the user has still not answered correctly after three tries, the program should output the correct answer.
# The program should ultimately output the user’s score, a number out of 10.

import random


def main():
    result = 0
    level = get_level()
    for _ in range(10):
        x,y = generate_integer(level)
        tries = 0
        while True:
            try:
                z = int(input(f"{x} + {y} = "))
                sum = x + y
            except(ValueError):
                print("EEE")
            else:
                if sum != z:
                    tries += 1
                    print("EEE")
                else:
                    tries = 0
                    break
                if tries == 3:
                    print(f"{x} + {y} = {sum}")
                    result += 1
                    break
    print(f"Score: {10 - result}")



def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
        except(ValueError):
            pass
        else:
              continue


def generate_integer(level):
    try:
        if 0 < level < 4:
            if level == 1:
                x = random.randint(0,10)
                y = random.randint(0,10)
                return x,y
            elif level == 2:
                x = random.randint(10,100)
                y = random.randint(10,100)
                return x,y
            else:
                x = random.randint(100,1000)
                y = random.randint(100,1000)
                return x,y
        else:
            raise ValueError
    except(TypeError):
        raise ValueError


if __name__ == "__main__":
    main()
