#program to establish connection between mysql server and this module
import mysql.connector
import weakref
def connect():
    connection=mysql.connector.connect(
        user='surajshukla7656',
        host="localhost",
        database="book_shop",
        password="shukla"
    )
    cursor=connection.cursor()
    return weakref.ref(connect)


def creating_table():
    pseudo_cursor=connect()
    cursor=pseudo_cursor()
    print(cursor)
    cursor.execute("select database()")
    for i in cursor:
        print(i)

if __name__ == "__main__":
    print(creating_table())