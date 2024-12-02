import sys
import csv
    
with open(fileseq, 'r') as filecsv:
    readerseq = csv.DictReader(filecsv)
    print(readerseq)