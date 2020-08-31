import mysql.connector
connection=mysql.connector.connect(
        user='surajshukla7656',
        host="localhost",
        database="book_shop",
        password="shukla"
    )
print('connection established successfully!')
cursor=connection.cursor(dictionary=True)
    
category=("laptop",)
sql="drop table %s"
cursor.execute(sql,category)
