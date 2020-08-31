""" menu program that rovides interface to the user to execute 
specific commands on the database"""

import operations
       
# menu interface for the user
def menu():
    username=operations.credential_verifications()
    operations.welcome_message()
    while True:
        try:
            prompt=input(f"\033[1;32mShuklaBookDepot@{username}$\033[1;37m ")          #input of executing command 

            if prompt=="exit":
                print("bye")
                break

            elif prompt!=None:
                eval(f"operations.{prompt}")

        except :
            print("invalid command!")

    operations.connection_close()

if __name__=="__main__":
    menu()
