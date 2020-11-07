# python program to print square, cube , square root ,cube root of numbers of upto 100


import random

while True:

    try :
        x=input('Enter x:')    

        print()

        if x=='e' :

            break

        else:
            x=int(x)

        print('number\tsquare\tcube\t\tsquare root\t\tcube root\n')

        for i in range(2,int(x)+1):

            print(f'{i} - \t- {i**2} - \t - {i**3} - \t - {i**.5} - \t - {i**(1/3)}')

            print()


    except:

        try :
            x,y=x.split()
            
            x=int(x)

            print('number\tsquare\tcube\t\tsquare root\t\tcube root\n')

            for i in range(int(x),int(y)+1):

                print(f'{i} - \t- {i**2} - \t - {i**3} - \t - {i**.5} - \t - {i**(1/3)}')

                print()

        except:

            print('invalid')  


# to highlight data
def color(col=7):

    color=f'\033[1;3{col}m'

    return color

def square(x,y):

    return x**2==y

def cube(x,y):

    return x**3==y

def squareroot(x,y):

    return x**.5

def cuberoot(x,y):

    return x**(1/3)



while True:

    decision=input(f'{color(3)}what(s/c/sr/cr/a/e){color()} : ')

    if decision!='cr' and decision!='sr' and decision!='s' and decision!='c' and decision!='a':

        break

    level=int(input((f'{color(3)}Enter maximum number{color()} : ')))

    print()

    x=random.randrange(2,level)

    while True:

        if decision=='s':

            try:

                a=input(f'{color(6)}Enter of {x}{color()} : ')

                if a=='e':
                    break

                print(square(x,int(a)))

            except:

                print("Only int\n")
                


        elif decision=='c':

            try:
                a=input(f'{color(6)}Enter of {x}{color()} : ')

                if a=='e':
                    break

                print(cube(x,int(a)))

            except:

                print("Only int\n")
                continue


        elif decision=='sr':
            
            try:
                a=input(f'{color(6)}Enter of {x}{color()} : ')

                if a=='e':
                    break

                print(squareroot(x,float(a)))

            except:

                print("Only float\n")
                continue

        elif decision=='cr':

            try:

                a=input(f'{color(6)}Enter of {x}{color()} : ')

                if a=='e':
                    break

                print(cuberoot(x,float(a)))
                
            except:

                print("Only float\n")
                continue
            
        elif decision=='a':

            try :

                a,b,c,d=input(f'{color(6)}Enter of {x}{color()} : ').split()

                print(square(x,int(a)))

                print(cube(x,int(b)))

                print(squareroot(x,int(c)))

                print(cuberoot(x,int(d)))

            except :

                break
        
        x=random.randrange(2,level)

        print()