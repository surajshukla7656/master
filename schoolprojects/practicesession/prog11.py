# python program to create a table through python interface

import mysql.connector

# making the connection
conn=mysql.connector.connect(
        host='localhost',
        user='surajshukla7656',
        password='shukla',
        database='practice_db'
        )


cursor=conn.cursor()

query='''create table if not exists demotableprog11(
rollnumber int not null  auto_increment,
name varchar(30) not null ,
noofsubject int not null,
primary key(rollnumber))'''

cursor.execute(query)
conn.commit()
print('Table created')
cursor.close()
conn.close()
