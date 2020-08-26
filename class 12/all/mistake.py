D:\>start /b mysqld

D:\>mysql -u user1 -h localhost   -p
Enter password: *******
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 2
Server version: 5.7.31 MySQL Community Server (GPL)

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

g4) SELECT PNAME, SNAME
FROM PRODUCTS P, SUPPLIERS S WHERE E SUPCODE = S. SUPCODE
AND QTY>100;

(a) 220 Ω
(b) 110 Ω
(c) 55 Ω
(d) 13.75 Ω

 (a) is equal to 5                        (b) is equal to 3

 (c) is equal to 7                       (d) does not exist
A → B proceeds virtually to the end. Determine: 
(a) the sign of ΔS of the reaction; 
(b) the sign of ΔG for the reaction B → A at the temperature T
(c) the possibility of the reaction B → A proceeding at low temperatures.
B:-G=-ve
C:- ?
(B) -ve
(C) yes ! , It can proceed

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

mysql>
o	To display all DepName along with the DepCde in descending order of DepCde.
o	To display the average age of Employees in DepCde as 103.
o	To display the name of DepHead of the Employee named “Sanjeev P”
o	To display the details of all employees who has joined before 2007 from EMPL¬OYEE table.
(b)	Give the output of the following SQL queries: 
o	SELECT COUNT (DISTINCT DepCde) FROM EMPLOYEE;
o	SELECT MAX(JoinDate), MIN (JointDate) FROM EMPLOYEE;
o	SELECT TName, DepHead FROM EMPLOYEE E, DEPARTMENT D
WHERE E.DepCde = D.DepCde;
o	SELECT COUNT (*) FROM EMPLOYEE WHERE Salary > 60000 AND Age > 30;
(a) 0.0012 /°C
(b) 0.0024 /°C
(c) 0.0032 /°C
(d) 0.0064 /°C

(a) Increasing
(b)   Decreasing
(c) Neither increasing nor decreasing
(d) None of these
the standard change in enthalpy ΔH°(298) of formation of CuO.

