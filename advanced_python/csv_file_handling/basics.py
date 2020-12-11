'''
Methods                          checklist                                    Description

writer                              ##                                        creates a writer object 
reader                              ##                                        returns an iterator 
writerow                            ##                                        takes an iterable with writer object
writerows                           ##                                        takes list of iterable with writer object
DictWriter                          ##                                        creates a dictwriter object
writeheader                         ##                                        writes fieldnames as header(first line of csv)
DictReader                          ##                                        returns an iterator of dict of csv file lines

'''


import csv

# ##### write #####
# with open('advanced_python/file_handling_csv/basics.csv','w') as f:

#     writer_object=csv.writer(f)                                               # creating  a csv writer object for writing

#     writer_object.writerow(['suraj','12'])                                    # takes a iterable 
 
#     writer_object.writerows([('kuldeep',34),('gagan',3),('vinay',3,4)])       # takes a list of iterables


# ##### read #####

# with open('advanced_python/file_handling_csv/basics.csv') as f:

#     reader_object=csv.reader(f)                                               # returns an iterator of lines in the csv file

#     print('reader_object-',reader_object)        
    
#     element=next(reader_object)                                               # being an iterator next method can also be used with reader_object

#     print('element-',element)

#     for row in reader_object:                                                 # first time loop will print next element as next has been used on the object

#         print('row-',row)

#         print('row_elements-',row[0],row[1])


# ##### dictwriter ######

# with open('advanced_python/file_handling_csv/basics.csv','a') as f:

#     fields=('name','age')

#     dict_writer_object=csv.DictWriter(f,fieldnames=fields)                                # fieldnames takes a list containing header elements

#     dict_writer_object.writeheader()                                                      # to write header - first line of csv file

#     l=[{'name':'suraj','age':34},{'name':'gagan','age':33},{'name':'kuldeep','age':43}]   # writerows takes list of iterables

#     dict_writer_object.writerows(l)


# ##### dictReader ###### 

# with open('advanced_python/file_handling_csv/basics.csv','r') as f:

#     dict_reader_object=csv.DictReader(f)                                                 # returns iterator of dict containing csv file data

#     next(dict_reader_object)                                                             # here effect of next nullified
 
#     print('fieldlines-',dict_reader_object.fieldnames)                                   # returns list of elements of first row(headers)

#     next(dict_reader_object)                                                             # here iterator moves on second element

#     print('file content:')
    
#     for i in dict_reader_object:

#         print(i)

