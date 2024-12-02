import csv
import sys


def main():
    # Expects the user to provide two command-line arguments:
    if len(sys.argv) != 3:
        sys.exit("Wrong parameters")
    arg1, arg2 = sys.argv[1],sys.argv[2]
    output(arg1,arg2)

# Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.
def output(arg1,arg2):
    # the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
    try:
        rows = []
        with open(arg1,"r") as csv_before:
            before_reader = csv.DictReader(csv_before)
            for row in before_reader:
                last_name, first_name = row["name"].split(",")
                names = {"first":first_name, "last": last_name, "house": row["house"]}
                rows.append(names)
        # the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
        with open(arg2,"w") as csv_after:
            fieldnames = ["first","last","house"]
            after_writer = csv.DictWriter(csv_after, fieldnames=fieldnames)
            after_writer.writeheader()
            for row in rows:
                after_writer.writerow({"first":row["first"].strip(), "last":row["last"],"house":row["house"]})
    except(FileNotFoundError,IndexError):
        sys.exit("File not found")


if __name__ == "__main__":
    main()


