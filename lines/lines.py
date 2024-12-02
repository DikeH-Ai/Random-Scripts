# import sys
import sys

def main():
    # implement a program that expects exactly one command-line argument, the name (or path) of a Python file, and
    if len(sys.argv) != 2:
        sys.exit("wrong parameter")
    para = sys.argv[1]
    checks(para)
    print(lines(para))

def checks(para):
    # If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .py, or if the specified file does not exist,
    # the program should instead exit via sys.exit.
    try:
        name,extension = para.split(".")
    except:
        sys.exit("No Extension")
    else:
        if extension != "py":
            sys.exit("Not a python file")

# outputs the number of lines of code in that file, excluding comments and blank lines.'
def lines(arg):
    number = 0
    try:
        with open(arg) as file:
            l = file.readlines()
            for line in l:
                # Assume that any line that starts with # optionally preceded by whitespace, is a comment.
                if line.strip().startswith("#") or line.isspace():
                    pass
                else:
                    number += 1
        return number
    except(FileNotFoundError):
        sys.exit("File does not exist")


main()