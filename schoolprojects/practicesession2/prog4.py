# program to add data to a csv file that contains customers names and their 
# mobile numbers and read the contents and print on the screen

import csv

def add():

    with open('csvfile','a') as f:
        cusomter_name=input('Enter customer name :')
        mobile_number=int(input('Enter mobile number :'))

        writer_object=csv.writer(f)
        writer_object.writerow([cusomter_name,mobile_number])


def display():

    with open('csvfile','r') as f:

        reader_object=csv.reader(f)
        for i in reader_object:
            print(i)

# driver's code

if __name__=='__main__':
    add()
    add()
    display()