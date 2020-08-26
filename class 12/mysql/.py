[4:13 PM, 8/14/2020] Vinod Sir: mysql> create database hospital_db;
Query OK, 1 row affected (0.08 sec)

mysql> use hospital_db;
Database changed
mysql>
mysql>
mysql> CREATE TABLE patients (
    ->           patientID      INT UNSIGNED  NOT NULL AUTO_INCREMENT,
    ->           name           VARCHAR(30)   NOT NULL DEFAULT '',
    ->           dateOfBirth    DATE          NOT NULL,
    ->           lastVisitDate  DATE          NOT NULL,
    ->           nextVisitDate  DATE          NULL,
    ->           PRIMARY KEY (patientID)
    ->        );
Query OK, 0 rows affected (0.70 sec)

mysql> show tables;
+-----------------------+
| Tables_in_hospital_db |
+-----------------------+
| patients              |
+-----------------------+
1 row in set (0.14 sec)

mysql> describe patients;
+---------------+------------------+------+-----+---------+----------------+
| Field         | Type             | Null | Key | Default | Extra          |
+---------------+------------------+------+-----+---------+----------------+
| patientID     | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| name          | varchar(30)      | NO   |     |         |                |
| dateOfBirth   | date             | NO   |     | NULL    |                |
| lastVisitDate | date             | NO   |     | NULL    |                |
| nextVisitDate | date             | YES  |     | NULL    |                |
+---------------+------------------+------+-----+---------+----------------+
5 rows in set (0.07 sec)

mysql> INSERT INTO patients VALUES
    ->           (1001, 'Ah Teck', '1991-12-31', '2012-01-20', NULL),
    ->           (NULL, 'Kumar', '2011-10-29', '2012-09-20', NULL),
    ->           (NULL, 'Ali', '2011-01-30', CURDATE(), NULL);
Query OK, 3 rows affected (0.13 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> select * from patients;
+-----------+---------+-------------+---------------+---------------+
| patientID | name    | dateOfBirth | lastVisitDate | nextVisitDate |
+-----------+---------+-------------+---------------+---------------+
|      1001 | Ah Teck | 1991-12-31  | 2012-01-20    | NULL          |
|      1002 | Kumar   | 2011-10-29  | 2012-09-20    | NULL          |
|      1003 | Ali     | 2011-01-30  | 2020-08-14    | NULL          |
+-----------+---------+-------------+---------------+---------------+
3 rows in set (0.00 sec)

mysql> SELECT * FROM patients
    ->        WHERE lastVisitDate BETWEEN '2012-09-15' AND CURDATE()
    ->        ORDER BY lastVisitDate;
+-----------+-------+-------------+---------------+---------------+
| patientID | name  | dateOfBirth | lastVisitDate | nextVisitDate |
+-----------+-------+-------------+---------------+---------------+
|      1002 | Kumar | 2011-10-29  | 2012-09-20    | NULL          |
|      1003 | Ali   | 2011-01-30  | 2020-08-14    | NULL          |
+-----------+-------+-------------+---------------+---------------+
2 rows in set (0.07 sec)

mysql> SELECT * FROM patients
    ->        WHERE YEAR(dateOfBirth) = 2011
    ->        ORDER BY MONTH(dateOfBirth), DAY(dateOfBirth)
    -> ;
+-----------+-------+-------------+---------------+---------------+
| patientID | name  | dateOfBirth | lastVisitDate | nextVisitDate |
+-----------+-------+-------------+---------------+---------------+
|      1003 | Ali   | 2011-01-30  | 2020-08-14    | NULL          |
|      1002 | Kumar | 2011-10-29  | 2012-09-20    | NULL          |
+-----------+-------+-------------+---------------+---------------+
2 rows in set (0.06 sec)

mysql> SELECT * FROM patients
    ->        WHERE MONTH(dateOfBirth) = MONTH(CURDATE())
    ->           AND DAY(dateOfBirth) = DAY(CURDATE());
Empty set (0.00 sec)

mysql> SELECT * FROM patients
    ->        WHERE MONTH(dateOfBirth) = 1;
+-----------+------+-------------+---------------+---------------+
| patientID | name | dateOfBirth | lastVisitDate | nextVisitDate |
+-----------+------+-------------+---------------+---------------+
|      1003 | Ali  | 2011-01-30  | 2020-08-14    | NULL          |
+-----------+------+-------------+---------------+---------------+
1 row in set (0.00 sec)

mysql> SELECT name, dateOfBirth, TIMESTAMPDIFF(YEAR, dateOfBirth, CURDATE()) AS age
    ->        FROM patients
    ->        ORDER BY age, dateOfBirth;
+---------+-------------+------+
| name    | dateOfBirth | age  |
+---------+-------------+------+
| Kumar   | 2011-10-29  |    8 |
| Ali     | 2011-01-30  |    9 |
| Ah Teck | 1991-12-31  |   28 |
+---------+-------------+------+
3 rows in set (0.04 sec)

mysql> SELECT name, lastVisitDate FROM patients
    ->        WHERE TIMESTAMPDIFF(DAY, lastVisitDate, CURDATE()) > 60;
+---------+---------------+
| name    | lastVisitDate |
+---------+---------------+
| Ah Teck | 2012-01-20    |
| Kumar   | 2012-09-20    |
+---------+---------------+
2 rows in set (0.00 sec)

mysql> SELECT name, lastVisitDate FROM patients
    ->        WHERE TO_DAYS(CURDATE()) - TO_DAYS(lastVisitDate) > 60;
+---------+---------------+
| name    | lastVisitDate |
+---------+---------------+
| Ah Teck | 2012-01-20    |
| Kumar   | 2012-09-20    |
+---------+---------------+
2 rows in set (0.05 sec)

mysql> SELECT * FROM patients
    ->        WHERE dateOfBirth > DATE_SUB(CURDATE(), INTERVAL 18 YEAR);
+-----------+-------+-------------+---------------+---------------+
| patientID | name  | dateOfBirth | lastVisitDate | nextVisitDate |
+-----------+-------+-------------+---------------+---------------+
|      1002 | Kumar | 2011-10-29  | 2012-09-20    | NULL          |
|      1003 | Ali   | 2011-01-30  | 2020-08-14    | NULL          |
+-----------+-------+-------------+---------------+---------------+
2 rows in set (0.03 sec)

mysql> UPDATE patients
    ->        SET nextVisitDate = DATE_ADD(CURDATE(), INTERVAL 6 MONTH)
    ->        WHERE name = 'Ali';
Query OK, 1 row affected (0.07 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> SELECT * FROM patients;
+-----------+---------+-------------+---------------+---------------+
| patientID | name    | dateOfBirth | lastVisitDate | nextVisitDate |
+-----------+---------+-------------+---------------+---------------+
|      1001 | Ah Teck | 1991-12-31  | 2012-01-20    | NULL          |
|      1002 | Kumar   | 2011-10-29  | 2012-09-20    | NULL          |
|      1003 | Ali     | 2011-01-30  | 2020-08-14    | 2021-02-14    |
+-----------+---------+-------------+---------------+---------------+
3 rows in set (0.00 sec)

mysql> select now(), curdate(), curtime();
+---------------------+------------+-----------+
| now()               | curdate()  | curtime() |
+---------------------+------------+-----------+
| 2020-08-14 16:12:50 | 2020-08-14 | 16:12:50  |
+---------------------+------------+-----------+
1 row in set (0.00 sec)

mysql>
[4:16 PM, 8/14/2020] Vinod Sir: mysql> SELECT DATEDIFF('2012-02-01', '2012-01-28');
+--------------------------------------+
| DATEDIFF('2012-02-01', '2012-01-28') |
+--------------------------------------+
|                                    4 |
+--------------------------------------+
1 row in set (0.00 sec)

mysql> SELECT DATEDIFF('2012-02-01', '2011-01-28');
+--------------------------------------+
| DATEDIFF('2012-02-01', '2011-01-28') |
+--------------------------------------+
|                                  369 |
+--------------------------------------+
1 row in set (0.00 sec)

mysql> SELECT TIMESTAMPDIFF(DAY, '2012-02-01', '2012-01-28');
+------------------------------------------------+
| TIMESTAMPDIFF(DAY, '2012-02-01', '2012-01-28') |
+------------------------------------------------+
|                                             -4 |
+------------------------------------------------+
1 row in set (0.00 sec)

mysql>[5:20 PM, 8/18/2020] Vinod Sir: Installing mysql python connector:
[5:21 PM, 8/18/2020] Vinod Sir: python -m pip install mysql-connector-python
[5:21 PM, 8/18/2020] Vinod Sir: # test.py
import mysql.connector
[5:21 PM, 8/18/2020] Vinod Sir: # mysql_connection1.py
import mysql.connector


mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123'
)

print(mydb)
[5:22 PM, 8/18/2020] Vinod Sir: # mysql_connection2.py
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123'
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
[5:22 PM, 8/18/2020] Vinod Sir: # mysql_connection3.py
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
[5:22 PM, 8/18/2020] Vinod Sir: # mysql_connection4.py
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)
[5:22 PM, 8/18/2020] Vinod Sir: # mysql_connection5.py
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
[5:23 PM, 8/18/2020] Vinod Sir: # mysql_connection6.py
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
[5:23 PM, 8/18/2020] Vinod Sir: # mysql_connection7.py
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY FIRST")
[5:23 PM, 8/18/2020] Vinod Sir: # mysql_connection8.py
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
[5:23 PM, 8/18/2020] Vinod Sir: # mysql_connection9.py
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
[5:24 PM, 8/18/2020] Vinod Sir: # mysql_connection10.py
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
[5:24 PM, 8/18/2020] Vinod Sir: # mysql_connection11.py
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
[5:25 PM, 8/18/2020] Vinod Sir: # mysql_connection13.py
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
[5:25 PM, 8/18/2020] Vinod Sir: # mysql_connection14.py
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
[5:25 PM, 8/18/2020] Vinod Sir: # mysql_connection15.py
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
[5:26 PM, 8/18/2020] Vinod Sir: # mysql_connection16.py
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
[5:27 PM, 8/18/2020] Vinod Sir: # mysql_connection18.py
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
[5:27 PM, 8/18/2020] Vinod Sir: # mysql_connection19.py
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
[5:27 PM, 8/18/2020] Vinod Sir: # mysql_connection20.py
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
[5:28 PM, 8/18/2020] Vinod Sir: # mysql_connection21.py
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
[5:29 PM, 8/18/2020] Vinod Sir: Note: After running this script we recreated the table customers and inserted the data in it.
[5:29 PM, 8/18/2020] Vinod Sir: # mysql_connection22.py
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
[5:29 PM, 8/18/2020] Vinod Sir: # mysql_connection23.py
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
[5:32 PM, 8/18/2020] Vinod Sir: Note: mysql_connection12.py is not required.
[5:32 PM, 8/18/2020] Vinod Sir: # mysql_connection12.py
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
    [5:20 PM, 8/18/2020] Vinod Sir: Installing mysql python connector:
[5:21 PM, 8/18/2020] Vinod Sir: python -m pip install mysql-connector-python
[5:21 PM, 8/18/2020] Vinod Sir: # test.py
import mysql.connector
[5:21 PM, 8/18/2020] Vinod Sir: # mysql_connection1.py
import mysql.connector


mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123'
)

print(mydb)
[5:22 PM, 8/18/2020] Vinod Sir: # mysql_connection2.py
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123'
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
[5:22 PM, 8/18/2020] Vinod Sir: # mysql_connection3.py
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
[5:22 PM, 8/18/2020] Vinod Sir: # mysql_connection4.py
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)
[5:22 PM, 8/18/2020] Vinod Sir: # mysql_connection5.py
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
[5:23 PM, 8/18/2020] Vinod Sir: # mysql_connection6.py
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
[5:23 PM, 8/18/2020] Vinod Sir: # mysql_connection7.py
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY FIRST")
[5:23 PM, 8/18/2020] Vinod Sir: # mysql_connection8.py
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
[5:23 PM, 8/18/2020] Vinod Sir: # mysql_connection9.py
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
[5:24 PM, 8/18/2020] Vinod Sir: # mysql_connection10.py
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
[5:24 PM, 8/18/2020] Vinod Sir: # mysql_connection11.py
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
[5:25 PM, 8/18/2020] Vinod Sir: # mysql_connection13.py
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
[5:25 PM, 8/18/2020] Vinod Sir: # mysql_connection14.py
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
[5:25 PM, 8/18/2020] Vinod Sir: # mysql_connection15.py
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
[5:26 PM, 8/18/2020] Vinod Sir: # mysql_connection16.py
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
[5:27 PM, 8/18/2020] Vinod Sir: # mysql_connection18.py
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
[5:27 PM, 8/18/2020] Vinod Sir: # mysql_connection19.py
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
[5:27 PM, 8/18/2020] Vinod Sir: # mysql_connection20.py
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
[5:28 PM, 8/18/2020] Vinod Sir: # mysql_connection21.py
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
[5:29 PM, 8/18/2020] Vinod Sir: Note: After running this script we recreated the table customers and inserted the data in it.
[5:29 PM, 8/18/2020] Vinod Sir: # mysql_connection22.py
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
[5:29 PM, 8/18/2020] Vinod Sir: # mysql_connection23.py
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
[5:32 PM, 8/18/2020] Vinod Sir: Note: mysql_connection12.py is not required.
[5:32 PM, 8/18/2020] Vinod Sir: # mysql_connection12.py
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

    print(x)print(x)


# Connecting to MySQL server

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
        connection.close()[11:49 AM, 8/20/2020] Vinod Sir:  Connecting to MySQL server

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
[11:49 AM, 8/20/2020] Vinod Sir: # Create table
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
[11:49 AM, 8/20/2020] Vinod Sir: #  insert a single row/record into MySQL table
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
[11:49 AM, 8/20/2020] Vinod Sir: # Using Python variables in a MySQL INSERT query

import mysql.connector
from mysql.connector import errorcode

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
[11:50 AM, 8/20/2020] Vinod Sir: mysql> show databases;
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
9 rows in set (0.00 sec)

mysql> use electonics;
ERROR 1049 (42000): Unknown database 'electonics'
mysql> use electronics;
Database changed
mysql> show tables;
+-----------------------+
| Tables_in_electronics |
+-----------------------+
| laptop                |
+-----------------------+
1 row in set (0.04 sec)

mysql> select * from laptop;
+----+---------------------+--------+---------------+
| Id | Name                | Price  | Purchase_date |
+----+---------------------+--------+---------------+
|  2 | Area 51M            |  60999 | 2019-04-14    |
|  3 | MacBook Pro         | 200499 | 2019-06-20    |
| 10 | Lenovo ThinkPad P71 |  30459 | 2019-08-14    |
+----+---------------------+--------+---------------+
3 rows in set (0.05 sec)

mysql>


