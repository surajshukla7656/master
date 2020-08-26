import mysql.connector

def connect():
    connection=mysql.connector.connect(
        user='surajshukla7656',
        host="localhost",
        database="book_shop",
        password="shukla"
    )
    return connection

connect()
if __name__ == "__main__":
    print(connect())