# imported module
import pro1  as main

# main menu
def menu():

    print(main.color(),'*'*5,f'{main.color(4)}MENU DRIVER{main.color()}','*'*5)

    
    # welcome message 
    main.welcome_message()


    #infinite loop
    while True:

        # try:
            #prompt
            prompt=input(f'{main.color(5)}Prompt${main.color()} ')

            #operations
            if prompt!="":
                
                # to exit
                if prompt=='exit()' or prompt=='e()':

                    print('bye')
                    
                    break
                
                # performing operations
                else:

                    eval(f'main.{prompt}')

        # except:

        #     print('Invalid Input!\n')
           
        #     continue


            
menu()