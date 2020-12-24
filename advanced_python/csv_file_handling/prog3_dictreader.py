from csv import DictReader

with open('nextpython/advanced_python/csv_file_handling/basics.csv','r') as f:

    reader_instance=DictReader(f)             # return iterator of dict using first line as keys

    print(reader_instance.fieldnames)         # return list of first row

    for i in reader_instance:       

        print(i)

# file 
'''
name,age
suraj,34
gagan,33
kuldeep,43
'''

#output

'''
{'name': 'suraj', 'age': '34'}
{'name': 'gagan', 'age': '33'}
{'name': 'kuldeep', 'age': '43'}
'''















# import csv

# with open('advanced_python/csv_file_handling/basics.csv','r') as f:

# #     dict_reader_object=csv.DictReader(f)                                                 # returns iterator of dict containing csv file data

# #     next(dict_reader_object)                                                             # here effect of next nullified
 
# #     print('fieldlines-',dict_reader_object.fieldnames)                                   # returns list of elements of first row(headers)

# #     next(dict_reader_object)                                                             # here iterator moves on second element

# #     print('file content:')
    
# #     for i in dict_reader_object:

# #         print(i)
#     pass