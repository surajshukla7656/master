
import main

def menu():
    print(main.color(),'*'*50,f'{main.color(4)}YOUR PRACTICE SESSION STARTED{main.color()}','*'*50)

    main.welcome_message()

    while True:

        prompt=input(f'{main.color(5)}JEE-ADVANCED-ORGRANIC-CHEMISTRY${main.color()} ')

        if prompt!="":
            prompt=prompt.lower()
        
            eval(f'main.{prompt}()')

menu()