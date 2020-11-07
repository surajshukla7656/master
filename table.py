#python program to access tables 

def table(num):
    for i in range(1,11):

        print(f'{num} x {i} = {num*i}')

def table_in_range(num,vertical=False):

    num1,num2=num.split()

    if vertical==True:

        for x in range(1,11):

            for y in range(int(num1),int(num2)+1):

                print(x*y,end='\t')

            print('\t')


    else:

        for x in range(int(num1),int(num2)+1):

            for y in range(1,11):

                print(x*y,end=' ')

            print()
            print()


while True:

    num=input('Enter number:')

    try :

        if num=='e':

            break

        num=int(num)

        table(num)

        print()

    except:

        try :
            table_in_range(num)

            print()

        except:
            print('invalid')
        
            
                