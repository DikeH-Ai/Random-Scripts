import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Checks
    # Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.).
    # using regex capture the hour:minute values
    if result := re.search(r"^(\d{1,2})(:\d{2})?\s(?:AM|PM)\sto\s(\d{1,2})(:\d{2})?\s(?:AM|PM)$",s):
        if int(result.group(1)) > 12:
            raise ValueError
         # if hour value > 12 or minute value > or less than 60
        elif 0 > int(result.group(2)) > 60:
            raise ValueError
    else:
        raise ValueError
    # else raise value error


    # convert function
    # implement a function called convert that expects a str in either of the 12-hour formats below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00).
    # using regex patterns capture the remaining values i.e AM or PM
    # check the formats recieved
    # if AM
        # if 12
            # return zero hour
        # return Time
    # else if PM
        #if not 12
            # return time 12 + init time


if __name__ == "__main__":
    main()