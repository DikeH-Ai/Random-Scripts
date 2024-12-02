import csv
import sys


def main():

    # TODO: Check for command-line usage
    # check commandline argument
    if len(sys.argv) != 3:
        print("Error")
        sys.exit(1)
    # save cmd argv in variables
    fileseq = sys.argv[1]
    filename = sys.argv[2]
    # TODO: Read database file into a variable
    # open/read file
    with open(filename, 'r') as file:
        reader = file.read()
    # TODO: Read DNA sequence file into a variable
    # open/read csv file. "i couldn"t use the 'with open()' command it was quite problematic trying to access the reader later in the code."
    filecsv = open(fileseq, 'r')
    readerseq = csv.DictReader(filecsv)
    # TODO: Find longest match of each STR in DNA sequence
    # create an STR list and store all STR's in it
    STR = ["AGATC", "AATG", "TATC", "TTTTTTCT", "TCTAG", "GATA", "GAAA", "TCTG"]
    # count dictionary to update STR:NUMBER AS KEY:VALUE
    count = {}
    for i in STR:
        maxnum = str(longest_match(reader, i))
        count[i] = maxnum

    # TODO: Check database for matching profiles
    # keepgoib boolean
    keepgoing = False
    # loop through csv file
    for row in readerseq:
        # convert csv file to list for easy comparism operation
        instance = list(count.values())
        instance1 = list(row.values())[1:]
    # save the product of the comparism operation in a variable
    # reference: https://pythonguides.com/check-if-a-list-exists-in-another-list-python/
        confirm = all(item in instance for item in instance1)
    # print name
        if confirm is True:
            keepgoing = True
            print(row['name'])
            return row['name']
    # use keepgoing variable to check if there was a match
    if keepgoing is False:
        print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
