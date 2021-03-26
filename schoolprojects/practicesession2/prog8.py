# python program to search a record stored in a table
# stu_tbl in stu_db using python and Mysql interface

import mysql.connector

connection=mysql.connector.connect(
    user='surajshukla7656',
    password='shukla',
    host='localhost',
    database='stu_db'
)

cursor=connection.cursor()

cursor.execute('select * from stu_tbl')

roll_number=int(input('Enter roll number to search :'))
found=False
for record in cursor.fetchall():
    if record[0]==roll_number:
        print('record found')
        print('name of student :',record[1],'percentage marks :',record[2])
        found=True
        break

if found==False:
    print('record not found')