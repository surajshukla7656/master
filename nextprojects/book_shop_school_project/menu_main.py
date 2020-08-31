""" menu program that rovides interface to the user to execute 
specific commands on the database"""

import operations

#program to verify the existing user with his/her user password
def credentials_verification():
    """this function accepts registered username and password and verify them from the users table 
    and then allow the access of database"""    
    try :
        username,password=input("Enter username and password:").split()   # input of registered username and password
        print()
        print("")

    except:
        print("""username or password does not match
TRY AGAIN""")
        credentials_verification()

    finally:
        menu()
       
# menu interface for the user
def menu(username="SURAJSHUKLA"):
    operations.welcome_message()
    while True:
        try:
            prompt=input(f"\033[1;32mShuklaBookDepot@{username}$\033[1;37m ")          #input of executing command 

            if prompt=="exit":
                print("bye")
                break

            elif prompt!=None:
                eval(f"operations.{prompt}()")

        except :
            print("invalid command!")

    operations.connection_close()

if __name__=="__main__":
    #credentials_verification()
    menu()
