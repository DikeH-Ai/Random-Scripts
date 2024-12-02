# TODO
import re
from cs50 import get_int, get_string
#  using regex validate input
pattern = '[\d]'
keepgoing = True
while keepgoing:
    user_input = get_string("Number: ")
    if (re.search(pattern, user_input)):
        keepgoing = False

array = []
vary = ""
vary1 = ""
total = 0
# for even user_input data(even checker)
if (len(user_input) % 2) == 0:
    for index in range(0, len(user_input), 2):
        # store the index value in value
        value = user_input[index]
        # check if index is even
        if index % 2 == 0:
            # multipy the index value by 2
            value = int(value) * 2
        # convert back to string
            new_value = str(value)
        # store in string variable
            vary += new_value

    add = 0
# loop through the string variable
    for i in vary:
        # add all the values together
        add += int(i)

# loop through user input selecting specific numbers with odd indexes
    for index in range(len(user_input)):
        # store the index value in value
        value = user_input[index]
    # check if index is odd
        if index % 2 != 0:
            # store in string variable
            vary1 += value

    add1 = 0
# loop through the string variable
    for i in vary1:
        # add all the values together
        add1 += int(i)

    total = add + add1
else:
    # for odd user_input data(odd checker)
    for index in range(1, len(user_input), 2):
        # store the index value in value
        value = user_input[index]
        # check if index is odd
        if index % 2 != 0:
            # multipy the index value by 2
            value = int(value) * 2
        # convert back to string
            new_value = str(value)
        # store in string variable
            vary += new_value

    add = 0
# loop through the string variable
    for i in vary:
        # add all the values together
        add += int(i)

# loop through user input selecting specific numbers with even indexes
    for index in range(len(user_input)):
        # store the index value in value
        value = user_input[index]
    # check if index is odd
        if index % 2 == 0:
            # store in string variable
            vary1 += value

    add1 = 0
# loop through the string variable
    for i in vary1:
        # add all the values together
        add1 += int(i)

    total = add + add1
# lenght checker
lenght = len(user_input)

# master card checker
masterbool = False
master = ["51", "52", "53", "54", "55"]
if user_input[:2] in master:
    masterbool = True
# if algorithm (total) does not end with a zero
# card checker
if total % 10 != 0:
    print("INVALID")
elif (user_input[:2] == "34" or user_input[:2] == "37") and (lenght == 15):
    print("AMEX")
elif (masterbool == True) and (lenght == 16):
    print("MASTERCARD")
elif (user_input[0] == "4") and (lenght == 13 or lenght == 16):
    print("VISA")
else:
    print("INVALID")
