import mysql.connector
connection=mysql.connector.connect(
        user='surajshukla7656',
        host="localhost",
        database="online_book_store",
        password="shukla"
    )
print('connection established successfully!')
cursor=connection.cursor(dictionary=True)

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



def show_books(bookname=None,bookid=None,category=None,author=None):


    via=(bookname,bookid,category,author)
    query='SELECT * FROM BOOKS WHERE BOOKNAME=%s or BOOKID=%s or CATEGORY=%s or AUTHOR=%s'
    cursor.execute(query,via)

    bookdetails=cursor.fetchall()

    if bookdetails!=None:
            
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

    else:
        
        print('Result Not Found!')



               
def new_purchase(customeremailid,customername,productid,amount,purchasedate=None,purchaseid=None):

    
    pdtID=(productid,)
    cursor.execute('SELECT BOOKID FROM BOOKS WHERE BOOKID=%s',pdtID)
    
    _productid_=cursor.fetchone()
    print(_productid_)

    if _productid_!=None:

        print("ih")
        customerinfo=(customeremailid,customername,purchaseid,productid,amount)

        query='INSERT INTO CUSTOMERS VALUES(%s,%s,%s,now(),%s,%s)'

        cursor.execute(query,customerinfo)

        connection.commit()

        print(f'Successfully Added! CUSTOMERNAME-{customername}')

    else:
        
        print('ERROR! Unmatched product ID')
        
    
        
new_purchase('surajshukla2703@gmail.com','surajshukla',3,480)