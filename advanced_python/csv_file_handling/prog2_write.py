import csv 

with open('advanced_python/file_handling_csv/basics.csv','w') as f:

    writer_object=csv.writer(f)                                               # creating  a csv writer object for writing

    writer_object.writerow(['suraj','12'])                                    # takes a iterable 
 
    writer_object.writerows([('kuldeep',34),('gagan',3),('vinay',3,4)])       # takes a list of iterables
