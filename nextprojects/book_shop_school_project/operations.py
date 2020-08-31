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
    cursor=connection.cursor()
    
except :
    print("""Something went wrong!
TRY AGAIN""")
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
    val=(userid,username,userpassword)
    cursor.execute("insert into users values(%s,%s,%s)",val)
    commit()
    
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

#driver's code
if __name__=="__main__":
    # add_user("001","owner","bookshop123")
    show_relations()
    show_users()
    # remove_user("owner")