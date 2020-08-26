mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123'
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123'
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY FIRST")
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT name, address FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone()

print(myresult)
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address ='Park Lane 38' "

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address LIKE '%way%' "

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name DESC"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

sql = "DROP TABLE customers"

mycursor.execute(sql)
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE customers MODIFY id INT auto_increment FIRST")

mycursor.execute("DESCRIBE customers")

for x in mycursor:
    print(x)
Roll no. 12520
(ii)	Write SQL commands for the following statements: 
-To display the names of all the white coloured vehicles.
- To display name of vehicle name and capacity of vehicles in ascending order of their sitting capacity.
- To display the highest charges at which a vehicle can be hired from CABHUB.
- To display the customer name and the corresponding name of the vehicle hired by them.
(c)Give the output of the following SQL queries : 
(i) SELECT COUNT(DISTINCT Make) FROM CABHUB;
(ii) SELECT MAX(Charges), MIN(Charges)
FROM CABHUB;
sql = "USE products_db"
mycursor.execute (sql)

sql = "CREATE TABLE users (id INT UNSIGNED auto_increment PRIMARY KEY,\
     name VARCHAR(30), \
         fav INT UNSIGNED)"
mycursor.execute (sql)

sql = "CREATE TABLE products (id INT UNSIGNED PRIMARY KEY,\
     name VARCHAR(30) NOT NULL)"

mycursor.execute (sql)

sql = "SHOW TABLES"
mycursor.execute (sql)

for x in mycursor:
    print(x)
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'products_db'
)

mycursor = mydb.cursor()

sql = "INSERT INTO users (name, fav) VALUES (%s, %s)"
val = [
    ('John', 154),
    ('Peter', 154),
    ('Amy', 155),
    ('Hannah', 0),
    ('Michael', 0)
]

mycursor.executemany(sql, val)

mydb.commit()

sql = "INSERT INTO products (id, name) VALUES (%s, %s)"
val = [
    (154, 'Chocolate Heaven'),
     (155,  'Tasty Lemon'),
     (156, 'Vanilla Dreams')
]

mycursor.executemany(sql, val)

mydb.commit()

sql = "SELECT * FROM users"
mycursor.execute(sql)

myresult = mycursor.fetchall()
for x in myresult:
    print(x)

sql = "SELECT * FROM products"
mycursor.execute(sql)

myresult = mycursor.fetchall()
for x in myresult:
    print(x)
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'products_db'
)

mycursor = mydb.cursor()

sql = "SELECT \
    users.name AS user,   products.name AS favorite \
    FROM users, products \
    WHERE users.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x) 

print("\n\n")

sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'products_db'
)

mycursor = mydb.cursor()

sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  LEFT JOIN products ON users.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'products_db'
)

mycursor = mydb.cursor()

sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  RIGHT JOIN products ON users.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'products_db'
)

mycursor = mydb.cursor()

sql = "SELECT * FROM users \
       CROSS JOIN products"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Electronics',
                                         user='user1',
                                         password='user123')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database()")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
(b) To display product name and price of all those products, whose price is in the range of 10000 and 15000 (both values inclusive).
(c) To display the number of products, which are supplied by each suplier. i.e., the expected output should be; 
	S01   2
	S02   2
	S03   1
(d) To display the price, product name and quantity (i.e., qty) of those products which have quantity more thhn 100.
(e) To display the names of those suppliers, who are either from DELHI or from CHENNAI.
(f) To display the name of the companies and the name of the products in descending order of company names.
	 Obtain the outputs of the following SQL queries based on the data given in tables PRODUCTS and SUPPLIERS above. 
g1) SELECT DISTINCT SUPCODE FROM PRODUCTS;
g2) SELEC MAX (PRICE), MIN (PRICE) FROM PRODUCTS;
g3) SELECT PRICE*QTY
FROM PRODUCTS WHERE PID = 104; (g4)
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Electronics',
                                         user='user1',
                                         password='user123')

    mySql_Create_Table_Query = """CREATE TABLE Laptop ( 
                             Id int(11) NOT NULL,
                             Name varchar(250) NOT NULL,
                             Price float NOT NULL,
                             Purchase_date Date NOT NULL,
                             PRIMARY KEY (Id)) """

    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("Laptop Table created successfully ")

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='electronics',
                                         user='user1',
                                         password='user123')
    mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date) 
                           VALUES 
                           (10, 'Lenovo ThinkPad P71', 30459, '2019-08-14') """

    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Laptop table")
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into Laptop table {}".format(error))

finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")

import mysql.connector
from mysql.connector import Error

def insertVariblesIntoTable(id, name, price, purchase_date):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='Electronics',
                                             user='user1',
                                             password='user123')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date) 
                                VALUES (%s, %s, %s, %s) """

        recordTuple = (id, name, price, purchase_date)
        cursor.execute(mySql_insert_query, recordTuple)
        connection.commit()
        print("Record inserted successfully into Laptop table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

insertVariblesIntoTable(2, 'Area 51M', 60999, '2019-04-14')
insertVariblesIntoTable(3, 'MacBook Pro', 200499, '2019-06-20')
+--------------------+
| Database           |
+--------------------+
| information_schema |
| electronics        |
| hospital_db        |
| mydatabase         |
| mysql              |
| performance_schema |
| products_db        |
| southwind          |
| sys                |
+--------------------+

import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Electronics',
                                         user='user1',
                                         password='user123')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database()")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Electronics',
                                         user='user1',
                                         password='user123')

    mySql_Create_Table_Query = """CREATE TABLE Laptop ( 
                             Id int(11) NOT NULL,
                             Name varchar(250) NOT NULL,
                             Price float NOT NULL,
                             Purchase_date Date NOT NULL,
                             PRIMARY KEY (Id)) """

    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("Laptop Table created successfully ")

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='electronics',
                                         user='user1',
                                         password='user123')
    mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date) 
                           VALUES 
                           (10, 'Lenovo ThinkPad P71', 30459, '2019-08-14') """

    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Laptop table")
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into Laptop table {}".format(error))

finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")

import mysql.connector
from mysql.connector import Error

def insertVariblesIntoTable(id, name, price, purchase_date):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='Electronics',
                                             user='user1',
                                             password='user123')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date) 
                                VALUES (%s, %s, %s, %s) """

        recordTuple = (id, name, price, purchase_date)
        cursor.execute(mySql_insert_query, recordTuple)
        connection.commit()
        print("Record inserted successfully into Laptop table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

insertVariblesIntoTable(2, 'Area 51M', 60999, '2019-04-14')
insertVariblesIntoTable(3, 'MacBook Pro', 200499, '2019-06-20')
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='electronics',
                                         user='user1',
                                         password='user123')

    mySql_select_Query = "select * from laptop"
    cursor = connection.cursor(buffered=True)
    cursor.execute(mySql_select_Query)
    record = cursor.fetchone()
    
    print("Id = ", record[0] )
    print("Name = ", record[1])
    print("Price = ", record[2])
    print("Purchase_date  = ", record[3], "\n")
    

except mysql.connector.Error as error:
    print("Error while connecting to MySQL", error)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
#  instead of a column id

import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Electronics',
                                         user='user1',
                                         password='user123')
    sql_select_Query = "select * from Laptop"
    # MySQLCursorDict creates a cursor that returns rows as dictionaries
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    
    print("Fetching each row using column name")

    for row in records:
        id = row["Id"]
        name = row["Name"]
        price = row["Price"]
        purchase_date = row["Purchase_date"]
        print(id, name, price, purchase_date)

except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='electronics',
                                         user='user1',
                                         password='user123')

    sql_Query = "select price from laptop where id = %s"
    id = (1,)

    cursor = connection.cursor()
    cursor.execute(sql_Query, id)
    record = cursor.fetchone()

    # selecting column value into varible
    price = float(record[0])
    print("Laptop price is : ", price)

except mysql.connector.Error as error:
    print("Failed to get record from database: {}".format(error))

finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='electronics',
                                         user='user1',
                                         password='user123')
    cursor = connection.cursor()

    print("Before updating a record ")
    sql_select_query = """select * from Laptop where id = 6"""
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)

    # Update single record now
    sql_update_query = """Update Laptop set Price = 101499 where id = 6"""
    cursor.execute(sql_update_query)
    connection.commit()
    print("Record Updated successfully ")

    print("After updating record ")
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)

except mysql.connector.Error as error:
    print("Failed to update table record: {}".format(error))
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
import mysql.connector
from mysql.connector import Error

def updateLaptopPrice(id, price):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='electronics',
                                             user='user1',
                                             password='user123')

        cursor = connection.cursor()
        sql_update_query = """Update laptop set price = %s where id = %s"""
        inputData = (price, id)
        cursor.execute(sql_update_query, inputData)
        connection.commit()
        print("Record Updated successfully ")

    except mysql.connector.Error as error:
        print("Failed to update record to database: {}".format(error))
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

updateLaptopPrice(4, 45000)
updateLaptopPrice(5, 145000)
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='electronics',
                                         user='user1',
                                         password='user123')

    cursor = connection.cursor()
    sql_update_query = """Update Laptop set Price = %s where id = %s"""

    # multiple records to be updated in tuple format
    records_to_update = [(30000, 3), (28750, 4)]
    cursor.executemany(sql_update_query, records_to_update)
    connection.commit()

    print(cursor.rowcount, "Records of a laptop table updated successfully")

except mysql.connector.Error as error:
    print("Failed to update records to database: {}".format(error))
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='electronics',
                                         user='user1',
                                         password='user123')

    cursor = connection.cursor()
    sql_update_query = """Update Laptop set Name = %s, Price = %s where id = %s"""

    name = "HP Pavilion"
    price = 28200
    id = 4
    input = (name, price, id)

    cursor.execute(sql_update_query, input)
    connection.commit()
    print("Multiple column updated successfully ")

except mysql.connector.Error as error:
    print("Failed to update record to database: {}".format(error))

finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

import mysql.connector
from mysql.connector import Error
from datetime import datetime

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='electronics',
                                         user='user1',
                                         password='user123')

    cursor = connection.cursor()
    sql_update_query = """Update Laptop set Purchase_date = %s where id = %s"""

    current_Date = datetime.now()
    formatted_date = current_Date.strftime('%Y-%m-%d')
    id = 2
    input = (formatted_date, id)
    cursor.execute(sql_update_query, input)
    connection.commit()
    print("Purchased Date Updated successfully ")

except mysql.connector.Error as error:
    print("Failed to update purchased date {}".format(error))

finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("connection is closed")
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='electronics',
                                         user='user1',
                                         password='user123')
    cursor = connection.cursor()
    print("Displaying laptop record Before Deleting it")

    
    sql_select_query = """select * from Laptop where id = 7"""
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)

    sql_Delete_query = """Delete from Laptop where id = 7"""
    cursor.execute(sql_Delete_query)
    connection.commit()

    cursor.execute(sql_select_query)
    records = cursor.fetchall()
    
    if len(records) == 0:
        print("\nRecord Deleted successfully ")

except mysql.connector.Error as error:
    print("Failed to delete record from table: {}".format(error))
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
#  to delete a row from MySQL table
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='electronics',
                                         user='user1',
                                         password='user123')
    cursor = connection.cursor()
    sql_Delete_query = """Delete from Laptop where id = %s"""
    laptopId = 6
    cursor.execute(sql_Delete_query, (laptopId,))
    connection.commit()
    print("Record Deleted successfully ")

except mysql.connector.Error as error:
    print("Failed to Delete record from table: {}".format(error))
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(host='localhost',
                                   database='electronics',
                                   user='user1',
                                   password='user123')

    cursor = connection.cursor()
    sql_Delete_query = """Delete from Laptop where id = %s"""
    records_to_delete = [(5,), (4,)]
    cursor.executemany(sql_Delete_query, records_to_delete)
    connection.commit()
    print(cursor.rowcount, " Record Deleted successfully")

except mysql.connector.Error as error:
    print("Failed to Delete records from MySQL table: {}".format(error))
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='electronics',
                                         user='user1',
                                         password='user123')
    cursor = connection.cursor()
    Delete_all_rows = """truncate table Laptop """
    cursor.execute(Delete_all_rows)
    connection.commit()
    print("All Record Deleted successfully ")

except mysql.connector.Error as error:
    print("Failed to Delete all records from database table: {}".format(error))
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='electronics',
                                         user='user1',
                                         password='user123')
    cursor = connection.cursor()
    alter_column = """ALTER TABLE Laptop DROP COLUMN Purchase_date"""
    cursor.execute(alter_column)
    connection.commit()
    print("Column Deleted successfully ")

except mysql.connector.Error as error:
    print("Failed to Delete column: {}".format(error))
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
                        THE MAIN FUNCTION OF PROGRAM
***********************************************"""

Welcome()

while True:
print (3*"\n",100*"=")
print ("""MAIN MENU

    1. New Account
    2. Deposit Amount
    3. Withdraw Amount
    4. Balance Enquiry
    5. All Account Holder List
    6. Close An Account
    7. Modify An Account
    8. Exit
    """)

try:
ch=input("Enter Your Choice(1~8): ")
if ch==1:
write_account()

elif ch==2:
num=input("\n\nEnter Account Number: ")
deposit_withdraw(num,1)


elifch==3:
num=input("\n\nEnter Account Number: ")
deposit_withdraw(num,2)

elif ch==4:
num=input("\n\nEnter Account Number: ")
display_sp(num)

elif ch==5:
display_all()

elif ch==6:
num=input("\n\nEnter Account Number: ")
delete_account(num)

elif ch==7:
num=input("\n\nEnter Account Number: ")
modify_account(num)

elif ch==8:
break

else:
print ("Input correcr choice...(1-8))"

except NameError:
print ("Input correct choice...(1-8))"


input("\n\n\n\n\nTHANK YOU\n\nPress any key to exit...")
