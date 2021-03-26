# python program to create  a table using mysql

import mysql.connector

connection=mysql.connector.connect(
    user='surajshukla7656',
    host='localhost',
    password='shukla',
    database='practice_db'
)

cursor=connection.cursor()

query='''create table if not exists Employee(
    Emp_ID int not null primary key,
    Emp_name varchar(20) not null,
    Gross_salary decimal(10,2)                                                                                                        )'''

cursor.execute(query)
connection.commit()

query='insert into Employee values(%s,%s,%s)'
data=(1001,'Ram Mohan',67000)

cursor.execute(query,data)
connection.commit()

data=(1001,'Ram Mohan',67000)

cursor.execute(query,data)
connection.commit()
