# imported module
import main

# main menu
def menu():

    print(main.color(),'*'*50,f'{main.color(4)}YOUR PRACTICE SESSION STARTED{main.color()}','*'*50)

    
    # welcome message 
    main.welcome_message()


    #infinite loop
    while True:

        #prompt
        prompt=input(f'{main.color(5)}JEE-ADVANCED-ORGRANIC-CHEMISTRY${main.color()} ')

        #operations
        if prompt!="":

            prompt=main.operator_manager(prompt)
            
            # to exit
            if prompt=='exit()':

                print('bye')
                
                break
            
            # performing operations
            else:

                eval(f'main.{prompt}')

        
menu()