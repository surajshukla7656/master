# python program to ask the user to add,display, and search records of employee stored in a binary file
# employee record contain employee code,name and salary
import pickle

# welcome message
def welcome_message():

    print('Welcome! Employee Management System(mini)')

# adding record
def add(file):

    with open(file,'ab') as f:  

        employee_code=int(input('Enter Employee code : '))

        employee_name=input('Enter Employee Name : ')

        salary=input('Enter Salary of Employee : ')

        employee_record=[employee_code,employee_name,salary]

        pickle.dump(employee_record,f)

        print('Record Added')

# display
def display(file) :

    with open(file,'rb') as f:

        try :
            
            print('\nRecords : \n')

            while True :

                record=pickle.load(f)

                print('Employee code : {}'.format(record[0]))
                print('Employee Name : {}'.format(record[1]))
                print('Salary : {}'.format(record[2]))
                print()
        except :

            print()

    
# search 
def search(file,employee_code):

    with open(file,'rb') as f:

        try :

            while True:

                record=pickle.load(f)

                print(record)
                if record[0]==int(employee_code):

                    print('\nRecord Found\n')

                    print('Employee code : {}'.format(record[0]))
                    print('Employee Name : {}'.format(record[1]))
                    print('Salary : {}'.format(record[2]))

                    break

        except:

            print('Record Not Found')

# driver's code 
if __name__=='__main__':
    
    pass