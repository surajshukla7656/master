''''this program provides different functions to perform 
CRUD in a database'''

import mysql.connector

#trying to connect with the server
try:
    connector=mysql.connector.connect(
        host='localhost',
        username='surajshukla7656',
        password='shukla',
        database='OSIRIS_ELECTRONICS'
    )

    #if connected
    cursor=connector.cursor(dictionary=True)

    print()
    print(F'\033[1;32m{"*"*50} CONNECTION ESTABLISHED SUCCESSFULLY! {"*"*50}\033[1;37m' )
    
except:
    print('UNABLE to connect! TRY AGAIN')


#welcome message

def welcome_message():

    print('''WELCOME!
TO DATABASE MENU INTERFACE 
DEVELOPED BY SURAJ SHUKLA''')


# to highlight data
def color(col=7):

    color=f'\033[1;3{col}m'

    return color


# to highlight data
def separator(num,symbol="*"):

    return symbol*num


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


# to verify and allow access to the authorised user
def verifications():
    
    pass

# program to verify the existing user with his/her user password 
def credential_verifications():

    '''this function accepts registered username and password and verify them from the users table 
    and then allow the access of database'''
       

    username,userpassword=input("Enter username and password:").split()
    #username,userpassword="owner","@123"

    cursor.execute('SELECT USERNAME,USERPASSWORD FROM USERS')

    users=cursor.fetchall()                                                    # an instance containing all usernames and their userpasswords

    for user in users:

        if user["USERNAME"] == username:                                       # checking existence of the user
            

            if user["USERPASSWORD"]==userpassword:                             # verifying password of the user
                  
                print(f'\nlogin successfully as \033[1;33m{username}\033[1;37m \n')

                return username
                break

            else:                                                              # if password not matched 

                print('\nUser Password Does Not Match \n\nAccess Request denied!Try again')

                exit()
                
    else:                                                                      # if user not exist
            
        print(f'\nuser {username} does not exits \n\nAccess Request denied!Try again')

        exit()
    

#function to add users to allow the access of database
def add_new_user(username,userpassword,userid=None):

    try:

        val=(userid,username,userpassword)
        
        cursor.execute('INSERT INTO USERS VALUES(%s,%s,%s)',val)

        connector.commit()
        
        print(f'\nSuccessfully Added! New  USER-{color(6)}{username}{color()}\n')
    except:

        print('\nError! Unable to add new user\n')
    

#show registered users 
def show_users():

    try :
        
        cursor.execute("SELECT USERID,USERNAME FROM USERS")
    
        users=cursor.fetchall()
        
        print(f'\n{separator(51)} THERE ARE {color(6)}{len(users)}{color()} ARE AUTHORISHED USERS {separator(51)}')
            
        for user in users:

            print()

            print(f'''{color(6)}USERID {color()}:{user['USERID']},
{color(6)}USERNAME {color()}:{user['USERNAME']}''')

            print()
        print(separator(137),'\n')
            
    except:

        print('\nOOPs! Something went wrong\n')


# to remove registered users
def remove_user(username):

    try :

        if username=='owner':                                     # restricting to remove root(owner)

            print('Root user can\'t be removed' )

        else:

            val=(username,)

            cursor.execute('DELETE FROM USERS WHERE USERNAME=%s',val)

            connector.commit()
            
            print(f'\nsuccessfully deleted! USERNAME - {color(6)}{username}{color()}\n')

    except:

        print(f'\n{color(6)}{username}{color()}! THIS USER DOES NOT EXIST\n')


# to add new product 
def add_laptop(brand,model_no,processor=None,graphic_card=None,os=None,ram=None,display=None,storage=None,camera=None,battery=None,keyboard=None,other_inputs=None,speakers=None,ports=None,wifi=None,bluetooth=None,weight=None,warranty=None,year_of_release=None,manufacture_in_country=None,stocks=None,price=None,productcode=None,others=None):
    
    try:
        parameters=(productcode,brand,model_no,processor,graphic_card,os,ram,display,storage,camera,battery,keyboard,other_inputs,speakers,ports,wifi,bluetooth,weight,warranty,year_of_release,manufacture_in_country,stocks,price,others)

        query=('INSERT INTO LAPTOP VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)')

        cursor.execute(query,parameters)
        connector.commit()

        print(f'\nSuccessfully Added! \'{color(6)}{brand}-{model_no}{color()}\'\n')

    except:
        print('\nUnable To Add New Product. TRY AGAIN!\n')


# to add more than one product
def add_laptops():

    while True:                                                                                              #loop to enter new product

        detail_dict={'brand':None,'model_no':None,'processor':None,'graphic_card':None,'os':None,'ram':None,'display':None,'storage':None,'camera':None,'battery':None,'keyboard':None,'other_inputs':None,'speakers':None,'ports':None,'wifi':None,'bluetooth':None,'weight':None,'warranty':None,'year_of_release':None,'manufactured_in_country':None,'stocks':None,'price':None,'others':None,'productcode':None}

        for detail in detail_dict:

            var=input(f'\n{color(4)}Enter {detail}:{color()}')
            
            if var=='' and detail=='brand' or var=='' and detail=='model_no' or var=='skip' or var=='stop':  # to skip parameters,break inner loop
                break

            elif var=='':                                                                                    # to keep the parameter None if null 
                var=None
        
            detail_dict[detail]=var                                                                          # adding parameter one by one
        
        if var=='' and detail=='brand' or var=='' and detail=='model_no' or var=='stop':                     #to stop entering new product, break outer loop
            break

        
        # adding new product one by one
        add_laptop(detail_dict['brand'],detail_dict['model_no'],detail_dict['processor'],detail_dict['graphic_card'],detail_dict['os'],detail_dict['ram'],detail_dict['display'],detail_dict['storage'],detail_dict['camera'],detail_dict['battery'],detail_dict['keyboard'],detail_dict['other_inputs'],detail_dict['speakers'],detail_dict['ports'],detail_dict['wifi'],detail_dict['bluetooth'],detail_dict['weight'],detail_dict['warranty'],detail_dict['year_of_release'],detail_dict['manufactured_in_country'],detail_dict['stocks'],detail_dict['price'],detail_dict['others'],detail_dict['productcode'])

    
# to display  laptops
def display(brand=None,model_no=None,processor=None,graphic_card=None,os=None,ram=None,display=None,storage=None,camera=None,battery=None,keyboard=None,other_inputs=None,speakers=None,ports=None,wifi=None,bluetooth=None,weight=None,warranty=None,year_of_release=None,manufacture_in_country=None,stocks=None,price=None,others=None,productcode=None):

        parameters=(productcode,brand,model_no,processor,graphic_card,os,ram,display,storage,camera,battery,keyboard,other_inputs,speakers,ports,wifi,bluetooth,weight,warranty,year_of_release,manufacture_in_country,stocks,price,others)
        
        query='SELECT * FROM LAPTOP WHERE PRODUCTCODE=%s OR BRAND=%s OR MODEL_NO=%s OR PROCESSOR=%s OR GRAPHIC_CARD=%s OR OS=%s OR RAM=%s  OR DISPLAY=%s OR STORAGE=%s OR CAMERA=%s OR BATTERY=%s OR KEYBOARD=%s OR OTHER_INPUTS=%s OR SPEAKERS=%s OR PORTS=%s OR WIFI=%s OR BLUETOOTH=%s OR WEIGHT=%s OR WARRANTY=%s OR YEAR_OF_RELEASE=%s OR MANUFACTURE_IN_COUNTRY=%s OR STOCKS=%s OR PRICE=%s OR OTHERS=%s'

        cursor.execute(query,parameters)

        laptopsDetails=cursor.fetchall()                                                                    # dict containing details of all laptops in dict format 

        for laptop in laptopsDetails:                                                                       # to print laptop details one by one

            print('\n\n\n')
             
            for x,y in laptop.items():

                print(f'''{color(6)}{x}:{color()}{y}''')


# to display all data of all  laptops
def display_all():

    query='SELECT * FROM LAPTOP '

    cursor.execute(query)

    laptopsDetails=cursor.fetchall()                                                                        # dict containing details of all laptops in dict format 

    for laptop in laptopsDetails:                                                                           # contain single laptop detail one by one

        print('\n\n')  

        for x,y in laptop.items():                                                                          # extracting information from the laptop instance one by one

            print(f'''{color(6)}{x}:{color()}{y}''')


# to display only names of product 
def display_products():

    query='SELECT PRODUCTCODE,BRAND,MODEL_NO FROM LAPTOP '

    cursor.execute(query)

    laptopsDetails=cursor.fetchall()                                                                        # dict containing details of all laptops in dict format 

    print(F'TOTAL - {len(laptopsDetails)}\n')

    for laptop in laptopsDetails:                                                                           # contain single laptop detail one by one

        for x,y in laptop.items():                                                                          # extracting information from the laptop instance one by one

            print(f'{color(6)}{x}:{color()}{y}',end='\t')

        print('\n')  



# to update  a single parameter 

def update_s(brand,model_no,parameter,update):

    p_meter=(update,brand,model_no)
    
    query=f'UPDATE LAPTOP SET {parameter}'+'=%s WHERE BRAND=%s AND MODEL_NO=%s'

    cursor.execute(query,p_meter)

    connector.commit()

    print(f'Successfully Updated {brand}-{model_no} to {update}')


# updating specific details of products using productcode

def update():

    print('''UPDATE COMMAND:
ENTER PRODUCT CODE OF PRODUCT FOR UPDATION
s ---> skip
n ---> move to next\n\n''')

    while True:

        parameters=('BRAND','MODEL_NO','PROCESSOR','GRAPHIC_CARD','OS','RAM','DISPLAY','STORAGE','CAMERA','BATTERY','KEYBOARD','OTHER_INPUTS','SPEAKERS','PORTS','WIFI','BLUETOOTH','WEIGHT','WARRANTY','YEAR_OF_RELEASE','MANUFACTURE_IN_RELEASE','STOCKS','PRICE','OTHERS')

        product_code_instance=input(f'{color(4)}Enter productcode:{color()}')

        if product_code_instance=='s':                                                               # enter s to stop further updating and exiting the function

            break

        else:

            for parameter in parameters:

                p_instance=input(f'{color(4)}Enter {parameter}{color()}:')                           # input of parameter to update 

                if p_instance=='n'  or p_instance=='':                                               # skiping and moving on next parameter 

                    continue

                elif p_instance=='s':                                                                 # skipping and moving to next product 

                    break

                else:

                    query=f'UPDATE LAPTOP SET {parameter}=\'{p_instance}\' WHERE PRODUCTCODE=\'{product_code_instance}\''

                    cursor.execute(query)

                    connector.commit()

                    print(f'Successfully Updated! {parameter} of product{product_code_instance} -----> {p_instance}')


# to delete a product completely from the database(not recoverable`)

def delete_p():

    productcode=input(f'\n{color(4)}Enter productcode:{color()}')                         # input of identity of product

    p_code=(productcode,)                                                                 # converting productcode to use it in cursor

    query='SELECT BRAND,MODEL_NO FROM LAPTOP WHERE PRODUCTCODE=%s'

    cursor.execute(query,p_code)

    extra_details=cursor.fetchall()

    if len(extra_details)!=0:                                                              # if product exist

        extra_details=list(extra_details[0].values())                                      # retrieving useful data 

        print(f'\nWARNING! NOT RECOVERABLE AFTER DELETION\n')
        
        confirm=input(f'{color(4)}Are You Sure You Want To  Delete(Y/n){color()} \'{productcode}-{extra_details[0]}-{extra_details[1]}\' {color(4)}:{color()}')

        if confirm=='y' or confirm=='yes':

            query='DELETE FROM LAPTOP WHERE PRODUCTCODE=%s'

            cursor.execute(query,p_code)

            connector.commit()

            print(f'\nSuccessfully Deleted - {productcode}-{extra_details[0]}-{extra_details[1]}')

        elif confirm=='n' or confirm=='no':

            print('\nNot Deleted!')

        else:

            print('\nUnkown Input!')

    else:

        print('\nOops! Product Not Exist')


# adding a new purchase made 

def new_purchase():
    
    purchase_parameter_dict={
    'CUSTOMERNAME':None,
    'CUSTOMEREMAILID':None,
    'PRODUCTS':None,
    'AMOUNTPAYED':None,
    'AMOUNTLEFT':None
    }

    for parameter in purchase_parameter_dict:

        detail=input(f'{color(4)}Enter {parameter}{color()}:')

        if parameter=='AMOUNTPAYED' or parameter=='AMOUNTLEFT':

            detail=int(detail)

        purchase_parameter_dict[parameter]=detail
    
    parameters=purchase_parameter_dict.values()
    p
    parameters=tuple(parameters)
    print(parameters)

    
    query='INSERT INTO PURCHASES VALUES(null,%s,%s,%s,%s,%s)'

    #query=f'INSERT INTO PURCHASES VALUES(null,\'{parameters[0]}\',\'{parameters[1]}\',\'{parameters[2]}\',\'{parameters[3]}\',\'{parameters[4]}\')'

    cursor.execute(query,parameters)

    connector.commit()

    print(f'Successfully Recorded New Purchase,PurchaseID-')


#showing all purchases made
def all_purchases():
    
    query='SELECT * FROM PURCHASES'

    cursor.execute(query)

    purchases=list(cursor.fetchall())

    for purchase in purchases:                                                                                # contain single purchase detail one by one

        print('\n\n')  

        for x,y in purchase.items():                                                                          # extracting information from the purchase instance one by one

            print(f'''{color(6)}{x}:{color()}{y}''')


def help():

    f=open('/home/surajshukla7656/Documents/nextpython/nextprojects/PROJECT_OSIRIS/README','r')

    for line in f.readlines():

        print(line,end='')
   
if __name__=='__main__':
    add_laptop('HP','THINKPAD','10TH GEN INTEL CORE i8','INTEL UHD','WINDOWS 10 HOME','LPDDR4 4GB','16 INCH FULL HD+ ','512 SSD','5MP WEBCAM','8 HOURS BACKUP','BACKLIGHT KEYS MAGIC KEYBOARD','MIC','DOLBY MODE','2 USB 1 USB TYPE-C','10','5','2 KG','1 YEAR','2020','INDIA',34,29999)
    #day(brand='LENOVO')
    add_laptops()
    pass