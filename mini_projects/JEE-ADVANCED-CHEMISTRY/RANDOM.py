import mysql.connector

connection=mysql.connector.connect(
    host='localhost',
    password='shukla',
    user='surajshukla7656',
    database='JEE_ADVANCED_CHEMISTRY'
)

if connection.is_connected():
    print('connected successfully')

else: 
    print('not connected')
    

cursor=connection.cursor()

cursor.execute('SHOW TABLES')

list1=cursor.fetchall()

# try : 
#     i=0

#     while True:

#         print(list1[i])

#         if i!=0 and i!=11 and i!=20:

#             query=f'ALTER TABLE {list1[i][0]}'+' ADD IMPORTANT VARCHAR(5)'

#             cursor.execute(query)

#             print('done')

#         else: 

#             print('passed')
#         i+=1
# except Exception as e : 

#     print('Error- x{}'.format(e))


for i in list1:

    cursor.execute(f'describe {i[0]}')

    print('\n\n')