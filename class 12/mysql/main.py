import mysql.connector

try: 
    connector1=mysql.connector.connect(
        user="surajshukla7656",
        password="shukla",
        host="localhost",
        database="school_management"
    )

except mysql.connector.Error as error:
    print(f"UNABLE TO CONNECT DUE T0 \n {error}")

finally :
    if connector1.isconnected():
        connector1.close()