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

            var=input(f'{color(5)}Enter {detail}:{color()}')
            
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

    query='SELECT BRAND,MODEL_NO FROM LAPTOP '

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


# 

   
if __name__=='__main__':
    #add_laptop('HP','THINKPAD','10TH GEN INTEL CORE i8','INTEL UHD','WINDOWS 10 HOME','LPDDR4 4GB','16 INCH FULL HD+ ','512 SSD','5MP WEBCAM','8 HOURS BACKUP','BACKLIGHT KEYS MAGIC KEYBOARD','MIC','DOLBY MODE','2 USB 1 USB TYPE-C','10','5','2 KG','1 YEAR','2020','INDIA',34,29999)
    #day(brand='LENOVO')
    add_laptops()
    pass