# TODO
from cs50 import get_string, get_int
import re


def main():
    # get strings
    text = get_string("Text: ")
    # get lenght of strings
    lenght = len(text)
    # call funtions
    L = count_letters(text)
    W = count_words(text)
    S = count_sentences(text)
    # coleman-liau index
    L = (L/W) * 100
    S = (S/W) * 100
    index = round(0.0588 * L - 0.296 * S - 15.8)

    if index < 1:
        print("Before Grade 1")
    elif index > 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")

# count letters function


def count_letters(text):
    pattern = "[A-Za-z]"
    letters = re.findall(pattern, text)
    print(len(letters))
    return len(letters)

# count words functiion


def count_words(text):
    words = len(text.split())
    print(words)
    return words

# count sentences function


def count_sentences(text):
    counter = 0
    senten = text
    for i in range(len(senten)):
        if senten[i] == ".":
            counter += 1
        elif senten[i] == "!":
            counter += 1
        elif senten[i] == "?":
            counter += 1
    print(counter)
    return counter


main()
