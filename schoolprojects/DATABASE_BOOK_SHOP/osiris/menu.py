""" menu program that rovides interface to the user to execute 
specific commands on the database"""

import operations
import main
       
# menu interface for the user
def menu():
    username=operations.credential_verifications()
    operations.welcome_message()
    while True:
       
        input_command=input(f"\033[1;35mShuklaBookDepot@{username}$\033[1;37m ")          #input of executing command 
        command=main.operator_manager(input_command)
      
        if command=="exit()":
            print("bye")
            break

        elif command!=None:
            eval(f"operations.{command}")
            operations.commit()
    
    operations.connection_close()

if __name__=="__main__":
    menu()
