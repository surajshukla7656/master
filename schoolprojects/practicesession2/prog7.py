# python program to display all the records stored in a 
# table stu_tbl using python and Mysql interface

import mysql.connector


Connection=mysql.connector.connect(
    user='surajshukla7656',
    host='localhost',
    password='shukla',
    database='stu_db'
)

cursor=Connection.cursor()

cursor.execute('select * from stu_tbl')

for record in cursor.fetchall():
    print(record)

