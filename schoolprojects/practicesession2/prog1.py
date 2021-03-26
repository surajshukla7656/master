# python program to create a binary file having roll numbers and 
# names of the students

#imported module 
import pickle

# creating file
def create_add():
    with open('binfile1','ab') as f:

        roll_number=int(input('Enter roll number: '))
        name=input('Enter name : ')

        pickle.dump([roll_number,name],f)

    f.close()



# search
def search():

    roll_number=int(input('Enter roll number to search: '))

    with open('binfile1','rb') as f:

        try:
            while True:

                detail=pickle.load(f)
                if detail[0]==roll_number:
                    print('Found')
                    print('name of student : ',detail[1])

                    break

        except:
            print('Not found')


#driver's code
if __name__=='__main__':
    create_add()
    create_add()
    search()