import csv

with open('advanced_python/file_handling_csv/basics.csv','a') as f:

    fields=('name','age')

    dict_writer_object=csv.DictWriter(f,fieldnames=fields)                                # fieldnames takes a list containing header elements

    dict_writer_object.writeheader()                                                      # to write header - first line of csv file

    l=[{'name':'suraj','age':34},{'name':'gagan','age':33},{'name':'kuldeep','age':43}]   # writerows takes list of dicts

    dict_writer_object.writerows(l)