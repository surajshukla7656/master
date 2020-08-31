"""  This program is for creating functions for the
execution of different operations in the book shop 
database  """


# establishing connection between mysql server and this module
import mysql.connector

try :
    connection=mysql.connector.connect(
        user='surajshukla7656',
        host="localhost",
        database="book_shop",
        password="shukla"
    )

    print('connection established successfully!')
    
    cursor=connection.cursor(dictionary=True)
    
except :

    print("""Something went wrong!
TRY AGAIN""")

finally:
    pass    



#program to verify the existing user with his/her user password
def credential_verifications():

    """this function accepts registered username and password and verify them from the users table 
    and then allow the access of database""" 
       
    try :
        #userName,userPassword=input("Enter username and password:").split()
        userName,userPassword="owner","123"

        cursor.execute("select username,userpassword from users")

        users=cursor.fetchall() # an instance containing username and userpassword

        for user in users:

            if user["username"] == userName:

                if user["userpassword"]==userPassword:
                    print()
                    print(f"login successfully as {userName}")

                    return userName
                    break
                    
            else:
                print(f"user {userName} does not exits")
                credential_verifications()
        
    except:

        print("""something went wrong!
TRY AGAIN!""")

        credential_verifications()
    
    finally:
        pass



#function to execute welcome message 
def welcome_message():

    print()

    print("""welcome!
to the book shop database management editor
created by SURAJSHUKLA""")

    print()

# to kill connection and cursor object
def connection_close():
    cursor.close()
    connection.close()

#to execute the command instantly
def commit():
    connection.commit()

#function to add users to allow the access of database
def add_user(username,userpassword,userid=None):

    try:

        val=(userid,username,userpassword)
        cursor.execute("insert into users values(%s,%s,%s)",val)
        commit()

    except:

        print("unable to add user")
    
#show relations present in database
def show_relations():

    cursor.execute("show tables")

    for table in cursor:
        print(table)

#show registered users 
def show_users():

    cursor.execute("select username from users")
    
    for user in cursor:

        if user==None:
            print("Not have any registered user")

        print(user)

# to remove registered users
def remove_user(username):

    val=(username,)
    cursor.execute("delete from users where username=%s",val)
    commit()

# to create a new categories of book
def create_new_book_category(category):
    cursor.execute("show tables")
    
    for relation in cursor:

        if relation==category:
            print("this category already present")
    
    else:

        sql=f"""create table if not exists {category}(
        bookID int not null primary key auto_increment,
        bookname varchar(50) not null unique,
        book_type varchar(20) not null,
        price decimal(9,2),
        specifications varchar(200))"""

        cursor.execute(sql)
        print(cursor)
        print(f"new book category({category}) created")

        commit()

# to show all the categories of books available
def show_all_category():
    cursor.execute("show tables")
    tables=cursor.fetchall()

    for category in tables:
        if category['Tables_in_book_shop']!="users":
            print(category['Tables_in_book_shop'])

# to remove any existing category of book
def remove_category(category):
    try :
        sql=f"drop table {category}"
        cursor.execute(sql)
        commit()
    
    except:
        print(f"{category} books does not exists")

# to add books according to its category
def add_books(category,bookname,book_type,price,spec=None,id=None):
    try:
        sql=f"insert into {category}"+" values(%s,%s,%s,%s,%s)"
        print(sql)
        category=(id,bookname,book_type,price,spec)
        cursor.execute(sql,category)
        commit()
    except:
        print("something went wrong!")

#driver's code
if __name__=="__main__":
    #add_user("suraj","s")
    # show_relations()
    # show_users()
    #remove_user("suraj")
    #user=credential_verifications()
    #create_new_book_category("cbse")
    show_all_category()
    remove_category("cbse")
    show_all_category()
    add_books("iitjee","hc verma",345)