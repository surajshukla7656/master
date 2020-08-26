import book_shop_connector
import operations


def credentials_verification():
    connection=book_shop_connector.connect()

    try :
        username,password=input("Enter username and password:").split()
        prompt=connection.cursor()
        print("connection successfully established!")

    except:
        print("""username or password does not match
TRY AGAIN""")
        credentials_verification()

    finally:
        menu(username)

    


def menu(username="SURAJSHUKLA"):
    operations.welcome_message()
    while True:
        prompt=input(f"\033[1;32m{username}$\033[1;37m ")
        if prompt=="exit":
            print("bye")
            break
        elif prompt!=None:
            eval(f"operations.{prompt}()")
        else:
            print("command not defined!")


menu()
