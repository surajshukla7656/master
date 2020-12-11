import mysql.connector

try:
    connector=mysql.connector.connect(
        host='localhost',
        user='surajshukla7656',
        password='shukla',

    )

    cursor=connector.cursor(dict=True)
    

except:
    pass

# welcome message
def welcome_message():
    print('''WELCOME TO SELF MADE TESTING 
PLATEFORM TO CRACK JEE ADVANCED
MADE BY SURAJSHUKLA 
FOR SURAJSHUKLA.

LETS CRACK IT!''')


#
def full_length_test():
    
    physics_chap=input('Enter physics chapter name:')

    no_of_topics=input('Enter no of topics:')
    No_of_questions=int(input('Enter no of questions present in the chapter:'))

    parameter
    cursor.execute(sql,parameters)
