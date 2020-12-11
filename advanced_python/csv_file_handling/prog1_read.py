import csv

with open('advanced_python/file_handling_csv/basics.csv') as f:

    reader_object=csv.reader(f,delimiter=',')                                 # returns an iterator of list of lines of the csv  file

    print('reader_object-',reader_object)        
    
    element=next(reader_object)                                               # being an iterator next method can also be used with reader_object

    print('element-',element)

    for row in reader_object:                                                 # first time loop will print next element as next has been used on the object

        print('row-',row)

        print('row_elements-',row[0],row[1])
