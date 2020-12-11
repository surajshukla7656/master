import sys
#This function provides the name of the existing python modules which have been imported.
a=sys.modules                          # return
print(a)

# This function returns a list of command line arguments passed to a Python script. The name of the script is always the item at index 0, and the rest of the arguments are stored at subsequent indices.

sys.argv


#This function shows the PYTHONPATH set in the current system. It is an environment variable that is a search path for all the python modules.
sys.path

#It is an object that contains the original values of stdin at the start of the program and used during finalization. It can restore the files.
sys.stdin

# This function is used to exit from either the Python console or command prompt, and also used to exit from the program in case of an exception.
sys.exit

# This value of this function is used to identify the platform on which we are working.
sys.platform

# the sys module allows you to use stdin() and stdout(), as well as stderr(), but, most interestingly, we can utilize sys.argv().
sys.stderr.write('This is stderr text\n')
sys.stderr.flush()
sys.stdout.write('This is stdout text\n')

'''
This is stderr text
This is stdout text
''' 


def main(arg):
    print(arg)

main(sys.argv[1])
main(sys.argv[0])

'''
$ python3 prog7.py   John
John
prog7.py
[11:55 PM, 11/22/2020] Vinod Sir: argv[0] is the name of python script (the program) and argv[1], argv[2], ...  are command line arguments
'''

for i in range(len(sys.argv)):
    if i == 0:
        print ("Function name: %s" % sys.argv[0])
    else:
        print ("%d. argument: %s" % (i,sys.argv[i]))

'''

$ python3 prog8.py John Smith Lucy
Function name: prog8.py
1. argument: John
2. argument: Smith
3. argument: Lucy

'''



# Call sys.exit(arg) to exit from Python with the exit status as arg. The argument arg can be an integer or another type of object and defaults to zero to indicate a successful termination. Set arg to any nonzero value to indicate an abnormal termination. 
# sys.exit() 
age = 17
  
if age < 18: 
      
    # exits the program 
    sys.exit("Age less than 18")     
else: 
    print("Age is not less than 18")

