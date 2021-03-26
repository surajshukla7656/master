# python program to create a binary file with name and roll number 
# search for a given number and display the name
# if not found display appropriate message


import pickle 

def  add():

    rollnumber=int(input('Enter roll number :'))
    name=input('Enter name: ')
    
    with open('binfile3','ab') as f:

        pickle.dump([rollnumber,name],f)


    f.close()
    print('Record Added')

def search():

    rollnumber=int(input('Enter roll number to search :'))

    try : 
        with open('binfile3','rb') as f:
            while True:
                detail=pickle.load(f)

                if detail[0]==rollnumber:
                    print('Record Found')
                    print('name :',detail[1])

                    break
                
    except :
        print('Record not Found')


if __name__=='__main__':

    add()
    add()
    search()

