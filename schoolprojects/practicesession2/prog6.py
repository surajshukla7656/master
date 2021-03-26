# python program to insert the following records
# in a table stu_tbl using python and mysql interface

import mysql.connector

connection=mysql.connector.connect(
    user='surajshukla7656',
    password='shukla',
    host='localhost',
    database='stu_db'
)

cursor=connection.cursor()

query='''create table if not exists stu_tbl(
    roll_no int not null primary key,
    name varchar(20) not null,
    perc_marks decimal(5,2)
)'''


cursor.execute(query)
connection.commit()

query='insert into stu_tbl values(%s,%s,%s)'


data=(1,'Ramesh Kumar',98.75)
cursor.execute(query,data)
connection.commit()


data=(2,'Mohan Prakash',78.50)
cursor.execute(query,data)
connection.commit()