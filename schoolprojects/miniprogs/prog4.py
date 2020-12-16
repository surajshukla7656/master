# python program to create a binary file with roll number,name and marks
# input a roll number and update the marks

import pickle
import sys 

# addition
def AddStudents(file):

    with open(file,'ab') as f :

        try :

            name=input('Enter name of student : ')
            roll_number=int(input('Enter roll number : '))
            print('Marks in five subject :')
            cs=int(input('\tEnter marks of cs : '))
            eng=int(input('\tEnter marks of english : '))
            phy=int(input('\tEnter marks of physics : '))
            chem=int(input('\tEnter marks of chemistry : '))
            math=int(input('\tEnter marks of math : '))

        except:

            print('Invalid Input')

        else:
            l=[name,roll_number,[cs,eng,phy,chem,math]]
            pickle.dump(l,f)


# to search by roll number 
def update(file):

    with open(file,'rb+') as f:

        try :

            roll_number=int(input('Enter roll number to search : '))

        except:

            print('Invalid Input')

        else:

            try:
                while True:

                    pos=f.tell()
                    l=pickle.load(f)

                    if l[1]==roll_number:
                        print('Record Found!')
                        print('Current details : ')
                        print('\tname :',l[0])
                        print('\troll number : ',l[1])
                        print('\tmarks in cs : ',l[2][0])
                        print('\tmarks in end : ',l[2][1])
                        print('\tmarks in phy : ',l[2][2])
                        print('\tmarks in chem : ',l[2][3])
                        print('\tmarks in math : ',l[2][4])
                        
                        cs=int(input('\tEnter marks of cs : '))
                        eng=int(input('\tEnter marks of english : '))
                        phy=int(input('\tEnter marks of physics : '))
                        chem=int(input('\tEnter marks of chemistry : '))
                        math=int(input('\tEnter marks of math : '))

                        l[2][0]=cs
                        l[2][1]=eng
                        l[2][2]=phy
                        l[2][3]=chem
                        l[2][4]=math

                        f.seek(pos)

                        pickle.dump(l,f)

                        Found=True

                        break

                f.seek(0)
            
            except :

                print('Student not found!')
    f.close()

# driver's code
if __name__=='__main__':

    file=sys.argv[1]

    AddStudents(file)
    AddStudents(file)
    AddStudents(file)
    AddStudents(file)
    AddStudents(file)

    print()
    update(file)