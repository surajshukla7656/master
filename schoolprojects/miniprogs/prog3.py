# python program to create a binary file with name and roll number,
# search for a given number and display the name 
# if not found display approprite message

import pickle
import sys

# addition
def AddStudents(file):

    with open(file,'ab') as f :

        try :

            name=input('Enter name of student : ')
            roll_number=int(input('Enter roll number : '))

        except:

            print('Invalid Input')

        else:

            l=[name,roll_number]
            pickle.dump(l,f)

# to search by roll number 
def Search(file):

    with open(file,'rb') as f:

        try :

            roll_number=int(input('Enter roll number to search : '))

        except:

            print('Invalid Input')

        else:

            try:

                while True:

                    l=pickle.load(f)

                    if l[1]==roll_number:

                        print('Found!')

                        print('name :',l[0])
                        
                        Found=True

                        break
            
            except :

                print('Student not found!')

# driver's code
if __name__=='__main__':

    file=sys.argv[1]


    # AddStudents(file)
    # AddStudents(file)
    # AddStudents(file)
    # AddStudents(file)
    # AddStudents(file)
    # print()
    # Search(file)
    Search(file)