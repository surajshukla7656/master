# menu driven python program for prog10.py
# functions available - Add,display,Search

import sys
import prog10

# menu
def menu(file):

    print(file)
    prog10.welcome_message()

    while True :

        try :
            prompt=input('>>> ')

            prompt=prompt.lower().split()

            if prompt[0]=='search':
                
                command='prog10.{}(\'{}\',\'{}\')'.format(prompt[0],file,prompt[1])
                
                eval(command)

            elif prompt[0]=='e' or prompt[0]=='exit':

                break
            
            else :
                
                command='prog10.{}(\'{}\')'.format(prompt[0],file)
            
                eval(command)

        except:

            print('Invalid Command')

# driver's code 
if __name__=='__main__':

    file=sys.argv[1]

    menu(file)