import csv
from tabulate import tabulate
import sys

def main():
    # expects exactly one command-line, a csv file
    if len(sys.argv) != 2:
        sys.exit("Wrong parameters")
    csv_file = sys.argv[1]
    checks(csv_file)
    formatted_table(csv_file)

def checks(csv_file):
    # if the file does not end in .csv
    try:
        name, extension =  csv_file.split(".")
    except:
        sys.exit("Wrong file type")
    else:
        if extension != "csv":
            sys.exit("Not a CSV file")

def formatted_table(csv_file):
    # outputs a table formatted in ascii
    try:
        with open(csv_file,"r") as csv_file:
            csv_reader = csv.reader(csv_file)
            print(tabulate(list(csv_reader), headers="firstrow", tablefmt="grid"))
    # if the specified file does not exist == programme should exit
    except(FileNotFoundError):
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()