# A sample project using binary file
# Student Management System
import pickle
import os
from os import path

def add_records():
    stu_list = []
    if path.exists('student_file.dat'):
        file = open('student_file.dat', 'rb')
        stu_list = pickle.load(file)
        file.close()

    while True:
        print('Enter details of the student:')
        adm_no = int(input('\tAdmission No.: '))
        roll_no = int(input('\tRoll No.: '))
        name = input('\tName: ')        
        print('\tMarks in 5 subjects: ')
        english = int(input("\t\tEnglish Marks: "))
        math = int(input("\t\tMathematics marks: "))
        computers = int(input("\t\tComputer Sc. Marks: "))
        physics = int(input("\t\tPhysics Marks: "))
        chemistry = int(input("\t\tChemistry Marks: "))
        total_marks  = english + math + computers + physics + chemistry
        percentage = (total_marks / 500) * 100
        stu_rec = [adm_no, roll_no, name, total_marks, percentage]
        stu_list.append(stu_rec)
        choice = input('Want ot add more records(y/n)?: ')
        if choice == 'n' or choice == 'N':
            break
    print('Appending data...')
    file = open('student_file.dat', 'wb')
    pickle.dump(stu_list, file)
    file.close()

def display_records():
    file = open('student_file.dat', 'rb')
    print('*' * 78)
    print('The content of the file...')
    try:
        while True:
            stu_list = pickle.load(file)
            for record in stu_list:
                print('\n\tAdmission No.: ', record[0])
                print('\tRoll No.: ', record[1])
                print('\tName: ', record[2])
                print('\tTotal marks: ', record[3])
                print('\tPercentage: ', record[4])
    except Exception:
        file.close()
    finally:
        print('*' * 78)

def search_record():
    file = open('student_file.dat', 'rb')
    rno = int(input('Student roll no. to be searched: '))
    found = False
    try:
        while True:
            stu_list = pickle.load(file)
            for record in stu_list:
                if record[1] == rno:
                    print('Record found')
                    print('\tAdmission No.: ', record[0])
                    print('\tRoll No.: ', record[1])
                    print('\tName: ', record[2])
                    print('\tTotal marks: ', record[3])
                    print('\tPercentage: ', record[4])
                    found = True
                    break
    except Exception:
        file.close()
    finally:
        if found == False:
            print('Record not found.')

def update_record():
    file = open('student_file.dat', 'rb+')
    rno = int(input('Student roll no. to be updated: '))
    found = False
    list = []
    stu_list = pickle.load(file)
    for record in stu_list:
        if record[1] == rno:
            print('Record found')
            print('The current details:')
            print('\tAdmission No.: ', record[0])
            print('\tRoll No.: ', record[1])
            print('\tName: ', record[2])
            print('\tTotal marks: ', record[3])
            print('\tPercentage: ', record[4])
            print('Now enter new details:')
            record[0] = int(input('\tAdmission No.: '))
            record[1] = int(input('\tRoll No.: '))
            record[2] = input('\tName: ')
            print('\tMarks in 5 subjects: ')
            english = int(input("\t\tEnglish Marks: "))
            math = int(input("\t\tMathematics marks: "))
            computers = int(input("\t\tComputer Sc. Marks: "))
            physics = int(input("\t\tPhysics Marks: "))
            chemistry = int(input("\t\tChemistry Marks: "))
            total_marks  = english + math + computers + physics + chemistry
            percentage = (total_marks / 500) * 100
            record[3] = total_marks
            record[4] = percentage
            found = True
        list.append(record)
    if found == True:
        file.seek(0)
        pickle.dump(list, file)
        print('Record updated successfully')
    else:
        print('Record not found')
    
    file.close()

def delete_record():
    file = open('student_file.dat', 'rb+')
    rno = int(input('Student roll no. to be DELETED: '))
    found = False
    list = []
    stu_list = pickle.load(file)
    for record in stu_list:
        if record[1] != rno:
            list.append(record)
        else:
            found = True
    if found == True:
        file.seek(0)
        pickle.dump(list, file)
        print('Record DELETED successfully')
    else:
        print('Record not found')
    
    file.close()

def show_choices():
    print('\n\nMenu')
    print('1. Add Record')
    print('2. Display Records')
    print('3. Search a Record')
    print('4. Update a Record')
    print('5. Delete a Record')
    print('6. Exit')

def welcome():
    print('Welcome to Student Management System')
    print('RPVV Raj Niwas marg, Delhi-110054')

def main():
    welcome()
    while True:
        show_choices()
        choice = input('Enter choice(1-6): ')
        print()
        
        if choice == '1':
            add_records()
            
        elif choice == '2':
            display_records()

        elif choice == '3':
            search_record()

        elif choice == '4':
            update_record()
        
        elif choice == '5':
            delete_record()
        
        elif choice == '6':
            break
        
        else:
            print('Invalid input')
            
#call the main function.
main()




# run and output:

# Welcome to Student Management System
# RPVV Raj Niwas marg, Delhi-110054


# Menu
# 1. Add Record
# 2. Display Records
# 3. Search a Record
# 4. Update a Record
# 5. Delete a Record
# 6. Exit
# Enter choice(1-6): 1

# Enter details of the student:
#         Admission No.: 1001
#         Roll No.: 1
#         Name: Kunal Sharma
#         Marks in 5 subjects: 
#                 English Marks: 99
#                 Mathematics marks: 100
#                 Computer Sc. Marks: 100
#                 Physics Marks: 98
#                 Chemistry Marks: 98
# Want ot add more records(y/n)?: y
# Enter details of the student:
#         Admission No.: 1002
#         Roll No.: 2
#         Name: Pawan Joshi
#         Marks in 5 subjects: 
#                 English Marks: 98
#                 Mathematics marks: 99
#                 Computer Sc. Marks: 100
#                 Physics Marks: 98
#                 Chemistry Marks: 95
# Want ot add more records(y/n)?: n
# Appending data...


# Menu
# 1. Add Record
# 2. Display Records
# 3. Search a Record
# 4. Update a Record
# 5. Delete a Record
# 6. Exit
# Enter choice(1-6): 2

# **************************
# The content of the file...

#         Admission No.:  1001
#         Roll No.:  1
#         Name:  Kunal Sharma
#         Total marks:  495
#         Percentage:  99.0

#         Admission No.:  1002
#         Roll No.:  2
#         Name:  Pawan Joshi
#         Total marks:  490
#         Percentage:  98.0
# **************************


# Menu
# 1. Add Record
# 2. Display Records
# 3. Search a Record
# 4. Update a Record
# 5. Delete a Record
# 6. Exit
# Enter choice(1-6): 3

# Student roll no. to be searched: 1
# Record found
#         Admission No.:  1001
#         Roll No.:  1
#         Name:  Kunal Sharma
#         Total marks:  495
#         Percentage:  99.0


# Menu
# 1. Add Record
# 2. Display Records
# 3. Search a Record
# 4. Update a Record
# 5. Delete a Record
# 6. Exit
# Enter choice(1-6): 3

# Student roll no. to be searched: 4
# Record not found.


# Menu
# 1. Add Record
# 2. Display Records
# 3. Search a Record
# 4. Update a Record
# 5. Delete a Record
# 6. Exit
# Enter choice(1-6): 4

# Student roll no. to be updated: 2
# Record found
# The current details:
#         Admission No.:  1002
#         Roll No.:  2
#         Name:  Pawan Joshi
#         Total marks:  490
#         Percentage:  98.0
# Now enter new details:
#         Admission No.: 1002
#         Roll No.: 2
#         Name: Pawan Joshi
#         Marks in 5 subjects: 
#                 English Marks: 99
#                 Mathematics marks: 100
#                 Computer Sc. Marks: 100
#                 Physics Marks: 96
#                 Chemistry Marks: 97
# Record updated successfully


# Menu
# 1. Add Record
# 2. Display Records
# 3. Search a Record
# 4. Update a Record
# 5. Delete a Record
# 6. Exit
# Enter choice(1-6): 2

# **************************
# The content of the file...

#         Admission No.:  1001
#         Roll No.:  1
#         Name:  Kunal Sharma
#         Total marks:  495
#         Percentage:  99.0

#         Admission No.:  1002
#         Roll No.:  2
#         Name:  Pawan Joshi
#         Total marks:  492
#         Percentage:  98.4
# **************************


# Menu
# 1. Add Record
# 2. Display Records
# 3. Search a Record
# 4. Update a Record
# 5. Delete a Record
# 6. Exit
# Enter choice(1-6): 1

# Enter details of the student:
#         Admission No.: 1003
#         Roll No.: 3
#         Name: Kirti Bisht
#         Marks in 5 subjects: 
#                 English Marks: 98
#                 Mathematics marks: 97
#                 Computer Sc. Marks: 98
#                 Physics Marks: 95
#                 Chemistry Marks: 96
# Want ot add more records(y/n)?: n
# Appending data...


# Menu
# 1. Add Record
# 2. Display Records
# 3. Search a Record
# 4. Update a Record
# 5. Delete a Record
# 6. Exit
# Enter choice(1-6): 2

# **************************
# The content of the file...

#         Admission No.:  1001
#         Roll No.:  1
#         Name:  Kunal Sharma
#         Total marks:  495
#         Percentage:  99.0

#         Admission No.:  1002
#         Roll No.:  2
#         Name:  Pawan Joshi
#         Total marks:  492
#         Percentage:  98.4

#         Admission No.:  1003
#         Roll No.:  3
#         Name:  Kirti Bisht
#         Total marks:  484
#         Percentage:  96.8
# **************************


# Menu
# 1. Add Record
# 2. Display Records
# 3. Search a Record
# 4. Update a Record
# 5. Delete a Record
# 6. Exit
# Enter choice(1-6): 5

# Student roll no. to be DELETED: 2
# Record DELETED successfully


# Menu
# 1. Add Record
# 2. Display Records
# 3. Search a Record
# 4. Update a Record
# 5. Delete a Record
# 6. Exit
# Enter choice(1-6): 2

# **************************
# The content of the file...

#         Admission No.:  1001
#         Roll No.:  1
#         Name:  Kunal Sharma
#         Total marks:  495
#         Percentage:  99.0

#         Admission No.:  1003
#         Roll No.:  3
#         Name:  Kirti Bisht
#         Total marks:  484
#         Percentage:  96.8
# **************************


# Menu
# 1. Add Record
# 2. Display Records
# 3. Search a Record
# 4. Update a Record
# 5. Delete a Record
# 6. Exit
# Enter choice(1-6): 7

# Invalid input


# Menu
# 1. Add Record
# 2. Display Records
# 3. Search a Record
# 4. Update a Record
# 5. Delete a Record
# 6. Exit
# Enter choice(1-6): 6