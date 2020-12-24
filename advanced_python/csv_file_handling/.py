import csv

with open('basics.csv') as f:

    reader_object=csv.DictReader(f)
    
    print(reader_object.fieldnames)
    for i in reader_object:
        print(i)