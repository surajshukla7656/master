''''this program provides different functions to perform 
CRUD in a database'''
# imported modules
import datetime

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
    print(F'\033[1;32m{"*"*10} CONNECTION ESTABLISHED SUCCESSFULLY! {"*"*10}\033[1;37m' )
    
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

    # modification

    if command=='del':

        prompt='delete_products()'

    elif command[:4]=='del-':
        
        prompt=f'delete_products({command[4:]})'

    else:
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



'''----------------------------------------------------- CREATE ----------------------------------------------------'''

# to add new product 
def add_laptop(brand,model_no,processor=None,graphic_card=None,os=None,ram=None,display=None,storage=None,camera=None,battery=None,keyboard=None,other_inputs=None,speakers=None,ports=None,wifi=None,bluetooth=None,weight=None,warranty=None,year_of_release=None,manufacture_in_country=None,stocks=None,price=None,productcode=None,others=None):
    
    try:

        # converting all parameters into upper case
        parameters=[productcode,brand,model_no,processor,graphic_card,os,ram,display,storage,camera,battery,keyboard,other_inputs,speakers,ports,wifi,bluetooth,weight,warranty,year_of_release,manufacture_in_country,stocks,price,others]

        for val in range(len(parameters)):

            parameters[val]=parameters[val].upper()

        parameters=tuple(parameters)


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

            var=var.upper()                                                                                  # converting into upper case
            
            if var=='' and detail=='brand' or var=='' and detail=='model_no' or var=='SKIP' or var=='STOP':  # to skip parameters,break inner loop
               
                break

            elif var=='':                                                                                    # to keep the parameter None if null 
                
                var=None
        
            detail_dict[detail]=var                                                                          # adding parameter one by one
        
        if var=='' and detail=='brand' or var=='' and detail=='model_no' or var=='STOP':                     #to stop entering new product, break outer loop
            
            break

        
        # adding new product one by one
        add_laptop(detail_dict['brand'],detail_dict['model_no'],detail_dict['processor'],detail_dict['graphic_card'],detail_dict['os'],detail_dict['ram'],detail_dict['display'],detail_dict['storage'],detail_dict['camera'],detail_dict['battery'],detail_dict['keyboard'],detail_dict['other_inputs'],detail_dict['speakers'],detail_dict['ports'],detail_dict['wifi'],detail_dict['bluetooth'],detail_dict['weight'],detail_dict['warranty'],detail_dict['year_of_release'],detail_dict['manufactured_in_country'],detail_dict['stocks'],detail_dict['price'],detail_dict['others'],detail_dict['productcode'])




'''----------------------------------------------------- RETRIEVE ----------------------------------------------------'''
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

    query='SELECT * FROM LAPTOP'

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

def stocks(productcode='all'):

    if productcode=='all' or productcode=='ALL':

        query='SELECT PRODUCTCODE,BRAND,MODEL_NO,STOCKS FROM LAPTOP'

    else:
    
        query=f'SELECT PRODUCTCODE,BRAND,MODEL_NO,STOCKS FROM LAPTOP WHERE PRODUCTCODE={productcode}'

    cursor.execute(query)

    laptop_stocks=cursor.fetchall()

    for stocks in laptop_stocks:                                                                           # contain single laptop detail one by one

        print('\n\n')  

        for x,y in stocks.items():                                                                          # extracting information from the laptop instance one by one

            print(f'''{color(6)}{x}:{color()}{y}''')


'''----------------------------------------------------- UPDATE ----------------------------------------------------'''

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

# updating stocks

def update_stocks(productcode,new_stocks):

    query='UPDATE LAPTOP SET STOCKS=%s WHERE PRODUCTCODE=%s'
    
    p_meter=(new_stocks,productcode)

    cursor.execute(query,p_meter)

    connector.commit()

    print('Updated Successfully!')


'''----------------------------------------------------- DELETE ----------------------------------------------------'''


# to delete a product completely from the database(not recoverable`)

def delete_products(productcode=None,many=False):

    if productcode==None:

        many=True

    while True : 

        if productcode=='show products':

            display_products()

        elif productcode!=None:
    
            p_code=(productcode,)                                                                 # converting productcode to use it in cursor

            query='SELECT BRAND,MODEL_NO FROM LAPTOP WHERE PRODUCTCODE=%s'

            cursor.execute(query,p_code)

            extra_details=cursor.fetchall()

            if len(extra_details)!=0:                                                              # if product exist

                extra_details=list(extra_details[0].values())                                      # retrieving useful data 

                print(f'\nWARNING! NOT RECOVERABLE AFTER DELETION\n')
                
                confirm=input(f'{color(4)}Are You Sure You Want To  Delete(Y/n){color()} \'{productcode}-{extra_details[0]}-{extra_details[1]}\'{color(4)} : {color()}')

                if confirm=='y' or confirm=='yes':

                    query='DELETE FROM LAPTOP WHERE PRODUCTCODE=%s'

                    cursor.execute(query,p_code)

                    connector.commit()

                    print(f'\nSuccessfully Deleted - {productcode}-{extra_details[0]}-{extra_details[1]}')

                elif confirm=='n' or confirm=='no':

                    print('\nNot Deleted!')

                elif confirm=='exit':

                    break

                else:

                    print('\nUnkown Input!')

            else:

                print('\nOops! Product Not Exist')

        # if only one product is to delete
        if many==False:
            break
            
        productcode=input(f'\n{color(4)}Enter productcode:{color()}')                         # input of identity of product

        if productcode=='exit':
            
            break

        



'''----------------------------------------------------- CUSTOMER ----------------------------------------------------'''

# adding a new purchase made 

def new_purchase(customername=None,customeremail=None,customerphone=None):
     
    if customername==None:

        fields=['customer name','customer email ID','phone no.','product code','discount(in %)','GST(IN %)']

        parameters=list()

    else:
        fields=['product code','discount(in %)','GST(IN %)']

        parameters=list([customername,customeremail,customerphone])

    i=0

    while i<len(fields):

        detail=input(f'\n{color(4)}Enter {fields[i]}{color()} : ')

        if detail=='p':

            if i>0:

                i-=1

                parameters.pop()

                continue

            else:
                
                print(f'{color(1)}\nWarning! i is less than 0{color()}')

        elif fields[i]=='product code':

            if detail.isdigit()==True:
            
                cursor.execute(f'SELECT BRAND,MODEL_NO,STOCKS,PRICE FROM LAPTOP WHERE PRODUCTCODE={detail}')

                details=cursor.fetchall()

                if len(details)!=0:

                    product=details[0]['BRAND']+'-'+details[0]['MODEL_NO']

                    print(f'-------->>>{color(4)} Product name {color()}: {product}')

                    parameters.append(detail)

                    parameters.append(product)

                    parameters.append(float(details[0]['PRICE']))

                    i+=1

                else:
                    
                    print('\n-------->>>Product Not Found(Only five digits code)')

            else:

                print('\n-------->>>Please! Enter Product code(Only in int(5))')

            continue

        elif fields[i]=='customer name' and detail=='':

            print('\n-------->>>Customer Name Can\'t Be Empty')

            continue

        elif fields[i]=='customer email ID' and 'mail.com' not in detail and '@' not in detail :

            print('\n-------->>>Invalid Email!')

            continue

        elif fields[i]=='discount(in %)':

            if detail=='':

                detail=int()

            discount_price=float(details[0]['PRICE'])*(float(detail) * 0.01)

            amount_after_applying_discount=int(details[0]['PRICE'])-discount_price

        elif fields[i]=='GST(IN %)':
            
            if detail=='':

                detail=int()
                
            GST_price=amount_after_applying_discount*(float(detail) * 0.01)

            amount_after_applying_gst=amount_after_applying_discount+GST_price

        elif fields[i]=='phone no.' :

            if detail=='':

                parameters.append(int())

            elif detail.isdigit()==False:

                print('\n-------->>>Invalid Input')
                
                continue

            elif len(detail)!=10:

                print('\n-------->>>Only ten digit numbers are allowed')

                continue

            else:

                parameters.append(None)

            i+=1

            continue
        
        # adding
        parameters.append(detail)

        i+=1

    parameters.append(amount_after_applying_gst)

    parameters.append(datetime.datetime.today())

    parameters.append(datetime.datetime.today())

    parameters=tuple(parameters)

    query='INSERT INTO PURCHASES VALUES(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

    # #query=f'INSERT INTO PURCHASES VALUES(null,\'{parameters[0]}\',\'{parameters[1]}\',\'{parameters[2]}\',\'{parameters[3]}\',\'{parameters[4]}\')'

    cursor.execute(query,parameters)

    connector.commit()

    cursor.execute('SELECT PURCHASEID,NET_AMOUNT_PAID,DATE_OF_PURCHASE,TIME_OF_PURCHASE FROM PURCHASES ORDER BY PURCHASEID DESC LIMIT 1 ')

    purchasedetail=cursor.fetchone()

    print(f'''\n------->>>Successfully Added!
------->>>{color(4)}PurchaseID{color()} : {purchasedetail['PURCHASEID']}, {color(4)}NET AMOUNT {color()}:{purchasedetail['NET_AMOUNT_PAID']}, {color(4)}TIME{color()} : {str(purchasedetail['DATE_OF_PURCHASE'])} {str(purchasedetail['TIME_OF_PURCHASE'])}''')

    return parameters[0:4]

# to add many purchases
def new_purchases(customername=None,customeremail=None,customerphone=None):

    while True:

        parameters=new_purchase(customername=customername,customeremail=customeremail,customerphone=customerphone)

        decision=input(f'\n{color(4)}Enter more transaction {color()}: ')

        if decision=='y':

            customername=parameters[0]
            customeremail=parameters[1]
            customerphone=parameters[2]

            continue

        else:

            print()

            break



# showing all purchases made
def all_purchases():
    
    query='SELECT * FROM PURCHASES'

    cursor.execute(query)

    purchases=list(cursor.fetchall())

    for purchase in purchases:                                                                                # contain single purchase detail one by one

        print('\n\n')  

        for x,y in purchase.items():                                                                          # extracting information from the purchase instance one by one

            print(f'''{color(6)}{x}:{color()}{y}''')



'''----------------------------------------------------- HELP ----------------------------------------------------'''

def help():

    f=open('/home/surajshukla7656/Documents/nextpython/nextprojects/PROJECT_OSIRIS/README','r')

    for line in f.readlines():

        print(line,end='')
   
  
if __name__=='__main__':
   
   #stocks(10008)

   #update_stocks(10008,23)

   new_purchases()
   pass