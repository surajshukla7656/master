
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+

mysql> create database southwind;
Query OK, 1 row affected (0.06 sec)

mysql> drop database southwind;
Query OK, 0 rows affected (0.43 sec)

mysql> create database if not exists southwind;
Query OK, 1 row affected (0.01 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| southwind          |
| sys                |
+--------------------+

mysql> drop database if exists southwind;
Query OK, 0 rows affected (0.00 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+

mysql> drop database southwind;
ERROR 1008 (HY000): Can't drop database 'southwind'; database doesn't exist
mysql> drop database if exists southwind;
Query OK, 0 rows affected, 1 warning (0.00 sec)

mysql> create database southwind;
Query OK, 1 row affected (0.01 sec)

mysql>
mysql>
mysql> show create database southwind;
+-----------+----------------------------------------------------------------------+
| Database  | Create Database                                                      |
+-----------+----------------------------------------------------------------------+
| southwind | CREATE DATABASE `southwind` /*!40100 DEFAULT CHARACTER SET latin1 */ |
+-----------+----------------------------------------------------------------------+

mysql>


mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| southwind          |
| sys                |
+--------------------+

mysql> use southwind;
Database changed
mysql> select database();
+------------+
| database() |
+------------+
| southwind  |
+------------+

mysql> use mysql;
Database changed
mysql> select database();
+------------+
| database() |
+------------+
| mysql      |
+------------+

mysql> use southwind;
Database changed
mysql> show tables;
Empty set (0.03 sec)

mysql> CREATE TABLE IF NOT EXISTS products (
    ->          productID    INT UNSIGNED  NOT NULL AUTO_INCREMENT,
    ->          productCode  CHAR(3)       NOT NULL DEFAULT '',
    ->          name         VARCHAR(30)   NOT NULL DEFAULT '',
    ->          quantity     INT UNSIGNED  NOT NULL DEFAULT 0,
    ->          price        DECIMAL(7,2)  NOT NULL DEFAULT 99999.99,
    ->          PRIMARY KEY  (productID)
    ->        );
Query OK, 0 rows affected (0.87 sec)

mysql> show tables;
+---------------------+
| Tables_in_southwind |
+---------------------+
| products            |
+---------------------+

mysql>
(a) R/2
(b) R/3
(c) 6 R
(d) 2 R
(a) 59.54 J/mol
(b) 5954 J/mol
(c) 595.4 J/mol
(d) 320.6 J/mol
(c) 2019 Microsoft Corporation. All rights reserved.

D:\WINDOWS\system32>cd \

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| southwind          |
| sys                |
+--------------------+

mysql> select database();
+------------+
| database() |
+------------+
| NULL       |
+------------+

mysql> use southwind;
Database changed
mysql> select database();
+------------+
| database() |
+------------+
| southwind  |
+------------+

mysql> show tables;
+---------------------+
| Tables_in_southwind |
+---------------------+
| products            |
+---------------------+

mysql> describe products;
+-------------+------------------+------+-----+----------+----------------+
| Field       | Type             | Null | Key | Default  | Extra          |
+-------------+------------------+------+-----+----------+----------------+
| productID   | int(10) unsigned | NO   | PRI | NULL     | auto_increment |
| productCode | char(3)          | NO   |     |          |                |
| name        | varchar(30)      | NO   |     |          |                |
| quantity    | int(10) unsigned | NO   |     | 0        |                |
| price       | decimal(7,2)     | NO   |     | 99999.99 |                |
+-------------+------------------+------+-----+----------+----------------+

mysql> select * from products;
Empty set (0.03 sec)

mysql> INSERT INTO products VALUES (1001, 'PEN', 'Pen Red', 5000, 1.23);
Query OK, 1 row affected (0.16 sec)

mysql> select * from products;
+-----------+-------------+---------+----------+-------+
| productID | productCode | name    | quantity | price |
+-----------+-------------+---------+----------+-------+
|      1001 | PEN         | Pen Red |     5000 |  1.23 |
+-----------+-------------+---------+----------+-------+

mysql> INSERT INTO products VALUES
    ->          (NULL, 'PEN', 'Pen Blue',  8000, 1.25),
    ->          (NULL, 'PEN', 'Pen Black', 2000, 1.25);
Query OK, 2 rows affected (0.06 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> select * from products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
+-----------+-------------+-----------+----------+-------+

mysql> INSERT INTO products (productCode, name, quantity, price) VALUES
    ->          ('PEC', 'Pencil 2B', 10000, 0.48),
    ->          ('PEC', 'Pencil 2H', 8000, 0.49);
Query OK, 2 rows affected (0.04 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> select * from products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> INSERT INTO products (productCode, name) VALUES ('PEC', 'Pencil HB');
Query OK, 1 row affected (0.03 sec)

mysql> select * from products;
+-----------+-------------+-----------+----------+----------+
| productID | productCode | name      | quantity | price    |
+-----------+-------------+-----------+----------+----------+
|      1001 | PEN         | Pen Red   |     5000 |     1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |     1.25 |
|      1003 | PEN         | Pen Black |     2000 |     1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |     0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |     0.49 |
|      1006 | PEC         | Pencil HB |        0 | 99999.99 |
+-----------+-------------+-----------+----------+----------+

mysql> INSERT INTO products values (NULL, NULL, NULL, NULL, NULL);
ERROR 1048 (23000): Column 'productCode' cannot be null
mysql>
(a) will decrease by 0.2 %
(b) will increase by 0.5 %
(c) will decrease by 0.05 %
(d) will increase by 0.2%

a)            3, 13

b)            4, 12

c)            6, 10

d)            8, 8

+-----------+-------------+-----------+----------+----------+

mysql> select productID, productCode from products;
+-----------+-------------+
| productID | productCode |
+-----------+-------------+
|      1001 | PEN         |
|      1002 | PEN         |
|      1003 | PEN         |
|      1004 | PEC         |
|      1005 | PEC         |
|      1006 | PEC         |
+-----------+-------------+

mysql> select * from products where productCode = 'pec';
+-----------+-------------+-----------+----------+----------+
| productID | productCode | name      | quantity | price    |
+-----------+-------------+-----------+----------+----------+
|      1004 | PEC         | Pencil 2B |    10000 |     0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |     0.49 |
|      1006 | PEC         | Pencil HB |        0 | 99999.99 |
+-----------+-------------+-----------+----------+----------+

mysql> select * from products where productCode = "pec";
+-----------+-------------+-----------+----------+----------+
| productID | productCode | name      | quantity | price    |
+-----------+-------------+-----------+----------+----------+
|      1004 | PEC         | Pencil 2B |    10000 |     0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |     0.49 |
|      1006 | PEC         | Pencil HB |        0 | 99999.99 |
+-----------+-------------+-----------+----------+----------+

mysql> show tables;
+---------------------+
| Tables_in_southwind |
+---------------------+
| products            |
+---------------------+

mysql> select * from Products where productCode = "pec";
+-----------+-------------+-----------+----------+----------+
| productID | productCode | name      | quantity | price    |
+-----------+-------------+-----------+----------+----------+
|      1004 | PEC         | Pencil 2B |    10000 |     0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |     0.49 |
|      1006 | PEC         | Pencil HB |        0 | 99999.99 |
+-----------+-------------+-----------+----------+----------+

mysql> select * from Products where productCode = "pec"  and price < 2.0;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> select * from Products where productCode = "pec"  and price < 2.0 and quantity > 8000;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
+-----------+-------------+-----------+----------+-------+

mysql> select productID, productCode, quantity
    -> from products
    -> where name like "Pencil%"  or quantity >= 8000;
+-----------+-------------+----------+
| productID | productCode | quantity |
+-----------+-------------+----------+
|      1002 | PEN         |     8000 |
|      1004 | PEC         |    10000 |
|      1005 | PEC         |     8000 |
|      1006 | PEC         |        0 |
+-----------+-------------+----------+

mysql> DELETE FROM products WHERE productID = 1006;
Query OK, 1 row affected (0.16 sec)

mysql> select * from Products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT name, price FROM products;
+-----------+-------+
| name      | price |
+-----------+-------+
| Pen Red   |  1.23 |
| Pen Blue  |  1.25 |
| Pen Black |  1.25 |
| Pencil 2B |  0.48 |
| Pencil 2H |  0.49 |
+-----------+-------+

mysql> select * from Products group by productCode;
ERROR 1055 (42000): Expression #1 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'southwind.Products.productID' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
mysql>
mysql>
mysql>
mysql> select productCode, max(quantity), min(quantity) from Products group by productCode;
+-------------+---------------+---------------+
| productCode | max(quantity) | min(quantity) |
+-------------+---------------+---------------+
| PEC         |         10000 |          8000 |
| PEN         |          8000 |          2000 |
+-------------+---------------+---------------+

mysql>
mysql>
mysql> select productCode, max(quantity), min(quantity)
    -> from products
    -> group by productCode
    -> having productCode = 'PEN';
+-------------+---------------+---------------+
| productCode | max(quantity) | min(quantity) |
+-------------+---------------+---------------+
| PEN         |          8000 |          2000 |
+-------------+---------------+---------------+

mysql>
mysql> select productCode, sum(price)
    -> from products
    -> group by productCode;
+-------------+------------+
| productCode | sum(price) |
+-------------+------------+
| PEC         |       0.97 |
| PEN         |       3.73 |
+-------------+------------+

mysql> select productCode, avg(price)
    -> from products
    -> group by productCode;
+-------------+------------+
| productCode | avg(price) |
+-------------+------------+
| PEC         |   0.485000 |
| PEN         |   1.243333 |
+-------------+------------+

mysql> select productCode, count(*)
    -> from products
    -> group by productCode;
+-------------+----------+
| productCode | count(*) |
+-------------+----------+
| PEC         |        2 |
| PEN         |        3 |
+-------------+----------+

mysql> select name, count(*)
    -> from products
    -> group by name;
+-----------+----------+
| name      | count(*) |
+-----------+----------+
| Pen Black |        1 |
| Pen Blue  |        1 |
| Pen Red   |        1 |
| Pencil 2B |        1 |
| Pencil 2H |        1 |
+-----------+----------+

mysql> select quantity, count(*)
    -> from products
    -> group by quantity;
+----------+----------+
| quantity | count(*) |
+----------+----------+
|     2000 |        1 |
|     5000 |        1 |
|     8000 |        2 |
|    10000 |        1 |
+----------+----------+

mysql> select distinct(quantity)  from products;
+----------+
| quantity |
+----------+
|     5000 |
|     8000 |
|     2000 |
|    10000 |
+----------+

mysql> select all(quantity)  from products;
+----------+
| quantity |
+----------+
|     5000 |
|     8000 |
|     2000 |
|    10000 |
|     8000 |
+----------+

mysql> SELECT name, price FROM products WHERE name LIKE 'P__%';
+-----------+-------+
| name      | price |
+-----------+-------+
| Pen Red   |  1.23 |
| Pen Blue  |  1.25 |
| Pen Black |  1.25 |
| Pencil 2B |  0.48 |
| Pencil 2H |  0.49 |
+-----------+-------+

mysql> SELECT name, price FROM products WHERE name LIKE 'P___R%';
+---------+-------+
| name    | price |
+---------+-------+
| Pen Red |  1.23 |
+---------+-------+

mysql>
Observe the following PARTICIPANTS and EVENTS table carefully and write the name of the RDBMS operation which will be used to produce the output as shown in RESULT? Also, find the Degree and Cardinality of the RESULT.
Cardinality : 6
 (a) –5 L2 / 2 m/s                 (b) –2 L2 / 5 m/s

(c) –L2 / 2 m/s                   (d) –L2 / 5 m/s
from its atoms is −436 kJ/mol and that of N2 is −712 kJ/mol, then the average bond enthalpy of N−H bond in NH3 is:
(a) -964  kJ /mol
(b) +352 kJ/mol
(c) +1056 kJ/ mol
(d) -1102  kJ/ mol
 Question 1:
Observe the following PARTICIPANTS and EVENTS table carefully and write the name of the RDBMS operation which will be used to produce the output as shown in RESULT? Also, find the Degree and Cardinality of the RESULT.

| Pen Black |  1.25 |
+-----------+-------+

mysql> SELECT name, price FROM products WHERE name LIKE 'PENCIL%';
+-----------+-------+
| name      | price |
+-----------+-------+
| Pencil 2B |  0.48 |
| Pencil 2H |  0.49 |
+-----------+-------+

mysql> SELECT name, price FROM products WHERE name like 'Pen%';
+-----------+-------+
| name      | price |
+-----------+-------+
| Pen Red   |  1.23 |
| Pen Blue  |  1.25 |
| Pen Black |  1.25 |
| Pencil 2B |  0.48 |
| Pencil 2H |  0.49 |
+-----------+-------+

mysql> SELECT name, price FROM products WHERE name like 'pen%';
+-----------+-------+
| name      | price |
+-----------+-------+
| Pen Red   |  1.23 |
| Pen Blue  |  1.25 |
| Pen Black |  1.25 |
| Pencil 2B |  0.48 |
| Pencil 2H |  0.49 |
+-----------+-------+

mysql> SELECT name, price FROM products WHERE name like 'pen %';
+-----------+-------+
| name      | price |
+-----------+-------+
| Pen Red   |  1.23 |
| Pen Blue  |  1.25 |
| Pen Black |  1.25 |
+-----------+-------+

mysql> SELECT * FROM products WHERE quantity >= 5000 AND name LIKE 'Pen %';
+-----------+-------------+----------+----------+-------+
| productID | productCode | name     | quantity | price |
+-----------+-------------+----------+----------+-------+
|      1001 | PEN         | Pen Red  |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue |     8000 |  1.25 |
+-----------+-------------+----------+----------+-------+

mysql> * FROM products WHERE quantity >= 5000 AND price < 1.24 AND name LIKE 'Pen %';
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '* FROM products WHERE quantity >= 5000 AND price < 1.24 AND name LIKE 'Pen %'' at line 1
mysql> select * FROM products WHERE quantity >= 5000 AND price < 1.24 AND name LIKE 'Pen %';
+-----------+-------------+---------+----------+-------+
| productID | productCode | name    | quantity | price |
+-----------+-------------+---------+----------+-------+
|      1001 | PEN         | Pen Red |     5000 |  1.23 |
+-----------+-------------+---------+----------+-------+

mysql>
mysql>
mysql> SELECT * FROM products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products WHERE NOT (quantity >= 5000 AND name LIKE 'Pen %');
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products WHERE  quantity >= 5000 AND name LIKE 'Pen %';
+-----------+-------------+----------+----------+-------+
| productID | productCode | name     | quantity | price |
+-----------+-------------+----------+----------+-------+
|      1001 | PEN         | Pen Red  |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue |     8000 |  1.25 |
+-----------+-------------+----------+----------+-------+

mysql> SELECT * FROM products WHERE  quantity < 5000 OR name NOT LIKE 'Pen %';
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql>
Attendance for: Class List on 2020-08-11

Names	2020-08-11 	Arrival time
vikas 210	?	10:46	11:15
md irfan	?	10:47
suraj shukla	?	10:47
samrat chhabra	?	10:47
aman sharma	?	10:47
himanshu jha	?	10:47
kirti bisht	?	10:47
simran rawat	?	10:47	11:05
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products WHERE name NOT IN ('Pen Red', 'Pen Black'); select * from products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products
    ->        WHERE (price BETWEEN 1.0 AND 2.0) AND (quantity BETWEEN 1000 AND 2000);
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products WHERE productCode IS NULL;
Empty set (0.07 sec)

mysql> SELECT * FROM products WHERE name LIKE 'Pen %' ORDER BY price ;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products WHERE name LIKE 'Pen %' ORDER BY price ASC;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products WHERE name LIKE 'Pen %' ORDER BY price DESC;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products WHERE name LIKE 'Pen %' ORDER BY price DESC, quantity;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products WHERE name LIKE 'Pen %' ORDER BY price DESC;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products ORDER BY RAND();
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products ORDER BY RAND();
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products ORDER BY RAND();
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products ORDER BY price LIMIT 2;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products ORDER BY price LIMIT 2, 1;
+-----------+-------------+---------+----------+-------+
| productID | productCode | name    | quantity | price |
+-----------+-------------+---------+----------+-------+
|      1001 | PEN         | Pen Red |     5000 |  1.23 |
+-----------+-------------+---------+----------+-------+

mysql> SELECT * FROM products ORDER BY price;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT productID AS ID, productCode AS Code,
    ->               name AS Description, price AS 'Unit Price'
    ->        FROM products
    ->        ORDER BY ID;
+------+------+-------------+------------+
| ID   | Code | Description | Unit Price |
+------+------+-------------+------------+
| 1001 | PEN  | Pen Red     |       1.23 |
| 1002 | PEN  | Pen Blue    |       1.25 |
| 1003 | PEN  | Pen Black   |       1.25 |
| 1004 | PEC  | Pencil 2B   |       0.48 |
| 1005 | PEC  | Pencil 2H   |       0.49 |
+------+------+-------------+------------+

mysql>  select * from products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> select * , price * 0.10 AS Discount from products;
+-----------+-------------+-----------+----------+-------+----------+
| productID | productCode | name      | quantity | price | Discount |
+-----------+-------------+-----------+----------+-------+----------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |   0.1230 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |   0.1250 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |   0.1250 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |   0.0480 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |   0.0490 |
+-----------+-------------+-----------+----------+-------+----------+

mysql>
mysql>
mysql> SELECT price FROM products;
+-------+
| price |
+-------+
|  1.23 |
|  1.25 |
|  1.25 |
|  0.48 |
|  0.49 |
+-------+

mysql> SELECT DISTINCT price AS 'Distinct Price' FROM products;
+----------------+
| Distinct Price |
+----------------+
|           1.23 |
|           1.25 |
|           0.48 |
|           0.49 |
+----------------+

mysql> SELECT DISTINCT price FROM products;
+-------+
| price |
+-------+
|  1.23 |
|  1.25 |
|  0.48 |
|  0.49 |
+-------+

mysql> SELECT DISTINCT price, name from Products;
+-------+-----------+
| price | name      |
+-------+-----------+
|  1.23 | Pen Red   |
|  1.25 | Pen Blue  |
|  1.25 | Pen Black |
|  0.48 | Pencil 2B |
|  0.49 | Pencil 2H |
+-------+-----------+

mysql> SELECT price, name from Products;
+-------+-----------+
| price | name      |
+-------+-----------+
|  1.23 | Pen Red   |
|  1.25 | Pen Blue  |
|  1.25 | Pen Black |
|  0.48 | Pencil 2B |
|  0.49 | Pencil 2H |
+-------+-----------+

mysql> SELECT DISTINCT productCode, price, name from Products;
+-------------+-------+-----------+
| productCode | price | name      |
+-------------+-------+-----------+
| PEN         |  1.23 | Pen Red   |
| PEN         |  1.25 | Pen Blue  |
| PEN         |  1.25 | Pen Black |
| PEC         |  0.48 | Pencil 2B |
| PEC         |  0.49 | Pencil 2H |
+-------------+-------+-----------+

mysql> SELECT DISTINCT productCode, price from Products;
+-------------+-------+
| productCode | price |
+-------------+-------+
| PEN         |  1.23 |
| PEN         |  1.25 |
| PEC         |  0.48 |
| PEC         |  0.49 |
+-------------+-------+

mysql> SELECT * FROM products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products ORDER BY productCode, productID;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products GROUP BY productCode;
ERROR 1055 (42000): Expression #1 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'southwind.products.productID' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
mysql>
mysql>
mysql> SELECT productCode, COUNT(*) FROM products GROUP BY productCode;
+-------------+----------+
| productCode | COUNT(*) |
+-------------+----------+
| PEC         |        2 |
| PEN         |        3 |
+-------------+----------+

mysql> SELECT productCode, COUNT(*) AS count
    ->        FROM products
    ->        GROUP BY productCode
    ->        ORDER BY count DESC;
+-------------+-------+
| productCode | count |
+-------------+-------+
| PEN         |     3 |
| PEC         |     2 |
+-------------+-------+

mysql> SELECT productCode, MAX(price) AS 'Highest Price', MIN(price) AS 'Lowest Price'
    ->        FROM products
    ->        GROUP BY productCode;
+-------------+---------------+--------------+
| productCode | Highest Price | Lowest Price |
+-------------+---------------+--------------+
| PEC         |          0.49 |         0.48 |
| PEN         |          1.25 |         1.23 |
+-------------+---------------+--------------+

mysql> SELECT productCode, MAX(price), MIN(price),
    ->               CAST(AVG(price) AS DECIMAL(7,2)) AS 'Average,
    '>               CAST(STD(price) AS DECIMAL(7,2)) AS 'Std Dev',
    '>               SUM(quantity)
    '>        FROM products
    '>
    '>
    '> ;
    '> ;
    '>
    '>
    '> ;
    '> ^C
mysql>
mysql>
mysql>
mysql> SELECT productCode, MAX(price), MIN(price),
    ->               CAST(AVG(price) AS DECIMAL(7,2)) AS 'Average',
    ->               CAST(STD(price) AS DECIMAL(7,2)) AS 'Std Dev',
    ->               SUM(quantity)
    ->        FROM products
    ->        GROUP BY productCode;
+-------------+------------+------------+---------+---------+---------------+
| productCode | MAX(price) | MIN(price) | Average | Std Dev | SUM(quantity) |
+-------------+------------+------------+---------+---------+---------------+
| PEC         |       0.49 |       0.48 |    0.49 |    0.01 |         18000 |
| PEN         |       1.25 |       1.23 |    1.24 |    0.01 |         15000 |
+-------------+------------+------------+---------+---------+---------------+

mysql>
mysql>
mysql> SELECT
    ->           productCode AS 'Product Code',
    ->           COUNT(*) AS 'Count',
    ->           CAST(AVG(price) AS DECIMAL(7,2)) AS 'Average'
    ->        FROM products
    ->        GROUP BY productCode
    ->        HAVING Count >=3;
+--------------+-------+---------+
| Product Code | Count | Average |
+--------------+-------+---------+
| PEN          |     3 |    1.24 |
+--------------+-------+---------+

mysql>
Enter password: *******
productCode     MAX(price)      MIN(price)      Average Std Dev SUM(quantity)

D:\mysql>mysql -u user1 -h localhost southwind -p  < abc.txt > result.csv
Enter password: *******

D:\mysql>type result.csv
productCode     MAX(price)      MIN(price)      Average Std Dev SUM(quantity)
•	PERKS is Freight Charges per kilometer.
•	Km is kilometers Travelled
•	NOP is number of passangers travelled in vechicle.
i.	To display CNO, CNAME, TRAVELDATE from the table TRAVEL in descending order of CNO.
ii.	To display the CNAME of all customers from the table TRAVEL who are travelling by vechicle with code Vo1 or Vo2
iii.	To display the CNO and CNAME of those customers from the table TRAVEL who travelled between ‘2015-12¬31’ and ‘2015-05-01’.
iv.	To display all the details from table TRAVEL for the customers, who have travel distacne more than 120 KM in ascending order of NOE
v.	SELECT COUNT (*), VCODE FROM TRAVEL GROUP BY VCODE HAVING COUNT (*) > 1;
vi.	SELECT DISTINCT VCODE FROM TRAVEL :
vii.	SELECT A.VCODE, CNAME, VEHICLETYPE FROM TRAVEL A, VEHICLE B WHERE A. VCODE = B. VCODE and KM < 90;
viii.	SELECT CNAME, KM*PERKM FROM TRAVEL A, VEHICLE B WHERE A.VCODE = B.VCODE AND A. VCODE ‘V05’;
(b) 0 A
(c) 0.13 A,  Q to P
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     4900 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> UPDATE products SET quantity = quantity + 50, price = 1.27 WHERE name = 'Pen Red';
Query OK, 1 row affected (0.04 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     4950 |  1.27 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> DELETE FROM products WHERE name LIKE 'Pencil%';
Query OK, 2 rows affected (0.08 sec)

mysql> select * from products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     4950 |  1.27 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
+-----------+-------------+-----------+----------+-------+

mysql> DELETE FROM products;
Query OK, 3 rows affected (0.03 sec)

mysql> select * from products;
Empty set (0.00 sec)

mysql> exit
Bye

D:\>cd mysql

D:\mysql>copy con > products_in.csv
\N,PEC,Pencil 3B,500,0.52
\N,PEC,Pencil 3B,500,0.52
\N,PEC,Pencil 4B,200,0.62
\N,PEC,Pencil 4B,200,0.62
\N,PEC,Pencil 5B,100,0.73
\N,PEC,Pencil 5B,100,0.73
\N,PEC,Pencil 6B,500,0.47
\N,PEC,Pencil 6B,500,0.47
^Z

D:\mysql>type products_in.csv
        1 file(s) copied.

D:\mysql>type products_in.csv
        1 file(s) copied.

D:\mysql>copy con products_in.csv
\N,PEC,Pencil 3B,500,0.52
Overwrite products_in.csv? (Yes/No/All): a
^Z
        1 file(s) copied.

D:\mysql>
D:\mysql>del products_in.csv

D:\mysql>copy con  products_in.csv
\N,PEC,Pencil 3B,500,0.52
\N,PEC,Pencil 4B,200,0.62
\N,PEC,Pencil 5B,100,0.73
\N,PEC,Pencil 6B,500,0.47
^Z
        1 file(s) copied.

D:\mysql>type products_in.csv
\N,PEC,Pencil 3B,500,0.52
\N,PEC,Pencil 4B,200,0.62
\N,PEC,Pencil 5B,100,0.73
\N,PEC,Pencil 6B,500,0.47

D:\mysql>mysql -u user1 -h 127.0.0.1 -p
Enter password: *******
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 3
Server version: 5.7.31 MySQL Community Server (GPL)

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> use southwind;
Database changed
mysql> show tables;
+---------------------+
| Tables_in_southwind |
+---------------------+
| products            |
+---------------------+

mysql> select * from products;
Empty set (0.01 sec)

mysql> LOAD DATA LOCAL INFILE 'D:/mysql/products_in.csv' INTO TABLE products
    ->          COLUMNS TERMINATED BY ','
    ->          LINES TERMINATED BY '\r\n';
Query OK, 4 rows affected (0.07 sec)
Records: 4  Deleted: 0  Skipped: 0  Warnings: 0

mysql> select * from products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1006 | PEC         | Pencil 3B |      500 |  0.52 |
|      1007 | PEC         | Pencil 4B |      200 |  0.62 |
|      1008 | PEC         | Pencil 5B |      100 |  0.73 |
|      1009 | PEC         | Pencil 6B |      500 |  0.47 |
+-----------+-------------+-----------+----------+-------+

mysql> delete from products;
Query OK, 4 rows affected (0.04 sec)

mysql> select * from products;
Empty set (0.00 sec)

mysql> exit
Bye

D:\mysql>copy con products_in.tsv
\N  PEC  Pencil 3B  500  0.52
\N  PEC  Pencil 4B  200  0.62
\N  PEC  Pencil 5B  100  0.73
\N  PEC  Pencil 6B  500  0.47
^Z
        1 file(s) copied.

D:\mysql>type products_in.tsv
\N  PEC  Pencil 3B  500  0.52
\N  PEC  Pencil 4B  200  0.62
\N  PEC  Pencil 5B  100  0.73
\N  PEC  Pencil 6B  500  0.47

D:\mysql>mysqlimport -u user1  -p --local southwind products_in.tsv
Enter password: *******
mysqlimport: Error: 1146, Table 'southwind.products_in' doesn't exist, when using table: products_in

D:\mysql>rename products_in.tsv products.tsv

D:\mysql>type products.tsv
\N  PEC  Pencil 3B  500  0.52
\N  PEC  Pencil 4B  200  0.62
\N  PEC  Pencil 5B  100  0.73
\N  PEC  Pencil 6B  500  0.47

D:\mysql>mysqlimport -u user1  -p --local southwind products_in.tsv
Enter password: *******
mysqlimport: Error: 1146, Table 'southwind.products_in' doesn't exist, when using table: products_in

D:\mysql>mysqlimport -u user1  -p --local southwind products.tsv
Enter password: *******
southwind.products: Records: 4  Deleted: 0  Skipped: 0  Warnings: 20

D:\mysql>mysql -u user1  -h 127.0.0.1  -p
Enter password: *******
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 7
Server version: 5.7.31 MySQL Community Server (GPL)

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> use southwind;
Database changed
mysql> select * from products;
+-----------+-------------+------+----------+-------+
| productID | productCode | name | quantity | price |
+-----------+-------------+------+----------+-------+
|      1013 |             |      |        0 |  0.00 |
|      1014 |             |      |        0 |  0.00 |
|      1015 |             |      |        0 |  0.00 |
|      1016 |             |      |        0 |  0.00 |
+-----------+-------------+------+----------+-------+

mysql> delete from products;
Query OK, 4 rows affected (0.04 sec)

mysql> select * from products;
Empty set (0.00 sec)

mysql> exit
Bye

D:\mysql>type products.tsv
\N      PEC     Pencil  4B      200     0.62
\N      PEC     Pencil  5B      100     0.73
D:\mysql>mysqlimport -u user1  -p --local southwind products.tsv
Enter password: *******
southwind.products: Records: 3  Deleted: 0  Skipped: 0  Warnings: 5

D:\mysql>mysql -u user1  -h 127.0.0.1  -p
Enter password: *******
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 9
Server version: 5.7.31 MySQL Community Server (GPL)

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> use southwind;
Database changed
mysql> select * from products;
+-----------+-------------+--------+----------+--------+
| productID | productCode | name   | quantity | price  |
+-----------+-------------+--------+----------+--------+
|      1001 | PEC         | Pencil |        3 | 500.00 |
|      1020 | PEC         | Pencil |        4 | 200.00 |
|      1021 | PEC         | Pencil |        5 | 100.00 |
+-----------+-------------+--------+----------+--------+

mysql> exit
Bye

D:\mysql>type abc.sql
DELETE FROM products;
INSERT INTO products VALUES (2001, 'PEC', 'Pencil 3B', 500, 0.52),
                            (NULL, 'PEC', 'Pencil 4B', 200, 0.62),
                            (NULL, 'PEC', 'Pencil 5B', 100, 0.73),
                            (NULL, 'PEC', 'Pencil 6B', 500, 0.47);
SELECT * FROM products;

D:\mysql>mysql -u user1  -h 127.0.0.1  -p
Enter password: *******
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 10
Server version: 5.7.31 MySQL Community Server (GPL)

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> use southwind;
Database changed
mysql> select * products;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'products' at line 1
mysql> select * from products;
+-----------+-------------+--------+----------+--------+
| productID | productCode | name   | quantity | price  |
+-----------+-------------+--------+----------+--------+
|      1001 | PEC         | Pencil |        3 | 500.00 |
|      1020 | PEC         | Pencil |        4 | 200.00 |
|      1021 | PEC         | Pencil |        5 | 100.00 |
+-----------+-------------+--------+----------+--------+

mysql>
mysql>
mysql> select * from products;
+-----------+-------------+--------+----------+--------+
| productID | productCode | name   | quantity | price  |
+-----------+-------------+--------+----------+--------+
|      1001 | PEC         | Pencil |        3 | 500.00 |
|      1020 | PEC         | Pencil |        4 | 200.00 |
|      1021 | PEC         | Pencil |        5 | 100.00 |
+-----------+-------------+--------+----------+--------+

mysql> source d:/mysql/abc.sql
Query OK, 3 rows affected (0.04 sec)

Query OK, 4 rows affected (0.04 sec)
Records: 4  Duplicates: 0  Warnings: 0

+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      2001 | PEC         | Pencil 3B |      500 |  0.52 |
|      2002 | PEC         | Pencil 4B |      200 |  0.62 |
|      2003 | PEC         | Pencil 5B |      100 |  0.73 |
|      2004 | PEC         | Pencil 6B |      500 |  0.47 |
+-----------+-------------+-----------+----------+-------+

mysql>

D:\>mysql -u user1 -h localhost -p
Enter password: *******
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 2
Server version: 5.7.31 MySQL Community Server (GPL)

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+

mysql> create database southwind;
Query OK, 1 row affected (0.06 sec)

mysql> drop database southwind;
Query OK, 0 rows affected (0.43 sec)

mysql> create database if not exists southwind;
Query OK, 1 row affected (0.01 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| southwind          |
| sys                |
+--------------------+

mysql> drop database if exists southwind;
Query OK, 0 rows affected (0.00 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+

mysql> drop database southwind;
ERROR 1008 (HY000): Can't drop database 'southwind'; database doesn't exist
mysql> drop database if exists southwind;
Query OK, 0 rows affected, 1 warning (0.00 sec)

mysql> create database southwind;
Query OK, 1 row affected (0.01 sec)

mysql>
mysql>
mysql> show create database southwind;
+-----------+----------------------------------------------------------------------+
| Database  | Create Database                                                      |
+-----------+----------------------------------------------------------------------+
| southwind | CREATE DATABASE `southwind` /*!40100 DEFAULT CHARACTER SET latin1 */ |
+-----------+----------------------------------------------------------------------+

mysql>


mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| southwind          |
| sys                |
+--------------------+

mysql> use southwind;
Database changed
mysql> select database();
+------------+
| database() |
+------------+
| southwind  |
+------------+

mysql> use mysql;
Database changed
mysql> select database();
+------------+
| database() |
+------------+
| mysql      |
+------------+

mysql> use southwind;
Database changed
mysql> show tables;
Empty set (0.03 sec)

mysql> CREATE TABLE IF NOT EXISTS products (
    ->          productID    INT UNSIGNED  NOT NULL AUTO_INCREMENT,
    ->          productCode  CHAR(3)       NOT NULL DEFAULT '',
    ->          name         VARCHAR(30)   NOT NULL DEFAULT '',
    ->          quantity     INT UNSIGNED  NOT NULL DEFAULT 0,
    ->          price        DECIMAL(7,2)  NOT NULL DEFAULT 99999.99,
    ->          PRIMARY KEY  (productID)
    ->        );
Query OK, 0 rows affected (0.87 sec)

mysql> show tables;
+---------------------+
| Tables_in_southwind |
+---------------------+
| products            |
+---------------------+





mysql> describe products;
+-------------+------------------+------+-----+----------+----------------+
| Field       | Type             | Null | Key | Default  | Extra          |
+-------------+------------------+------+-----+----------+----------------+
| productID   | int(10) unsigned | NO   | PRI | NULL     | auto_increment |
| productCode | char(3)          | NO   |     |          |                |
| name        | varchar(30)      | NO   |     |          |                |
| quantity    | int(10) unsigned | NO   |     | 0        |                |
| price       | decimal(7,2)     | NO   |     | 99999.99 |                |
+-------------+------------------+------+-----+----------+----------------+

mysql> select * from products;
Empty set (0.03 sec)

mysql> INSERT INTO products VALUES (1001, 'PEN', 'Pen Red', 5000, 1.23);
Query OK, 1 row affected (0.16 sec)

mysql> select * from products;
+-----------+-------------+---------+----------+-------+
| productID | productCode | name    | quantity | price |
+-----------+-------------+---------+----------+-------+
|      1001 | PEN         | Pen Red |     5000 |  1.23 |
+-----------+-------------+---------+----------+-------+

mysql> INSERT INTO products VALUES
    ->          (NULL, 'PEN', 'Pen Blue',  8000, 1.25),
    ->          (NULL, 'PEN', 'Pen Black', 2000, 1.25);
Query OK, 2 rows affected (0.06 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> select * from products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
+-----------+-------------+-----------+----------+-------+

mysql> INSERT INTO products (productCode, name, quantity, price) VALUES
    ->          ('PEC', 'Pencil 2B', 10000, 0.48),
    ->          ('PEC', 'Pencil 2H', 8000, 0.49);
Query OK, 2 rows affected (0.04 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> select * from products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> INSERT INTO products (productCode, name) VALUES ('PEC', 'Pencil HB');
Query OK, 1 row affected (0.03 sec)

mysql> select * from products;
+-----------+-------------+-----------+----------+----------+
| productID | productCode | name      | quantity | price    |
+-----------+-------------+-----------+----------+----------+
|      1001 | PEN         | Pen Red   |     5000 |     1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |     1.25 |
|      1003 | PEN         | Pen Black |     2000 |     1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |     0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |     0.49 |
|      1006 | PEC         | Pencil HB |        0 | 99999.99 |
+-----------+-------------+-----------+----------+----------+

mysql> INSERT INTO products values (NULL, NULL, NULL, NULL, NULL);
ERROR 1048 (23000): Column 'productCode' cannot be null
mysql>

mysql>
mysql> use southwind;
Database changed
mysql>
mysql> select * from products;
+-----------+-------------+-----------+----------+----------+
| productID | productCode | name      | quantity | price    |
+-----------+-------------+-----------+----------+----------+
|      1001 | PEN         | Pen Red   |     5000 |     1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |     1.25 |
|      1003 | PEN         | Pen Black |     2000 |     1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |     0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |     0.49 |
|      1006 | PEC         | Pencil HB |        0 | 99999.99 |
+-----------+-------------+-----------+----------+----------+

mysql> select productID, productCode from products;
+-----------+-------------+
| productID | productCode |
+-----------+-------------+
|      1001 | PEN         |
|      1002 | PEN         |
|      1003 | PEN         |
|      1004 | PEC         |
|      1005 | PEC         |
|      1006 | PEC         |
+-----------+-------------+

mysql> select * from products where productCode = 'pec';
+-----------+-------------+-----------+----------+----------+
| productID | productCode | name      | quantity | price    |
+-----------+-------------+-----------+----------+----------+
|      1004 | PEC         | Pencil 2B |    10000 |     0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |     0.49 |
|      1006 | PEC         | Pencil HB |        0 | 99999.99 |
+-----------+-------------+-----------+----------+----------+

mysql> select * from products where productCode = "pec";
+-----------+-------------+-----------+----------+----------+
| productID | productCode | name      | quantity | price    |
+-----------+-------------+-----------+----------+----------+
|      1004 | PEC         | Pencil 2B |    10000 |     0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |     0.49 |
|      1006 | PEC         | Pencil HB |        0 | 99999.99 |
+-----------+-------------+-----------+----------+----------+

mysql> show tables;
+---------------------+
| Tables_in_southwind |
+---------------------+
| products            |
+---------------------+

mysql> select * from Products where productCode = "pec";
+-----------+-------------+-----------+----------+----------+
| productID | productCode | name      | quantity | price    |
+-----------+-------------+-----------+----------+----------+
|      1004 | PEC         | Pencil 2B |    10000 |     0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |     0.49 |
|      1006 | PEC         | Pencil HB |        0 | 99999.99 |
+-----------+-------------+-----------+----------+----------+

mysql> select * from Products where productCode = "pec"  and price < 2.0;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> select * from Products where productCode = "pec"  and price < 2.0 and quantity > 8000;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
+-----------+-------------+-----------+----------+-------+

mysql> select productID, productCode, quantity
    -> from products
    -> where name like "Pencil%"  or quantity >= 8000;
+-----------+-------------+----------+
| productID | productCode | quantity |
+-----------+-------------+----------+
|      1002 | PEN         |     8000 |
|      1004 | PEC         |    10000 |
|      1005 | PEC         |     8000 |
|      1006 | PEC         |        0 |
+-----------+-------------+----------+

mysql> DELETE FROM products WHERE productID = 1006;
Query OK, 1 row affected (0.16 sec)

mysql> select * from Products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT name, price FROM products;
+-----------+-------+
| name      | price |
+-----------+-------+
| Pen Red   |  1.23 |
| Pen Blue  |  1.25 |
| Pen Black |  1.25 |
| Pencil 2B |  0.48 |
| Pencil 2H |  0.49 |
+-----------+-------+

mysql> 
mysql>
mysql> select productCode, max(quantity), min(quantity) from Products group by productCode;
+-------------+---------------+---------------+
| productCode | max(quantity) | min(quantity) |
+-------------+---------------+---------------+
| PEC         |         10000 |          8000 |
| PEN         |          8000 |          2000 |
+-------------+---------------+---------------+

mysql>
mysql>
mysql> select productCode, max(quantity), min(quantity)
    -> from products
    -> group by productCode
    -> having productCode = 'PEN';
+-------------+---------------+---------------+
| productCode | max(quantity) | min(quantity) |
+-------------+---------------+---------------+
| PEN         |          8000 |          2000 |
+-------------+---------------+---------------+

mysql>
mysql> select productCode, sum(price)
    -> from products
    -> group by productCode;
+-------------+------------+
| productCode | sum(price) |
+-------------+------------+
| PEC         |       0.97 |
| PEN         |       3.73 |
+-------------+------------+

mysql> select productCode, avg(price)
    -> from products
    -> group by productCode;
+-------------+------------+
| productCode | avg(price) |
+-------------+------------+
| PEC         |   0.485000 |
| PEN         |   1.243333 |
+-------------+------------+

mysql> select productCode, count(*)
    -> from products
    -> group by productCode;
+-------------+----------+
| productCode | count(*) |
+-------------+----------+
| PEC         |        2 |
| PEN         |        3 |
+-------------+----------+

mysql> select name, count(*)
    -> from products
    -> group by name;
+-----------+----------+
| name      | count(*) |
+-----------+----------+
| Pen Black |        1 |
| Pen Blue  |        1 |
| Pen Red   |        1 |
| Pencil 2B |        1 |
| Pencil 2H |        1 |
+-----------+----------+

mysql> select quantity, count(*)
    -> from products
    -> group by quantity;
+----------+----------+
| quantity | count(*) |
+----------+----------+
|     2000 |        1 |
|     5000 |        1 |
|     8000 |        2 |
|    10000 |        1 |
+----------+----------+

mysql> select distinct(quantity)  from products;
+----------+
| quantity |
+----------+
|     5000 |
|     8000 |
|     2000 |
|    10000 |
+----------+

mysql> select all(quantity)  from products;
+----------+
| quantity |
+----------+
|     5000 |
|     8000 |
|     2000 |
|    10000 |
|     8000 |
+----------+

mysql> SELECT name, price FROM products WHERE name LIKE 'P__%';
+-----------+-------+
| name      | price |
+-----------+-------+
| Pen Red   |  1.23 |
| Pen Blue  |  1.25 |
| Pen Black |  1.25 |
| Pencil 2B |  0.48 |
| Pencil 2H |  0.49 |
+-----------+-------+

mysql> SELECT name, price FROM products WHERE name LIKE 'P___R%';
+---------+-------+
| name    | price |
+---------+-------+
| Pen Red |  1.23 |
+---------+-------+

mysql>

mysql> SELECT name, price FROM products WHERE price < 1.0;
+-----------+-------+
| name      | price |
+-----------+-------+
| Pencil 2B |  0.48 |
| Pencil 2H |  0.49 |
+-----------+-------+

mysql> SELECT name, quantity FROM products WHERE quantity <= 2000;
+-----------+----------+
| name      | quantity |
+-----------+----------+
| Pen Black |     2000 |
+-----------+----------+

mysql> SELECT name, price FROM products WHERE productCode = 'PEN';
+-----------+-------+
| name      | price |
+-----------+-------+
| Pen Red   |  1.23 |
| Pen Blue  |  1.25 |
| Pen Black |  1.25 |
+-----------+-------+

mysql> SELECT name, price FROM products WHERE name LIKE 'PENCIL%';
+-----------+-------+
| name      | price |
+-----------+-------+
| Pencil 2B |  0.48 |
| Pencil 2H |  0.49 |
+-----------+-------+

mysql> SELECT name, price FROM products WHERE name like 'Pen%';
+-----------+-------+
| name      | price |
+-----------+-------+
| Pen Red   |  1.23 |
| Pen Blue  |  1.25 |
| Pen Black |  1.25 |
| Pencil 2B |  0.48 |
| Pencil 2H |  0.49 |
+-----------+-------+

mysql> SELECT name, price FROM products WHERE name like 'pen%';
+-----------+-------+
| name      | price |
+-----------+-------+
| Pen Red   |  1.23 |
| Pen Blue  |  1.25 |
| Pen Black |  1.25 |
| Pencil 2B |  0.48 |
| Pencil 2H |  0.49 |
+-----------+-------+

mysql> SELECT name, price FROM products WHERE name like 'pen %';
+-----------+-------+
| name      | price |
+-----------+-------+
| Pen Red   |  1.23 |
| Pen Blue  |  1.25 |
| Pen Black |  1.25 |
+-----------+-------+

mysql> SELECT * FROM products WHERE quantity >= 5000 AND name LIKE 'Pen %';
+-----------+-------------+----------+----------+-------+
| productID | productCode | name     | quantity | price |
+-----------+-------------+----------+----------+-------+
|      1001 | PEN         | Pen Red  |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue |     8000 |  1.25 |
+-----------+-------------+----------+----------+-------+

mysql> 
mysql> select * FROM products WHERE quantity >= 5000 AND price < 1.24 AND name LIKE 'Pen %';
+-----------+-------------+---------+----------+-------+
| productID | productCode | name    | quantity | price |
+-----------+-------------+---------+----------+-------+
|      1001 | PEN         | Pen Red |     5000 |  1.23 |
+-----------+-------------+---------+----------+-------+

mysql>
mysql>
mysql> SELECT * FROM products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products WHERE NOT (quantity >= 5000 AND name LIKE 'Pen %');
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products WHERE  quantity >= 5000 AND name LIKE 'Pen %';
+-----------+-------------+----------+----------+-------+
| productID | productCode | name     | quantity | price |
+-----------+-------------+----------+----------+-------+
|      1001 | PEN         | Pen Red  |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue |     8000 |  1.25 |
+-----------+-------------+----------+----------+-------+

mysql> SELECT * FROM products WHERE  quantity < 5000 OR name NOT LIKE 'Pen %';
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql>

Database changed
mysql> SELECT * FROM products WHERE name IN ('Pen Red', 'Pen Black');
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products WHERE name NOT IN ('Pen Red', 'Pen Black');
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products WHERE name NOT IN ('Pen Red', 'Pen Black'); select * from products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products
    ->        WHERE (price BETWEEN 1.0 AND 2.0) AND (quantity BETWEEN 1000 AND 2000);
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products WHERE productCode IS NULL;
Empty set (0.07 sec)

mysql> SELECT * FROM products WHERE name LIKE 'Pen %' ORDER BY price ;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products WHERE name LIKE 'Pen %' ORDER BY price ASC;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products WHERE name LIKE 'Pen %' ORDER BY price DESC;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products WHERE name LIKE 'Pen %' ORDER BY price DESC, quantity;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products WHERE name LIKE 'Pen %' ORDER BY price DESC;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products ORDER BY RAND();
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products ORDER BY RAND();
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products ORDER BY RAND();
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products ORDER BY price LIMIT 2;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products ORDER BY price LIMIT 2, 1;
+-----------+-------------+---------+----------+-------+
| productID | productCode | name    | quantity | price |
+-----------+-------------+---------+----------+-------+
|      1001 | PEN         | Pen Red |     5000 |  1.23 |
+-----------+-------------+---------+----------+-------+

mysql> SELECT * FROM products ORDER BY price;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT productID AS ID, productCode AS Code,
    ->               name AS Description, price AS 'Unit Price'
    ->        FROM products
    ->        ORDER BY ID;
+------+------+-------------+------------+
| ID   | Code | Description | Unit Price |
+------+------+-------------+------------+
| 1001 | PEN  | Pen Red     |       1.23 |
| 1002 | PEN  | Pen Blue    |       1.25 |
| 1003 | PEN  | Pen Black   |       1.25 |
| 1004 | PEC  | Pencil 2B   |       0.48 |
| 1005 | PEC  | Pencil 2H   |       0.49 |
+------+------+-------------+------------+

mysql>  select * from products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> select * , price * 0.10 AS Discount from products;
+-----------+-------------+-----------+----------+-------+----------+
| productID | productCode | name      | quantity | price | Discount |
+-----------+-------------+-----------+----------+-------+----------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |   0.1230 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |   0.1250 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |   0.1250 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |   0.0480 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |   0.0490 |
+-----------+-------------+-----------+----------+-------+----------+

mysql>
mysql>
mysql> SELECT price FROM products;
+-------+
| price |
+-------+
|  1.23 |
|  1.25 |
|  1.25 |
|  0.48 |
|  0.49 |
+-------+

mysql> SELECT DISTINCT price AS 'Distinct Price' FROM products;
+----------------+
| Distinct Price |
+----------------+
|           1.23 |
|           1.25 |
|           0.48 |
|           0.49 |
+----------------+

mysql> SELECT DISTINCT price FROM products;
+-------+
| price |
+-------+
|  1.23 |
|  1.25 |
|  0.48 |
|  0.49 |
+-------+

mysql> SELECT DISTINCT price, name from Products;
+-------+-----------+
| price | name      |
+-------+-----------+
|  1.23 | Pen Red   |
|  1.25 | Pen Blue  |
|  1.25 | Pen Black |
|  0.48 | Pencil 2B |
|  0.49 | Pencil 2H |
+-------+-----------+

mysql> SELECT price, name from Products;
+-------+-----------+
| price | name      |
+-------+-----------+
|  1.23 | Pen Red   |
|  1.25 | Pen Blue  |
|  1.25 | Pen Black |
|  0.48 | Pencil 2B |
|  0.49 | Pencil 2H |
+-------+-----------+

mysql> SELECT DISTINCT productCode, price, name from Products;
+-------------+-------+-----------+
| productCode | price | name      |
+-------------+-------+-----------+
| PEN         |  1.23 | Pen Red   |
| PEN         |  1.25 | Pen Blue  |
| PEN         |  1.25 | Pen Black |
| PEC         |  0.48 | Pencil 2B |
| PEC         |  0.49 | Pencil 2H |
+-------------+-------+-----------+

mysql> SELECT DISTINCT productCode, price from Products;
+-------------+-------+
| productCode | price |
+-------------+-------+
| PEN         |  1.23 |
| PEN         |  1.25 |
| PEC         |  0.48 |
| PEC         |  0.49 |
+-------------+-------+

mysql> SELECT * FROM products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products ORDER BY productCode, productID;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
+-----------+-------------+-----------+----------+-------+


mysql>
mysql> SELECT productCode, COUNT(*) FROM products GROUP BY productCode;
+-------------+----------+
| productCode | COUNT(*) |
+-------------+----------+
| PEC         |        2 |
| PEN         |        3 |
+-------------+----------+

mysql> SELECT productCode, COUNT(*) AS count
    ->        FROM products
    ->        GROUP BY productCode
    ->        ORDER BY count DESC;
+-------------+-------+
| productCode | count |
+-------------+-------+
| PEN         |     3 |
| PEC         |     2 |
+-------------+-------+

mysql> SELECT productCode, MAX(price) AS 'Highest Price', MIN(price) AS 'Lowest Price'
    ->        FROM products
    ->        GROUP BY productCode;
+-------------+---------------+--------------+
| productCode | Highest Price | Lowest Price |
+-------------+---------------+--------------+
| PEC         |          0.49 |         0.48 |
| PEN         |          1.25 |         1.23 |
+-------------+---------------+--------------+

mysql>
mysql> SELECT productCode, MAX(price), MIN(price),
    ->               CAST(AVG(price) AS DECIMAL(7,2)) AS 'Average',
    ->               CAST(STD(price) AS DECIMAL(7,2)) AS 'Std Dev',
    ->               SUM(quantity)
    ->        FROM products
    ->        GROUP BY productCode;
+-------------+------------+------------+---------+---------+---------------+
| productCode | MAX(price) | MIN(price) | Average | Std Dev | SUM(quantity) |
+-------------+------------+------------+---------+---------+---------------+
| PEC         |       0.49 |       0.48 |    0.49 |    0.01 |         18000 |
| PEN         |       1.25 |       1.23 |    1.24 |    0.01 |         15000 |
+-------------+------------+------------+---------+---------+---------------+



mysql> use southwind;
Database changed
mysql> select * from products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> UPDATE products SET quantity = quantity - 100 WHERE name = 'Pen Red';
Query OK, 1 row affected (0.17 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     4900 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> UPDATE products SET quantity = quantity + 50, price = 1.27 WHERE name = 'Pen Red';
Query OK, 1 row affected (0.04 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     4950 |  1.27 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> DELETE FROM products WHERE name LIKE 'Pencil%';
Query OK, 2 rows affected (0.08 sec)

mysql> select * from products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     4950 |  1.27 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
+-----------+-------------+-----------+----------+-------+

mysql> DELETE FROM products;
Query OK, 3 rows affected (0.03 sec)

mysql> select * from products;
Empty set (0.00 sec)

mysql> exit
Bye

D:\>cd mysql


D:\mysql>copy con  products_in.csv
\N,PEC,Pencil 3B,500,0.52
\N,PEC,Pencil 4B,200,0.62
\N,PEC,Pencil 5B,100,0.73
\N,PEC,Pencil 6B,500,0.47
^Z
        1 file(s) copied.

D:\mysql>type products_in.csv
\N,PEC,Pencil 3B,500,0.52
\N,PEC,Pencil 4B,200,0.62
\N,PEC,Pencil 5B,100,0.73
\N,PEC,Pencil 6B,500,0.47

D:\mysql>mysql -u user1 -h 127.0.0.1 -p
Enter password: *******
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 3
Server version: 5.7.31 MySQL Community Server (GPL)

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> use southwind;
Database changed
mysql> show tables;
+---------------------+
| Tables_in_southwind |
+---------------------+
| products            |
+---------------------+

mysql> select * from products;
Empty set (0.01 sec)

mysql> LOAD DATA LOCAL INFILE 'D:/mysql/products_in.csv' INTO TABLE products
    ->          COLUMNS TERMINATED BY ','
    ->          LINES TERMINATED BY '\r\n';
Query OK, 4 rows affected (0.07 sec)
Records: 4  Deleted: 0  Skipped: 0  Warnings: 0

mysql> select * from products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1006 | PEC         | Pencil 3B |      500 |  0.52 |
|      1007 | PEC         | Pencil 4B |      200 |  0.62 |
|      1008 | PEC         | Pencil 5B |      100 |  0.73 |
|      1009 | PEC         | Pencil 6B |      500 |  0.47 |
+-----------+-------------+-----------+----------+-------+

mysql> delete from products;
Query OK, 4 rows affected (0.04 sec)

mysql> select * from products;
Empty set (0.00 sec)

mysql> exit
Bye

D:\mysql>copy con products_in.tsv
\N  PEC  Pencil 3B  500  0.52
\N  PEC  Pencil 4B  200  0.62
\N  PEC  Pencil 5B  100  0.73
\N  PEC  Pencil 6B  500  0.47
^Z
        1 file(s) copied.

D:\mysql>type products_in.tsv
\N  PEC  Pencil 3B  500  0.52
\N  PEC  Pencil 4B  200  0.62
\N  PEC  Pencil 5B  100  0.73
\N  PEC  Pencil 6B  500  0.47

D:\mysql>mysqlimport -u user1  -p --local southwind products_in.tsv
Enter password: *******
mysqlimport: Error: 1146, Table 'southwind.products_in' doesn't exist, when using table: products_in

D:\mysql>rename products_in.tsv products.tsv

D:\mysql>type products.tsv
\N	PEC	Pencil	4B	200	0.62
\N	PEC	Pencil	5B	100	0.73



D:\mysql>type products.tsv
\N      PEC     Pencil  4B      200     0.62
\N      PEC     Pencil  5B      100     0.73
D:\mysql>mysqlimport -u user1  -p --local southwind products.tsv
Enter password: *******
southwind.products: Records: 3  Deleted: 0  Skipped: 0  Warnings: 5

D:\mysql>mysql -u user1  -h 127.0.0.1  -p
Enter password: *******
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 9
Server version: 5.7.31 MySQL Community Server (GPL)

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> use southwind;
Database changed
mysql> select * from products;
+-----------+-------------+--------+----------+--------+
| productID | productCode | name   | quantity | price  |
+-----------+-------------+--------+----------+--------+
|      1001 | PEC         | Pencil |        3 | 500.00 |
|      1020 | PEC         | Pencil |        4 | 200.00 |
|      1021 | PEC         | Pencil |        5 | 100.00 |
+-----------+-------------+--------+----------+--------+

mysql> exit
Bye

D:\mysql>type abc.sql
DELETE FROM products;
INSERT INTO products VALUES (2001, 'PEC', 'Pencil 3B', 500, 0.52),
                            (NULL, 'PEC', 'Pencil 4B', 200, 0.62),
                            (NULL, 'PEC', 'Pencil 5B', 100, 0.73),
                            (NULL, 'PEC', 'Pencil 6B', 500, 0.47);
SELECT * FROM products;

D:\mysql>mysql -u user1  -h 127.0.0.1  -p
Enter password: *******
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 10
Server version: 5.7.31 MySQL Community Server (GPL)

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> use southwind;
Database changed

mysql> select * from products;
+-----------+-------------+--------+----------+--------+
| productID | productCode | name   | quantity | price  |
+-----------+-------------+--------+----------+--------+
|      1001 | PEC         | Pencil |        3 | 500.00 |
|      1020 | PEC         | Pencil |        4 | 200.00 |
|      1021 | PEC         | Pencil |        5 | 100.00 |
+-----------+-------------+--------+----------+--------+

mysql>
mysql>
mysql> select * from products;
+-----------+-------------+--------+----------+--------+
| productID | productCode | name   | quantity | price  |
+-----------+-------------+--------+----------+--------+
|      1001 | PEC         | Pencil |        3 | 500.00 |
|      1020 | PEC         | Pencil |        4 | 200.00 |
|      1021 | PEC         | Pencil |        5 | 100.00 |
+-----------+-------------+--------+----------+--------+

mysql> source d:/mysql/abc.sql
Query OK, 3 rows affected (0.04 sec)

Query OK, 4 rows affected (0.04 sec)
Records: 4  Duplicates: 0  Warnings: 0

+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      2001 | PEC         | Pencil 3B |      500 |  0.52 |
|      2002 | PEC         | Pencil 4B |      200 |  0.62 |
|      2003 | PEC         | Pencil 5B |      100 |  0.73 |
|      2004 | PEC         | Pencil 6B |      500 |  0.47 |
+-----------+-------------+-----------+----------+-------+

mysql>
Give the output the following SQL queries :
i.	Select Designation Count (*) From Admin Group By Designation Having Count (*) <2;
ii.	SELECT max (EXPERIENCE) FROM SCH¬OOL;
iii.	SELECT TEACHER FROM SCHOOL WHERE EXPERIENCE >12 ORDER BY TEACHER;
iv.	SELECT COUNT (*), GENDER FROM AD¬MIN GROUP BY GENDER;
(a) 1
(b) 2
(c) 3
(d) 4

(a) A point of maximum         

    ->          name        VARCHAR(30)   NOT NULL DEFAULT '',
    ->          phone       CHAR(8)       NOT NULL DEFAULT '',
    ->          PRIMARY KEY (supplierID)
    ->        );
Query OK, 0 rows affected (1.06 sec)

mysql> show tables;
+---------------------+
| Tables_in_southwind |
+---------------------+
| products            |
| suppliers           |
+---------------------+

mysql> describe suppliers;
+------------+------------------+------+-----+---------+----------------+
| Field      | Type             | Null | Key | Default | Extra          |
+------------+------------------+------+-----+---------+----------------+
| supplierID | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| name       | varchar(30)      | NO   |     |         |                |
| phone      | char(8)          | NO   |     |         |                |
+------------+------------------+------+-----+---------+----------------+

mysql> INSERT INTO suppliers VALUE
    ->           (501, 'ABC Traders', '88881111'),
    ->           (502, 'XYZ Company', '88882222'),
    ->           (503, 'QQ Corp', '88883333');
Query OK, 3 rows affected (0.14 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql>
mysql> select * from suppliers;
+------------+-------------+----------+
| supplierID | name        | phone    |
+------------+-------------+----------+
|        501 | ABC Traders | 88881111 |
|        502 | XYZ Company | 88882222 |
|        503 | QQ Corp     | 88883333 |
+------------+-------------+----------+

mysql> describe products;
+-------------+------------------+------+-----+----------+----------------+
| Field       | Type             | Null | Key | Default  | Extra          |
+-------------+------------------+------+-----+----------+----------------+
| productID   | int(10) unsigned | NO   | PRI | NULL     | auto_increment |
| productCode | char(3)          | NO   |     |          |                |
| name        | varchar(30)      | NO   |     |          |                |
| quantity    | int(10) unsigned | NO   |     | 0        |                |
| price       | decimal(7,2)     | NO   |     | 99999.99 |                |
+-------------+------------------+------+-----+----------+----------------+

mysql> ALTER TABLE products
    ->        ADD COLUMN supplierID INT UNSIGNED NOT NULL;
Query OK, 0 rows affected (1.21 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> describe products;
+-------------+------------------+------+-----+----------+----------------+
| Field       | Type             | Null | Key | Default  | Extra          |
+-------------+------------------+------+-----+----------+----------------+
| productID   | int(10) unsigned | NO   | PRI | NULL     | auto_increment |
| productCode | char(3)          | NO   |     |          |                |
| name        | varchar(30)      | NO   |     |          |                |
| quantity    | int(10) unsigned | NO   |     | 0        |                |
| price       | decimal(7,2)     | NO   |     | 99999.99 |                |
| supplierID  | int(10) unsigned | NO   |     | NULL     |                |
+-------------+------------------+------+-----+----------+----------------+

mysql> select * from products;
+-----------+-------------+-----------+----------+-------+------------+
| productID | productCode | name      | quantity | price | supplierID |
+-----------+-------------+-----------+----------+-------+------------+
|      2001 | PEC         | Pencil 3B |      500 |  0.52 |          0 |
|      2002 | PEC         | Pencil 4B |      200 |  0.62 |          0 |
|      2003 | PEC         | Pencil 5B |      100 |  0.73 |          0 |
|      2004 | PEC         | Pencil 6B |      500 |  0.47 |          0 |
+-----------+-------------+-----------+----------+-------+------------+

mysql> UPDATE products SET supplierID = 501;
Query OK, 4 rows affected (0.07 sec)
Rows matched: 4  Changed: 4  Warnings: 0

mysql> select * from products;
+-----------+-------------+-----------+----------+-------+------------+
| productID | productCode | name      | quantity | price | supplierID |
+-----------+-------------+-----------+----------+-------+------------+
|      2001 | PEC         | Pencil 3B |      500 |  0.52 |        501 |
|      2002 | PEC         | Pencil 4B |      200 |  0.62 |        501 |
|      2003 | PEC         | Pencil 5B |      100 |  0.73 |        501 |
|      2004 | PEC         | Pencil 6B |      500 |  0.47 |        501 |
+-----------+-------------+-----------+----------+-------+------------+

mysql>
mysql>
mysql> ALTER TABLE products
    ->        ADD FOREIGN KEY (supplierID) REFERENCES suppliers (supplierID);
Query OK, 4 rows affected (0.87 sec)
Records: 4  Duplicates: 0  Warnings: 0

mysql> describe products;
+-------------+------------------+------+-----+----------+----------------+
| Field       | Type             | Null | Key | Default  | Extra          |
+-------------+------------------+------+-----+----------+----------------+
| productID   | int(10) unsigned | NO   | PRI | NULL     | auto_increment |
| productCode | char(3)          | NO   |     |          |                |
| name        | varchar(30)      | NO   |     |          |                |
| quantity    | int(10) unsigned | NO   |     | 0        |                |
| price       | decimal(7,2)     | NO   |     | 99999.99 |                |
| supplierID  | int(10) unsigned | NO   | MUL | NULL     |                |
+-------------+------------------+------+-----+----------+----------------+

mysql>
mysql> UPDATE products SET supplierID = 502 WHERE productID  = 2004;
Query OK, 1 row affected (0.17 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from products;
+-----------+-------------+-----------+----------+-------+------------+
| productID | productCode | name      | quantity | price | supplierID |
+-----------+-------------+-----------+----------+-------+------------+
|      2001 | PEC         | Pencil 3B |      500 |  0.52 |        501 |
|      2002 | PEC         | Pencil 4B |      200 |  0.62 |        501 |
|      2003 | PEC         | Pencil 5B |      100 |  0.73 |        501 |
|      2004 | PEC         | Pencil 6B |      500 |  0.47 |        502 |
+-----------+-------------+-----------+----------+-------+------------+

mysql> SELECT products.name, price, suppliers.name
    ->        FROM products, suppliers
    ->        WHERE products.supplierID = suppliers.supplierID
    ->           AND price < 0.6;
+-----------+-------+-------------+
| name      | price | name        |
+-----------+-------+-------------+
| Pencil 3B |  0.52 | ABC Traders |
| Pencil 6B |  0.47 | XYZ Company |
+-----------+-------+-------------+

mysql> select * products;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'products' at line 1
mysql> select * from products;
+-----------+-------------+-----------+----------+-------+------------+
| productID | productCode | name      | quantity | price | supplierID |
+-----------+-------------+-----------+----------+-------+------------+
|      2001 | PEC         | Pencil 3B |      500 |  0.52 |        501 |
|      2002 | PEC         | Pencil 4B |      200 |  0.62 |        501 |
|      2003 | PEC         | Pencil 5B |      100 |  0.73 |        501 |
|      2004 | PEC         | Pencil 6B |      500 |  0.47 |        502 |
+-----------+-------------+-----------+----------+-------+------------+

mysql> select * from suppliers;
+------------+-------------+----------+
| supplierID | name        | phone    |
+------------+-------------+----------+
|        501 | ABC Traders | 88881111 |
|        502 | XYZ Company | 88882222 |
|        503 | QQ Corp     | 88883333 |
+------------+-------------+----------+

mysql> SELECT products.name, price, suppliers.name
    ->        FROM products, suppliers
    ->        WHERE products.supplierID = suppliers.supplierID
    ->           AND price < 0.6;
+-----------+-------+-------------+
| name      | price | name        |
+-----------+-------+-------------+
| Pencil 3B |  0.52 | ABC Traders |
| Pencil 6B |  0.47 | XYZ Company |
+-----------+-------+-------------+

mysql>
mysql> SELECT products.name, price, suppliers.name , phone
    ->        FROM products, suppliers
    ->        WHERE products.supplierID = suppliers.supplierID
    ->           AND price > 0.6;
+-----------+-------+-------------+----------+
| name      | price | name        | phone    |
+-----------+-------+-------------+----------+
| Pencil 4B |  0.62 | ABC Traders | 88881111 |
| Pencil 5B |  0.73 | ABC Traders | 88881111 |
+-----------+-------+-------------+----------+

mysql> SELECT products.name AS 'Product Name', price, suppliers.name AS 'Supplier Name'
    ->        FROM products, suppliers
    ->        WHERE products.supplierID = suppliers.supplierID AND price < 0.6;
+--------------+-------+---------------+
| Product Name | price | Supplier Name |
+--------------+-------+---------------+
| Pencil 3B    |  0.52 | ABC Traders   |
| Pencil 6B    |  0.47 | XYZ Company   |
+--------------+-------+---------------+

mysql>
mysql>
mysql>
mysql>
mysql>
mysql> SELECT products.name AS 'Product Name', price, suppliers.name AS 'Supplier Name'
    ->        FROM products
    ->           JOIN suppliers ON products.supplierID = suppliers.supplierID
    ->        WHERE price < 0.6;
+--------------+-------+---------------+
| Product Name | price | Supplier Name |
+--------------+-------+---------------+
| Pencil 3B    |  0.52 | ABC Traders   |
| Pencil 6B    |  0.47 | XYZ Company   |
+--------------+-------+---------------+

mysql>
(i) SELECT Name, Joinyear FROM APPLI¬CANTS
	WHERE GENDER=’F’ and C_ID=’A02′;
(ii)	SELECT MIN (Joinyear) 
	FROM APPLICANTS
	WHERE Gender=’m’;
(iii)	SELECT AVG (Fee) FROM APPLICANTS
	WHERE C_ID=’A0T OR C_ID=’A05′;
(iv)	SELECT SUM- (Fee), C_ID FROM C_ ID
	GROUP BY C_ID
	HAVING COUNT(*)=2;
wires is equal to L, the cross-section radius of each wire equals a. In the case a << L find:
(a) the current density at the point equally removed from the axes of the wires by a distance r if the potential difference between the
wires is equal to V;
|      2003 | PEC         | Pencil 5B |      100 |  0.73 |        501 |
|      2004 | PEC         | Pencil 6B |      500 |  0.47 |        502 |
+-----------+-------------+-----------+----------+-------+------------+

mysql> select * from suppliers;
+------------+-------------+----------+
| supplierID | name        | phone    |
+------------+-------------+----------+
|        501 | ABC Traders | 88881111 |
|        502 | XYZ Company | 88882222 |
|        503 | QQ Corp     | 88883333 |
+------------+-------------+----------+

mysql>
mysql> delete from suppliers where supplierID = 502;
ERROR 1451 (23000): Cannot delete or update a parent row: a foreign key constraint fails (`southwind`.`products`, CONSTRAINT `products_ibfk_1` FOREIGN KEY (`supplierID`) REFERENCES `suppliers` (`supplierID`))
mysql>
mysql>
mysql>
mysql>
mysql>

mysql>
mysql> select productID, products.supplierID
    -> from Products, Suppliers
    -> where products.supplierID = suppliers.supplierID;
+-----------+------------+
| productID | supplierID |
+-----------+------------+
|      2001 |        501 |
|      2002 |        501 |
|      2003 |        501 |
|      2004 |        502 |
+-----------+------------+

mysql>
mysql> select * from products;
+-----------+-------------+-----------+----------+-------+------------+
| productID | productCode | name      | quantity | price | supplierID |
+-----------+-------------+-----------+----------+-------+------------+
|      2001 | PEC         | Pencil 3B |      500 |  0.52 |        501 |
|      2002 | PEC         | Pencil 4B |      200 |  0.62 |        501 |
|      2003 | PEC         | Pencil 5B |      100 |  0.73 |        501 |
|      2004 | PEC         | Pencil 6B |      500 |  0.47 |        502 |
+-----------+-------------+-----------+----------+-------+------------+

mysql>
mysql> create view  products_quantity AS
    -> select name, quantity from products;
Query OK, 0 rows affected (0.11 sec)

mysql> show tables;
+---------------------+
| Tables_in_southwind |
+---------------------+
| products            |
| products_quantity   |
| suppliers           |
+---------------------+

mysql>
mysql> select * from products_quantity;
+-----------+----------+
| name      | quantity |
+-----------+----------+
| Pencil 3B |      500 |
| Pencil 4B |      200 |
| Pencil 5B |      100 |
| Pencil 6B |      500 |
+-----------+----------+

mysql> CREATE VIEW products_suppliers AS select productID, products.supplierID, suppliers.name
    ->  from Products, Suppliers
    -> where products.supplierID = suppliers.supplierID;
Query OK, 0 rows affected (0.13 sec)

mysql> show tables;
+---------------------+
| Tables_in_southwind |
+---------------------+
| products            |
| products_quantity   |
| products_suppliers  |
| suppliers           |
+---------------------+

mysql> select * from products_suppliers;
+-----------+------------+-------------+
| productID | supplierID | name        |
+-----------+------------+-------------+
|      2001 |        501 | ABC Traders |
|      2002 |        501 | ABC Traders |
|      2003 |        501 | ABC Traders |
|      2004 |        502 | XYZ Company |
+-----------+------------+-------------+

mysql> select * from products_suppliers  where productID = 2002;
+-----------+------------+-------------+
| productID | supplierID | name        |
+-----------+------------+-------------+
|      2002 |        501 | ABC Traders |
+-----------+------------+-------------+

mysql> select * from products_suppliers  where supplierID = 502;
+-----------+------------+-------------+
| productID | supplierID | name        |
+-----------+------------+-------------+
|      2004 |        502 | XYZ Company |
+-----------+------------+-------------+

mysql> select * from products_suppliers  where supplierID = 501;
+-----------+------------+-------------+
| productID | supplierID | name        |
+-----------+------------+-------------+
|      2001 |        501 | ABC Traders |
|      2002 |        501 | ABC Traders |
|      2003 |        501 | ABC Traders |
+-----------+------------+-------------+

mysql>
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

mysql> SELECT * FROM patients
    ->        WHERE lastVisitDate BETWEEN '2012-09-15' AND CURDATE()
    ->        ORDER BY lastVisitDate;
+-----------+-------+-------------+---------------+---------------+
| patientID | name  | dateOfBirth | lastVisitDate | nextVisitDate |
+-----------+-------+-------------+---------------+---------------+
|      1002 | Kumar | 2011-10-29  | 2012-09-20    | NULL          |
|      1003 | Ali   | 2011-01-30  | 2020-08-14    | NULL          |
+-----------+-------+-------------+---------------+---------------+

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

mysql> SELECT name, lastVisitDate FROM patients
    ->        WHERE TIMESTAMPDIFF(DAY, lastVisitDate, CURDATE()) > 60;
+---------+---------------+
| name    | lastVisitDate |
+---------+---------------+
| Ah Teck | 2012-01-20    |
| Kumar   | 2012-09-20    |
+---------+---------------+

mysql> SELECT name, lastVisitDate FROM patients
    ->        WHERE TO_DAYS(CURDATE()) - TO_DAYS(lastVisitDate) > 60;
+---------+---------------+
| name    | lastVisitDate |
+---------+---------------+
| Ah Teck | 2012-01-20    |
| Kumar   | 2012-09-20    |
+---------+---------------+

mysql> SELECT * FROM patients
    ->        WHERE dateOfBirth > DATE_SUB(CURDATE(), INTERVAL 18 YEAR);
+-----------+-------+-------------+---------------+---------------+
| patientID | name  | dateOfBirth | lastVisitDate | nextVisitDate |
+-----------+-------+-------------+---------------+---------------+
|      1002 | Kumar | 2011-10-29  | 2012-09-20    | NULL          |
|      1003 | Ali   | 2011-01-30  | 2020-08-14    | NULL          |
+-----------+-------+-------------+---------------+---------------+

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

mysql> select now(), curdate(), curtime();
+---------------------+------------+-----------+
| now()               | curdate()  | curtime() |
+---------------------+------------+-----------+
| 2020-08-14 16:12:50 | 2020-08-14 | 16:12:50  |
+---------------------+------------+-----------+

mysql>
+--------------------------------------+
| DATEDIFF('2012-02-01', '2012-01-28') |
+--------------------------------------+
|                                    4 |
+--------------------------------------+

mysql> SELECT DATEDIFF('2012-02-01', '2011-01-28');
+--------------------------------------+
| DATEDIFF('2012-02-01', '2011-01-28') |
+--------------------------------------+
|                                  369 |
+--------------------------------------+

mysql> SELECT TIMESTAMPDIFF(DAY, '2012-02-01', '2012-01-28');
+------------------------------------------------+
| TIMESTAMPDIFF(DAY, '2012-02-01', '2012-01-28') |
+------------------------------------------------+
|                                             -4 |
+------------------------------------------------+

mysql>
FROM COMPANY, CUSTOMER WHERE
COMPANY. CID=CUSTOMER.CID AND

            (a) (–∞, 1]                                           (b) [3, ∞)

            (c) (–∞, 1] U [3, ∞)                                 (d) [1, 3]
changing the temperature?

(a) 3 : 4
(b) 3 : 2
(c) 5 : 1
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

mysql> select * from laptop;
+----+---------------------+--------+---------------+
| Id | Name                | Price  | Purchase_date |
+----+---------------------+--------+---------------+
|  2 | Area 51M            |  60999 | 2019-04-14    |
|  3 | MacBook Pro         | 200499 | 2019-06-20    |
| 10 | Lenovo ThinkPad P71 |  30459 | 2019-08-14    |
+----+---------------------+--------+---------------+
