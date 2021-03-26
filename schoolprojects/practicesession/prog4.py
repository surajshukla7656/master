# python program to create a binary file with roll number, name and marks 
# input a roll number and update the marks

import pickle 


def add():
    
    rollnumber=int(input('Enter roll number : '))
    name=input('Enter name : ')
    print('Enter marks : ')
    cs=int(input('CS : '))
    maths=int(input('Maths :'))
    physics=int(input('Physics : '))
    chemistry=int(input('chemistry :'))
    english=int(input('English :'))
    
    details=(rollnumber,name,{'cs':cs,'maths':maths,'physics':physics,'chemistry':chemistry,'english':english})
    print(details)
    with open('binfile4','ab') as f:

        pickle.dump(details,f)

        print('Record Added')

    f.close()


def update():

    rollnumber=int(input('Enter roll Number :'))

    with open('binfile4','rb+') as f:
        
       try :
            while True :
                pos=f.tell()
                i=pickle.load(f)
                
                if i[0]==rollnumber:
                    for sub,marks in i[2].items():

                        print(f'{sub} : {marks}')
                        new_marks=input('Enter new marks :')

                        if new_marks=='':
                            continue
                        else:
                            i[2][sub]=new_marks
                            details=(rollnumber,i[1],i[2])
                            f.seek(pos)
                            pickle.dump(details,f)
                            print('Record Updated')
                            
                    
        except:
            print('bye')
    f.close()

if __name__=='__main__':

    add()
    update()

                    

