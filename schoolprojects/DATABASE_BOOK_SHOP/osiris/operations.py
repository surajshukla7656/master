'''  This program is for creating functions for the
execution of different operations in the book shop 
database  '''

import random
# establishing connection between mysql server and this module
import mysql.connector

try :
    connection=mysql.connector.connect(
        user='surajshukla7656',
        host="localhost",
        database="online_book_store",
        password="shukla"
    )

    print()
    print(F'\033[1;32m{"*"*50} CONNECTION ESTABLISHED SUCCESSFULLY! {"*"*50}\033[1;37m' )
    
    cursor=connection.cursor(dictionary=True)
    
except :

    print('''Something went wrong!
TRY AGAIN''')

finally:
    pass    



#program to verify the existing user with his/her user password
def credential_verifications():

    '''this function accepts registered username and password and verify them from the users table 
    and then allow the access of database'''
       
    try :
        #userName,userPassword=input("Enter username and password:").split()
        userName,userPassword="owner","123"

        cursor.execute('SELECT USERNAME,USERPASSWORD FROM USERS')

        users=cursor.fetchall() # an instance containing username and userpassword

        for user in users:

            if user["USERNAME"] == userName:

                if user["USERPASSWORD"]==userPassword:
                    print()
                    print(f'login successfully as \033[1;33m{userName}\033[1;37m ')

                    return userName
                    break
                    
            else:
                print(f'user {userName} does not exits')
        
                    
    except:

        print('''something went wrong!
TRY AGAIN''')

        credential_verifications()
    
    finally:
        pass



#function to execute welcome message 
def welcome_message():

    print()

    print('''WELCOME !
TO THE BOOSHOP DATABASE MANAGEMENT CONSOLE INTERFACE 
CREATED BY SURAJSHUKLA''')

    print()

# to kill connection and cursor object
def connection_close():
    cursor.close()
    connection.close()

#to execute the command instantly
def commit():
    connection.commit()

# to highlight data
def color(col=7):

    if col!=None:
        pass
    else:
        col=random.randint(2,6)

    color=f'\033[1;3{col}m'

    return color

# to highlight data
def separator(num,symbol="*"):
    return symbol*num


#function to add users to allow the access of database
def add_new_user(username,userpassword,userid=None):

    try:

        val=(userid,username,userpassword)
        cursor.execute('INSERT INTO USERS VALUES(%s,%s,%s)',val)
        commit()
        
        print(f'\nSuccessfully Added! New  USER-{color(6)}{username}{color()}\n')
    except:

        print('\nError! Unable to add new user\n')
    

#show registered users 
def show_users():
    try :
        cursor.execute("SELECT USERID,USERNAME FROM USERS")
    
        users=cursor.fetchall()
        
        print(f'\n{separator(51)} THERE ARE {color(6)}{len(users)}{color()} ARE AUTHORISHED USERS {separator(51)}')
            
        for user in users:

            print()

            print(f'''{color(6)}USERID {color()}:{user['USERID']},
{color(6)}USERNAME {color()}:{user['USERNAME']}''')

            print()
        print(separator(137),'\n')
            
    except:

        print('\nOOPs! Something went wrong\n')


# to remove registered users
def remove_user(username):

    try :

        val=(username,)
        cursor.execute('DELETE FROM USERS WHERE USERNAME=%s',val)
        commit()
        
        print(f'\nsuccessfully deleted! USERNAME - {color(6)}{username}{color()}\n')

    except:

        print(f'\n{color(6)}{username}{color()}! THIS USER DOES NOT EXIST\n')


# to add a new book with details
def add_book(bookname,costprice,listprice,stocks,author,publishdate,category,language,discount=0,others=None,bookid=None) :
    
    try:

        book_details=(bookid,bookname,costprice,listprice,stocks,author,publishdate,discount,category,language,others)

        query='INSERT INTO BOOKS VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

        cursor.execute(query,book_details)

        print(f'successfully added!BOOKNAME-{color(6)}{bookname}{color()}')
    

    except:

        print('\nOOPS! Something went wrong\n')
        

# to enter details about new purchase
def new_purchase(customeremailid,customername,productid,amount,purchaseid=None,purchasedate=None):

    try:
        pdtID=(productid,)
        cursor.execute('SELECT BOOKID FROM BOOKS WHERE BOOKID=%s',pdtID)
        
        _productid_=cursor.fetchone()

        if _productid_!=None:

            customerinfo=(customeremailid,customername,purchaseid,productid,amount)

            query='INSERT INTO CUSTOMERS VALUES(%s,%s,%s,now(),%s,%s)'

            cursor.execute(query,customerinfo)

            connection.commit()

            print(f'Successfully Added! CUSTOMERNAME-{customername}')

        else:
            
            print('ERROR! Unmatched product ID')
            
    except:
        print('OOPs! something went wrong')
        

# searching books
def show_books(bookname=None,bookid=None,category=None,author=None):

    try:

        via=(bookname,bookid,category,author)
        query='SELECT * FROM BOOKS WHERE BOOKNAME=%s or BOOKID=%s or CATEGORY=%s or AUTHOR=%s'
        cursor.execute(query,via)

        bookdetails=cursor.fetchall()

        if len(bookdetails)!=0:
              
            print(f'\n{separator(51)} THERE ARE {color(6)}{len(bookdetails)}{color()} ARE BOOKS AVAILABLE  {separator(51)}')

            for book in bookdetails:

                print()

                print(f'''{color(6)}BOOKID{color()}:{book["BOOKID"]},
{color(6)}BOOKNAME{color()}:{book["BOOKNAME"]},
{color(6)}COSTPRICE{color()}:{book["COSTPRICE"]},
{color(6)}LISTPRICE{color()}:{book["LISTPRICE"]},
{color(6)}STOCKS{color()}:{book["STOCKS"]},
{color(6)}AUTHOR{color()}:{book["AUTHOR"]},
{color(6)}PUBLISHDATE{color()}:{book["PUBLISHEDDATE"]},
{color(6)}DISCOUNT{color()}:{book["DISCOUNT"]},
{color(6)}CATEGORY{color()}:{book["CATEGORY"]},
{color(6)}LANGUAGE{color()}:{book["LANGUAGE"]},
{color(6)}OTHERS{color()}:{book["OTHERS"]}''')

                print()

            print(separator(137))

        else:
            
            print('\nResult Not Found!\n')
               

    except:

        print('OOPS! something went wrong')



# To show customers details
def show_customers(customeremailid=None,customername=None,purchaseid=None,purchasedate=None,productid=None):

    try:
        via=(customeremailid,customername,purchaseid,productid,purchasedate)
        query='SELECT * FROM CUSTOMERS WHERE CUSTOMEREMAILID=%s OR CUSTOMERNAME=%s OR PURCHASEID=%s OR PURCHASEDATE=%s  OR PRODUCTID=%s'

        cursor.execute(query,via)

        customers_details=cursor.fetchall()

        if customers_details!=None:

            print(f'\n{separator(51)} THERE ARE {color(6)}{len(customers_details)}{color()} ARE AUTHORISHED USERS {separator(51)}')

            for customer in customers_details:

                print()

                print(f'''{color(6)}CUSTOMEREMAILID{color()}:{customer['CUSTOMEREMAILID']},
{color(6)}CUSTOMERNAME{color()}:{customer['CUSTOMERNAME']},
{color(6)}PURCHASEID{color()}:{customer['PURCHASEID']},
{color(6)}PURCHASEDATE{color()}:{customer['PURCHASEDATE']},
{color(6)}PRODUCTID{color()}:{customer['PRODUCTID']},
{color(6)}AMOUNTPAID{color()}:{customer['AMOUNTPAID']},
{color(6)}DISCOUNT{color()}:{customer['DISCOUNT']},''')

                print()

        else:

            print('Result Not Found!')
    
    except:

        ('OOPs! something went wrong')


# To update stocks 
def update_stocks(stocks,bookname=None,bookid=None,category=None,author=None):
    
    try:

        show_books(bookname=bookname,bookid=bookid)

        via=(stocks,bookname,bookid,category,author)

        query='UPDATE BOOKS SET STOCKS=%s WHERE BOOKNAME=%s or BOOKID=%s or CATEGORY=%s or AUTHOR=%s'

        cursor.execute(query,via)

        print('Updated successfully!')

        show_books(bookname=bookname,bookid=bookid)

    except:

        print('OOPS! something went wrong')
    
   
# To remove book
def remove_book(bookname=None,bookid=None,category=None,author=None):

    try:
    
        via=(bookname,bookid,category,author)

        query='DELETE  FROM BOOKS WHERE BOOKNAME=%s or BOOKID=%s or CATEGORY=%s or AUTHOR=%s'

        cursor.execute(query,via)

        connection.commit()

        print('Removed successfully')

    except:

        print('OOPs! something went wrong')    


# To remove customer
def remove_customer(customername):
    
    try:
        via=(customername,)
        query='DELETE  FROM CUSTOMERS WHERE CUSTOMERNAME=%s'
        cursor.execute(query,via)
        connection.commit()

        print('Removed successfully')
    
    except:
        
        print('OOPs! Something went wrong')


#driver's code
if __name__=="__main__":
#    show_book(bookname="cingage")
#    show_customer(purchaseid=4)
    show_users()
    new_purchase('surajshukla2703@gmail.com','surajshukla',3,480)
    