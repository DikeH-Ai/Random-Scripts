# TODO
# import get_int from cs50 lib
from cs50 import get_int
keepgoing = True
# check if conditions are met
while keepgoing:
    height = get_int("Height: ")
    if height >= 1 and height <= 8:
        keepgoing = False
# loop create half a pyramid
    for i in range(1, height + 1):
        for j in range(1, height):
            print(" ", end="")
        height -= 1
        for k in range(i):
            print("#", end="")
        print("\n", end='')