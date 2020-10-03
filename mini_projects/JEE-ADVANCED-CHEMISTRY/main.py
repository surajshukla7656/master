import mysql.connector

connector=mysql.connector.connect(
    host='localhost',
    user='surajshukla7656',
    password='shukla',
    database='JEE_ADVANCED_CHEMISTRY'

)

cursor=connector.cursor()


# welcome message
def welcome_message():
    print('''\n\nWELCOME TO 
JEE-ADVANCED-ORGANIC PRACTICE DATABASE 
CREATED BY SURAJSHUKLA\n\n''')

# to highlight data
def color(col=7):

    color=f'\033[1;3{col}m'

    return color


#
def new():

    #adding new chapter
    chapter_no=int(input('Enter chapter_no:'))

    chapter_name=input('Enter chapter name :') 

    cursor.execute('show tables')

    chapters=cursor.fetchall()                                                        # list containing all chapters

    level=input('Enter level:')                                                       # level of questions

    no_of_questions=int(input('Enter no of questions:'))                                   # no of questions in that level

    # if the chapter already exit then adding new levels
    if chapter_name in chapters==True:

        sql=f'''
            ALTER TABLE {chapter_name}
            ADD COLUMN LEVEL_{level} INT NOT NULL,
            ADD COLUMN CORRECT_ANSWER_{level} VARCHAR(5),
            ADD COLUMN MY_ANSWER_{level} VARCHAR(5),
            ADD COLUMN CONCLUSION_{level} VARCHAR(10)
            ADD COLUMN OTHERS_{level} VARCHAR(40)
            '''

    # if the chapter_name does not exit adding new chapter_name
    else:

        cursor.execute(f'INSERT INTO ALL_CHAPTERS VALUES({chapter_no},\'{chapter_name}\')')
        connector.commit()

        sql=f'''
            CREATE TABLE {chapter_name}(
            LEVEL_{level} INT NOT NULL,
            CORRECT_ANSWER_{level} VARCHAR(5),
            MY_ANSWER_{level} VARCHAR(5),
            CONCLUSION_{level} VARCHAR(10),
            OTHERS_{level} VARCHAR(40)   
            )'''
  

    # query
    cursor.execute(sql)
    connector.commit()


    # adding questions with answers
    for i in range(1,no_of_questions+1):

        answer=input(f'\n{color(4)}Enter correct answer of question-{i}:{color()}')

        sql=F'INSERT INTO {chapter_name}(LEVEL_{level},CORRECT_ANSWER_{level}) VALUES({i},\'{answer}\')'

        cursor.execute(sql)
        
        connector.commit()

   
    # to re-verify
    cursor.execute(f'SELECT LEVEL_{level},CORRECT_ANSWER_{level} FROM {chapter_name}')

    answer_keys=cursor.fetchall()

    for i in answer_keys:
        print(f'question-{i[0]}:{i[1]}')

        correct_answer=input("Correct Answer: ")

        if correct_answer=='':
            continue

        else:
            cursor.execute(F'UPDATE {chapter_name} SET CORRECT_ANSWER_{level}=\'{correct_answer}\' WHERE LEVEL_{level}={i[0]}')
            connector.commit()

            corrected=cursor.fetchone()
            print('\nCorrected\n\n')
            

    print('\nNew Chapter Added Successfully!\n')


# to start the practice session
def start(chapter_no=None,chapter_name=None,level=None,start_from_question_number=None):
    print(start_from_question_number)

    if chapter_no==None:
        # to select chapter to start 
        chapter_no=int(input('\nEnter chapter number:'))

        cursor.execute(f'SELECT CHAPTERNAME FROM ALL_CHAPTERS WHERE CHAPTERNO={chapter_no}')

        chapter_name=cursor.fetchone()
        chapter_name=chapter_name[0]
        print(chapter_name)
        
        if chapter_name==None:
            print('\n\nChapter Does Not Exit! Please Add It.')

        else:
            level=input('\nEnter level:')

            start_from_question_number=int(input('\nStart From: '))
        
    else:
        pass

        
    # creating answer key buffer
    cursor.execute(F'SELECT * FROM {chapter_name}')

    answer_key=cursor.fetchall()

    # to give answer
    while True:

        # input of answer
        your_ans=input(f'\n{color(4)}Enter your answer of question number-{start_from_question_number}:{color()}')

        if your_ans=='s':
            cursor.execute('DELETE FROM CURRENT')

            cursor.execute(f'INSERT INTO CURRENT VALUES({chapter_no},\'{chapter_name}\',\'{level}\',{start_from_question_number})')
            connector.commit()

            break
        # if correct 
        elif your_ans==answer_key[start_from_question_number-1][1]:

            print('\nCORRECT ANSWER\n')

            cursor.execute(f'UPDATE {chapter_name} SET MY_ANSWER_{level}=\'{your_ans}\',CONCLUSION_{level}=\'CORRECT\' WHERE LEVEL_{level}={answer_key[start_from_question_number-1][0]}')

            connector.commit()

        # if wrong
        else:

            print('\nINCORRECT ANSWER\n')

            decision=input('Want To See Solution:')

            if decision=='y':

                # correct answer
                print(F'Correct Answer is - {answer_key[start_from_question_number-1][1]}')
                
                # other information
                others=input('\nEnter others:\n')

                cursor.execute(f'UPDATE {chapter_name} SET OTHERS_{level}=\'{others})\' WHERE LEVEL_{level}={answer_key[start_from_question_number-1][0]}')
                connector.commit()

            else:
                continue

        start_from_question_number+=1    

# to show all added chapters
def chapters():
    cursor.execute('SELECT * FROM ALL_CHAPTERS')

    chapters=cursor.fetchall()

    for chapter in chapters:
        print(f'\nchapter no-{chapter[0]},chapter name-{chapter[1]}\n')
        
        
# to resume journey
def resume():
    cursor.execute('SELECT * FROM CURRENT')

    resumed=cursor.fetchall()

    print(resumed)

    start(resumed[0][0],resumed[0][1],resumed[0][2],resumed[0][3])

# to see current progress
def current():
    cursor.execute('SELECT * FROM CURRENT')

    resumed=cursor.fetchall()

    if len(resumed)==1:
        print(resumed)
        print(f'''\nChapter no:{resumed[0][0]},
Chapter_name:{resumed[0][1]},
Level:{resumed[0][2]},
Question no:{resumed[0][3]}\n''')

    else:
        print('\nNo Information\n')


   

    