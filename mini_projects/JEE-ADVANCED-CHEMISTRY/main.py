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
    
    # 0 - black
    # 1 - red
    # 2 - light green
    # 3 - yellow
    # 4 - blue
    # 5 - magenta
    # 6 - light blue 
    
    color=f'\033[1;3{col}m'

    return color


 # to modifying input command
def operator_manager(command):

    prompt=""

    # replacing space by underskore
    for char in command:

        if char==" ":
        
            prompt+="_"
        
        else:
        
            prompt+=char

    # add parentheses at the end if absent
    if "(" and ")" not in prompt:

        prompt+="()"
    
    command=prompt.lower()

    return command


# enter a new chapter-solution record

def new(fast=False):

    #adding new chapter
    chapter_number=int(input(f'{color(2)}Enter chapter_number : {color()}'))

    chapter_name=input(f'{color(2)}Enter chapter name : {color()}') 
 
    chapter_name=chapter_name.upper()                                                                      # converting into upper case

    cursor.execute('SHOW TABLES')

    chapters=cursor.fetchall()                                                                             # list containing all chapters

    level=input(f'{color(4)}Enter level :{color()}')                                                       # level of questions

    no_of_questions=int(input(f'{color(4)}Enter no of questions :{color()}'))                              # no of questions in that level

    # if the chapter already exit then adding new levels
    if chapter_name in chapters==True:

        sql=f'''
            ALTER TABLE {chapter_name}
            ADD COLUMN QUESTION_NUMBER_LEVEL_{level} INT NOT NULL,
            ADD COLUMN CORRECT_ANSWER_{level} VARCHAR(5),
            ADD COLUMN MY_ANSWER_{level} VARCHAR(5),
            ADD COLUMN STATUS_{level} VARCHAR(10)
            ADD COLUMN NOTE_{level} VARCHAR(40)
            '''

    # if the chapter_name does not exit adding new chapter_name
    else:

        sql=f'''
            CREATE TABLE {chapter_name}(
            QUESTION_NUMBER_LEVEL_{level} INT NOT NULL,
            CORRECT_ANSWER_{level} VARCHAR(5),
            MY_ANSWER_{level} VARCHAR(5),
            STATUS_{level} VARCHAR(10),
            NOTE_{level} VARCHAR(40)   
            )'''
  

    # query
    cursor.execute(sql)
    connector.commit()


    # adding questions with answers
    for i in range(1,no_of_questions+1):

        answer=input(f'\n{color(3)}Enter correct answer of question-{i}:{color()}')

        sql=f'INSERT INTO {chapter_name}(LEVEL_{level},CORRECT_ANSWER_{level}) VALUES({i},\'{answer}\')'

        cursor.execute(sql)
        
        connector.commit()

    # to re-verify
    if fast==False:
        cursor.execute(f'SELECT LEVEL_{level},CORRECT_ANSWER_{level} FROM {chapter_name}')

        answer_keys=cursor.fetchall()

        for i in answer_keys:

            print(f'{color(2)}question-{i[0]} :{i[1]}{color()}')

            correct_answer=input(f"{color(6)}\nCorrect Answer :{color()} ")

            if correct_answer=='':
                continue

            else:
                cursor.execute(F'UPDATE {chapter_name} SET CORRECT_ANSWER_{level}=\'{correct_answer}\' WHERE LEVEL_{level}={i[0]}')
                connector.commit()

                corrected=cursor.fetchone()
                print('\nCorrected\n')

    
    elif fast==True:

        cursor.execute(f'SELECT LEVEL_{level},CORRECT_ANSWER_{level} FROM {chapter_name}')

        answer_keys=cursor.fetchall()                                                               # tuple containing answers with question number

        for question_number in answer_keys:                                                         # printing all questions with answers

            print(f'{color(2)}question-{question_number[0]} :{question_number[1]}{color()}')

        # for correction
        while True:

            question_number,correct_answer=input(f"{color(6)}\nQuestion Number And Correct Answer :{color()} ").split()

            # to exit
            if question_number=="exit":
            
                break

            cursor.execute(F'UPDATE {chapter_name} SET CORRECT_ANSWER_{level}=\'{correct_answer}\' WHERE LEVEL_{question_number}')

            connector.commit()

            corrected=cursor.fetchone()

            print(f'\nCorrected! To {corrected}\n')
    
        record_manager(chapter_number,chapter_name,no_of_questions)

        print(f'\nNew Chapter Added Successfully! CHAPTER NUMBER : {chapter_number} , CHAPTERNAME : {chapter_name}\n')


def correction(chapter_number,level):

    # chapter_number=input(f'{color(2)}Enter chapter number : {color()}')

    # level=input(f'{color(2)}Enter level : {color()}')

    cursor.execute(f'SELECT CHAPTERNAME FROM PROGRESS_REPORT WHERE CHAPTERNUMBER={chapter_number}')

    chapter_name=cursor.fetchone()

    cursor.execute(f'SELECT LEVEL_{level},CORRECT_ANSWER_{level} FROM {chapter_name}')

    answer_keys=cursor.fetchall()                                                               # tuple containing answers with question number

    for question_number in answer_keys:                                                         # printing all questions with answers

        print(f'{color(2)}{question_number[0]} :{question_number[1]}{color()}',end=' ')

    while True:

        question_number,correct_answer=input(f"{color(6)}\nQuestion Number And Correct Answer :{color()} ").split()

        # to exit
        if question_number=="exit":
        
            break
        
        else:
            cursor.execute(F'UPDATE {chapter_name} SET CORRECT_ANSWER_{level}=\'{correct_answer}\' WHERE LEVEL_{question_number}')

            connector.commit()

            corrected=cursor.fetchone()

        print(f'Corrected! - {corrected} ')


# to start the practice session
def start(chapter_number=None,chapter_name=None,level=None,start_from_question_number=None):

    if chapter_number==None:

        # to select chapter to start 
        chapter_number=int(input(f'\n{color(2)}Enter chapter number :{color()}'))

        cursor.execute(f'SELECT CHAPTERNAME FROM PROGRESS_REPORT WHERE CHAPTERNO={chapter_number}')

        chapter_name=cursor.fetchone()

        chapter_name=chapter_name[0]

        print(f'\n{color(4)}CHAPTER NAME{color()} : ',chapter_name)
        
        if chapter_name==None:

            print('\n\nChapter Does Notprevious_report[0][6]- Exit! Please Add It.')

        else:

            level=input(F'\n{color(2)}Enter level :{color()} ')

            start_from_question_number=int(input(f'\n{color(2)}Start From :{color()} '))
        
    else:
        pass
    
    # creating previous report buffer

    cursor.execute(f'SELECT * FROM PROGRESS_REPORT WHERE CHAPTERNUMBER={chapter_number}')

    previous_report=cursor.fetchall()
    previous_report=list(previous_report)

        
    # creating answer key buffer
    cursor.execute(F'SELECT * FROM {chapter_name}')

    answer_key=cursor.fetchall()

    # to give answer
    while True:

        # input of answer
        your_ans=input(f'\n{color(6)}Enter your answer of question number-{start_from_question_number}:{color()}')

        if your_ans=='exit':

            break

        # if skipped
        elif your_ans=='s' or your_ans=='skip':

            cursor.execute(f'UPDATE {chapter_name} SET STATUS_{level}=\'SKIPPED\' WHERE QUESTION_NUMBER_LEVEL_1={answer_key[start_from_question_number-1][0]}')

            connector.commit()

            print(f'--------->>> {color(4)}SKIPPED{color()}')

            start_from_question_number+=1  

            continue
        
        # to move on previous problem
        elif your_ans=='p':

            start_from_question_number-=1  

            continue
        
        # to enter note in previous question
        elif your_ans=='pn':

            start_from_question_number-=1  

            # other information
            notes=input(f'\n--->{color(6)} Enter Notes : {color(6)}')

            cursor.execute(f'UPDATE {chapter_name} SET OTHERS_{level}=\'{notes})\' WHERE QUESTION_NUMBER_LEVEL_1={answer_key[start_from_question_number-1][0]}')

            print(f'--------->>> {color(4)}ADDED{color()}')

            start_from_question_number+=1

            continue

        # if correct 
        elif your_ans==answer_key[start_from_question_number-1][1]:

            print(f'--------->>> {color(4)}CORRECT ANSWER{color()}\n')

            cursor.execute(f'UPDATE {chapter_name} SET MY_ANSWER_{level}=\'{your_ans}\',STATUS_{level}=\'CORRECT\' WHERE QUESTION_NUMBER_LEVEL_1={answer_key[start_from_question_number-1][0]}')

            connector.commit()

        # if wrong
        else:

            print(f'--------->>> {color(1)}INCORRECT ANSWER\n{color()}')

            decision=input(f'{color(6)}--------->>> Want To See Solution:{color()}')

            if decision=='y':                # correct answer
                print(F'\n--->{color(4)} Correct Answer is - {color()}{answer_key[start_from_question_number-1][1]}')
                
                # other information
                notes=input(f'\n--->{color(6)} Enter Note:{color(6)}')

                cursor.execute(f'UPDATE {chapter_name} SET STATUS_{level}=\'INCORRECT\' ,NOTE_{level}=\'{notes})\' WHERE QUESTION_NUMBER_LEVEL_1={answer_key[start_from_question_number-1][0]}')
                
                connector.commit()

            # to exit
            elif decision=="exit":
                 
                cursor.execute('DELETE FROM CURRENT')

                cursor.execute(f'INSERT INTO CURRENT VALUES({chapter_number},\'{chapter_name}\',\'{level}\',{start_from_question_number})')
          
                connector.commit()

                break
                

            else:
                continue

        start_from_question_number+=1  

    # to update current record

    cursor.execute('DELETE FROM CURRENT')

    cursor.execute(f'INSERT INTO CURRENT VALUES({chapter_number},\'{chapter_name}\',\'{level}\',{start_from_question_number})')

    connector.commit()

    # to update progress report 
    
    progress_report_manager(chapter_number,start_from_question_number,previous_report)


# to show all added chapters
def show_chapters():

    cursor.execute('SELECT CHAPTERNAME FROM PROGRESS_REPORT')

    chapters=cursor.fetchall()

    for chapter in chapters:
        print(f'{color(4)}\nchapter no -{color()}{chapter[0]} , {color(4)}chapter name-{color()}{chapter[1]}\n')
        
        
# to resume journey
def resume():

    cursor.execute('SELECT * FROM CURRENT')

    resumed=cursor.fetchall()

    current()

    start(resumed[0][0],resumed[0][1],resumed[0][2],resumed[0][3])

# to see current progress
def current():

    cursor.execute('SELECT * FROM CURRENT')

    resumed=cursor.fetchall()

    if len(resumed)==1:

        print(f'''\n{color(4)}Chapter no:{color()}{resumed[0][0]},
{color(4)}Chapter_name:{color()}{resumed[0][1]},
{color(4)}Level:{color()}{resumed[0][2]},
{color(4)}Question no:{color()}{resumed[0][3]}\n''')

    else:
        print('\nNo Information\n')


# records the new added chapter
def record_manager(chapter_number,chapter_name,total_questions_level_1):

    parameter=(chapter_number,chapter_name)

    query='INSERT INTO PROGRESS_RECORD(CHAPTERNUMBER,CHAPTERNAME,TOTAL_QUESTIONS_LEVEL_1) VALUES(%s,%s,%s)'

    cursor.execute(query,parameter)

    connector.commit()

    print('Added Successfully! ')


# progress manager
def progress_report_manager(chapter_number,current_question,previous_report):
    
    cursor.execute(f'SELECT CHAPTERNAME FROM PROGRESS_REPORT WHERE CHAPTERNUMBER={chapter_number}')

    chapter_name=cursor.fetchall()

    if len(chapter_name)==0:

        print('Oops! Chapter not found')

    else:

        chapter_name=chapter_name[0][0]

        # total questions
        cursor.execute(f'SELECT COUNT(*) FROM {chapter_name}')

        total_questions=cursor.fetchone()
        total_questions=total_questions[0]

        # attempted questions
        cursor.execute(f'SELECT COUNT(*) FROM {chapter_name} WHERE STATUS_1 IS NOT NULL')

        attempted_questions=cursor.fetchone()
        attempted_questions=attempted_questions[0]

        # non-attempted questions
        cursor.execute(f'SELECT COUNT(*) FROM {chapter_name} WHERE STATUS_1 IS NULL')

        non_attempted_questions=cursor.fetchone()
        
        non_attempted_questions=non_attempted_questions[0]

        # wrong and skipped questions
        cursor.execute(f'SELECT COUNT(*) FROM {chapter_name} WHERE STATUS_1=\'INCORRECT\' OR STATUS_1=\'SKIPPED\'')

        wrong_and_skipped_questions=cursor.fetchone()
        
        wrong_and_skipped_questions=wrong_and_skipped_questions[0]

        # correct  questions
        correct_questions=attempted_questions-wrong_and_skipped_questions

        # status
        cursor.execute(f'SELECT COUNT(*) FROM {chapter_name} WHERE STATUS_1=\'CORRECT\'')

        status=cursor.fetchone()

        status=status[0]

        # bookmarks
        cursor.execute(f'SELECT QUESTION_NUMBER_LEVEL_1 FROM {chapter_name} WHERE NOTE_1 IS NOT NULL')

        bookmarks=cursor.fetchall()

        bookmarks_str=''

        for i in bookmarks:

            bookmarks_str=bookmarks_str+str(i[0])+', '

        # update 
        query='UPDATE PROGRESS_REPORT SET ATTEMPTED_QUESTIONS_LEVEL_1=%s,NON_ATTEMPTED_QUESTIONS_LEVEL_1=%s,CORRECT_QUESTIONS_LEVEL_1=%s,WRONG_OR_SKIPPED_QUESTIONS_LEVEL_1=%s,BOOKMARKED_QUESTIONS_LEVEL_1=%s,CURRENT_QUESTION_NUMBER=%s WHERE CHAPTERNUMBER=%s'

        p_meter=(attempted_questions,non_attempted_questions,correct_questions,wrong_and_skipped_questions,bookmarks_str,current_question,chapter_number)

        cursor.execute(query,p_meter)

        connector.commit()

        # display update report 
        print(f'\n{color(2)}Progress Report Of Chapter Number {color()}: {chapter_number}, Chapter Name : {chapter_name} Updated!\n')

        # display today report 
        print(f'''{color(2)}SESSION REPORT : {color()}
        
    {color(4)}CORRECT ANSWERS : {color()}{correct_questions-previous_report[0][5]},
    {color(4)}WRONG OR SKIPPED ANSWERS: {color()}{wrong_and_skipped_questions-previous_report[0][6]},
    {color(4)}TOTAL QUESTIONS ATTEMPTED : {color()}{previous_report[0][4]-non_attempted_questions}\n\n\n''')

        progress(chapter_number)


# to show progress report of a chapter
def progress(chapter_number):

    cursor.execute(f'SELECT * FROM PROGRESS_REPORT WHERE CHAPTERNUMBER={chapter_number}')

    # extracting progress report 
    progress_report=cursor.fetchall()

    print(f'''{color(3)}CHAPTER {chapter_number} REPORT :
    
    {color(4)}CHAPTER NAME : {color()}{progress_report[0][1]},
    {color(4)}TOTAL QUESTIONS : {color()}{progress_report[0][2]},
    {color(4)}ATTEMPTED QUESTIONS : {color()}{progress_report[0][3]},
    {color(4)}NON ATTEMPTED QUESTIONS : {color()}{progress_report[0][4]},
    {color(4)}CORRECT QUESTIONS : {color()}{progress_report[0][5]}
    {color(4)}WRONG AND SKIPPED QUESTIONS {color()}: {progress_report[0][6]},
    {color(4)}CURRENT QUESTION : {color()}{progress_report[0][8]},
    {color(4)}BOOKMARKS QUESTION : {color()}{progress_report[0][7]}\n''')


# master key to run any command
def master_key():

    master_command=input(f'\n{color(2)}Enter Master Command :{color()} ')

    cursor.execute(master_command)

    master_output=cursor.fetchall()

    connector.commit()

    count=0
    
    if len(master_output)!=0:

        for row in master_output:
            
            count+=1

            print(f'{color(4)}row{count} : {color()}{row}\n')

    elif len(master_output)==0:

        print('No Output')

    else:

        print('Anonymous')

if __name__=="__main__":
    pass