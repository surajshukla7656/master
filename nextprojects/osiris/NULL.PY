# to create a new categories of book
def create_category(category):
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
    
    if len(tables)<=1:
        print("Does not contain any category!")
    else:
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
def add_book(category,bookname,book_type,price,spec=None,id=None):
    try:
        sql=f"insert into {category}"+" values(%s,%s,%s,%s,%s)"
        print(sql)
        book_data=(id,bookname,book_type,price,spec)
        cursor.execute(sql,book_data)
        commit()
    except:
        print("something went wrong!")

# to display books of a category
def display_books(category):
    try :
        cursor.execute(f"select * from {category}")

        books_in_category=cursor.fetchall()
       

        if len(books_in_category)==0:

            print("Not available any book!")

        else:
            for book in books_in_category:
                print(f"""\n
bookID={book["bookID"]}
book={book["bookname"]}
booktype={book["book_type"]}
book price={book["price"]}
specifications={book["specifications"]}\n""")


    except:
        print(f"This '{category}' category may not exist!")

# display information about a particular category
def describe_category(category):
    cursor.execute(f"describe {category}")
    
    columns=cursor.fetchall()
    
    for column in columns:
        print(f"{column['Field']},\t\t{column['Type']},\t\t{column['Null']}")
