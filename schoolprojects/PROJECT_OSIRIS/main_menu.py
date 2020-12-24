'''python program to create a menu interface for the 
performing CRUD in the database'''

# imported module
import main
import mysql.connector

# main menu
def menu():

    # identifying user
    user=main.credential_verifications()

    # welcome message 
    main.welcome_message()


    #infinite loop
    while True:

        try:
            #prompt
            prompt=input(f'\n{main.color(5)}OSIRIS_ELECTRONICS/{user} ${main.color()} ')

            #operations
            if prompt!="":

                prompt=main.operator_manager(prompt)
                
                # to exit
                if prompt=='exit()' or prompt=='e()':

                    print('bye')
                    
                    break
                
                # performing operations
                else:

                    eval(f'main.{prompt}')

        except mysql.connector.Error as error :

            print(f'Error : {error}')

        except :

            print('Error')
        
menu()