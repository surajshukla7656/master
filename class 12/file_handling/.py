'''Pie (π) is a well-known mathematical constant, which is defined as the ratio of the circumference to the diameter of a circle and its value is 3.141592653589793.

>>> import math
>>>math.pi
3.141592653589793  

# Another well-known mathematical constant defined in the math module is e. It is called Euler's number and it is a base of the natural logarithm. Its value is 2.718281828459045. 
>>>math.e
2.718281828459045
[9:37 AM, 11/22/2020] Vinod Sir: The math module contains functions for calculating various trigonometric ratios for a given angle. The functions (sin, cos, tan, etc.) need the angle in radians as an argument. We, on the other hand, are used to express the angle in degrees. The math module presents two angle conversion functions: degrees() and radians(), to convert the angle from degrees to radians and vice versa. For example, the following statements convert the angle of 30 degrees to radians and back (Note: π radians is equivalent to 180 degrees). 
>>>math.radians(30)
0.5235987755982988
>>>math.degrees(math.pi/6)
29.999999999999996 
The following statements show sin, cos and tan ratios for the angle of 30 degrees (0.5235987755982988 radians): 
>>math.sin(0.5235987755982988)
0.499999999999…
[9:37 AM, 11/22/2020] Vinod Sir: math.log()
The math.log() method returns the natural logarithm of a given number. The natural logarithm is calculated to the base e. 
>>>math.log(10)
2.302585092994046 
math.log10()
The math.log10() method returns the base-10 logarithm of the given number. It is called the standard logarithm. 
>>>math.log10(10)
1.0 
math.exp()
The math.exp() method returns a float number after raising e (math.e) to given number. In other words, exp(x) gives e**x. 
>>>math.exp(10)
1.0 
This can be verified by the exponent operator. 
>>>math.e**10
22026.465794806703
[9:38 AM, 11/22/2020] Vinod Sir: math.pow()
The math.pow() method receives two float arguments, raises the first to the second and returns the result. In other words, pow(4,4) is equivalent to 4**4. 
>>>math.pow(2,4)
16.0
>>>2**4
16 
math.sqrt()
The math.sqrt() method returns the square root of a given number. 
>>>math.sqrt(100)
10.0
>>>math.sqrt(3)
1.7320508075688772
[9:38 AM, 11/22/2020] Vinod Sir: The following two functions are called representation functions. The ceil() function approximates the given number to the smallest integer, greater than or equal to the given floating point number. The floor() function returns the largest integer less than or equal to the given number. 
>>>math.ceil(4.5867)
5
>>>math.floor(4.5687)
4
[9:39 AM, 11/22/2020] Vinod Sir: Dear students go through this material and confirm that you have understood the concepts.
[10:16 PM, 11/22/2020] Vinod Sir: Positional parameters, keyword parameters etc.:
[10:16 PM, 11/22/2020] Vinod Sir: Positional arguments are arguments that can be called by their position in the function definition.

Keyword arguments are arguments that can be called by their name.

Required arguments are arguments that must passed to the function.

Optional arguments are argument that can be not passed to the function. In python optional arguments are arguments that have a default value.
[10:16 PM, 11/22/2020] Vinod Sir: def fn (a, b, c = 1):          # a and b required, c optional.
    return a * b + c

print (fn (1, 2))               # returns 3, positional and default.
print (fn (1, 2, 3))            # returns 5, positional.
print (fn (c = 5, b = 2, a = 2)) # returns 9, named.
print (fn (b = 2, a = 2))       # returns 5, named and default.
print (fn (5, c = 2, b = 1))     # returns 7, positional and named.
print (fn (8, b = 0))           # returns 1, positional, named and default.
[10:17 PM, 11/22/2020] Vinod Sir: Output:
[10:18 PM, 11/22/2020] Vinod Sir: 3
5
9
5
7
1
[10:19 PM, 11/22/2020] Vinod Sir: Note:
The meaning of the = changes, depending on whether it's in the definition or in the call.

In the definition, it marks the argument optional and sets a default value.

In the call, it simply allows you to specify which arguments should be which values, in whatever order you want.
[10:20 PM, 11/22/2020] Vinod Sir: This concept is important from CBSE Exam point of view. So go through it and confirm thatyou have understood the concept.
[10:47 PM, 11/22/2020] Vikas: Yes Sir
[10:51 PM, 11/22/2020] Kunal: Done sir 👍🏻
[11:27 PM, 11/22/2020] Vinod Sir: Some examples of time module:
[11:31 PM, 11/22/2020] Vinod Sir: Python has a module named time to handle time-related tasks. To use functions defined in the module, we need to import the module first.
import time
[11:32 PM, 11/22/2020] Vinod Sir: # The time() function returns the number of seconds passed since epoch.
# For Unix system, January 1, 1970, 00:00:00 at UTC is epoch (the point where time begins).
import time
seconds = time.time()
print("Seconds since epoch =", seconds)
[11:34 PM, 11/22/2020] Vinod Sir: # The time.ctime() function takes seconds passed since epoch as an argument and returns a
# string representing local time.
import time

# seconds passed since epoch
seconds = 1545925769.9618232
local_time = time.ctime(seconds)
print("Local time:", local_time)
[11:34 PM, 11/22/2020] Vinod Sir: If you run the program, the output will be something like:
Local time: Thu Dec 27 15:49:29 2018
[11:35 PM, 11/22/2020] Vinod Sir: # The sleep() function suspends (delays) execution of 
# the current thread for the given number of seconds.
import time

print("This is printed immediately.")
time.sleep(2.4)
print("This is printed after 2.4 seconds.")
[11:36 PM, 11/22/2020] Vinod Sir: # The localtime() function takes the number of seconds
# passed since epoch as an argument and returns struct_time in local time.
import time

result = time.localtime(1545925769)
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)
[11:36 PM, 11/22/2020] Vinod Sir: When you run the program, the output will be something like:
result: time.struct_time(tm_year=2018, tm_mon=12, tm_mday=27, tm_hour=15, tm_min=49, tm_sec=29, tm_wday=3, tm_yday=361, tm_isdst=0)

year: 2018
tm_hour: 15
[11:39 PM, 11/22/2020] Vinod Sir: The sys module:
[11:39 PM, 11/22/2020] Vinod Sir: Python sys module

The python sys module provides functions and variables which are used to manipulate different parts of the Python Runtime Environment. It lets us access system-specific parameters and functions.
[11:40 PM, 11/22/2020] Vinod Sir: sys.modules

This function provides the name of the existing python modules which have been imported.
[11:40 PM, 11/22/2020] Vinod Sir: sys.argv

This function returns a list of command line arguments passed to a Python script. The name of the script is always the item at index 0, and the rest of the arguments are stored at subsequent indices.
[11:41 PM, 11/22/2020] Vinod Sir: sys.path

This function shows the PYTHONPATH set in the current system. It is an environment variable that is a search path for all the python modules.
[11:41 PM, 11/22/2020] Vinod Sir: sys.stdin

It is an object that contains the original values of stdin at the start of the program and used during finalization. It can restore the files.
[11:41 PM, 11/22/2020] Vinod Sir: sys.exit

This function is used to exit from either the Python console or command prompt, and also used to exit from the program in case of an exception.
[11:42 PM, 11/22/2020] Vinod Sir: sys.platform

This value of this function is used to identify the platform on which we are working.
[11:43 PM, 11/22/2020] Vinod Sir: The sys module allows you to use stdin() and stdout(), as well as stderr(), but, most interestingly, we can utilize sys.argv().
[11:52 PM, 11/22/2020] Vinod Sir: Examples of sys module:
[11:52 PM, 11/22/2020] Vinod Sir: import sys

sys.stderr.write('This is stderr text\n')
sys.stderr.flush()
sys.stdout.write('This is stdout text\n')
[11:52 PM, 11/22/2020] Vinod Sir: Output:
[11:53 PM, 11/22/2020] Vinod Sir: This is stderr text
This is stdout text
[11:53 PM, 11/22/2020] Vinod Sir: argv = command line arguments:
[11:53 PM, 11/22/2020] Vinod Sir: import sys
def main(arg):
    print(arg)

main(sys.argv[1])
main(sys.argv[0])
[11:54 PM, 11/22/2020] Vinod Sir: Output:
[11:54 PM, 11/22/2020] Vinod Sir: $ python3 prog7.py   John
John
prog7.py
[11:55 PM, 11/22/2020] Vinod Sir: argv[0] is the name of python script (the program) and argv[1], argv[2], ...  are command line arguments
[11:59 PM, 11/22/2020] Vinod Sir: import sys

for i in range(len(sys.argv)):
    if i == 0:
        print ("Function name: %s" % sys.argv[0])
    else:
        print ("%d. argument: %s" % (i,sys.argv[i]))
[11:59 PM, 11/22/2020] Vinod Sir: Output:
[11:59 PM, 11/22/2020] Vinod Sir: $ python3 prog8.py John Smith Lucy
Function name: prog8.py
1. argument: John
2. argument: Smith
3. argument: Lucy
[12:08 AM, 11/23/2020] Vinod Sir: Use sys.exit() to exit Python

Call sys.exit(arg) to exit from Python with the exit status as arg. The argument arg can be an integer or another type of object and defaults to zero to indicate a successful termination. Set arg to any nonzero value to indicate an abnormal termination.
[12:08 AM, 11/23/2020] Vinod Sir: # Python program to demonstrate 
# sys.exit() 
  
  
import sys 
  
  
age = 17
  
  
if age < 18: 
      
    # exits the program 
    sys.exit("Age less than 18")     
else: 
    print("Age is not less than 18")
[12:08 AM, 11/23/2020] Vinod Sir: Output:
[12:09 AM, 11/23/2020] Vinod Sir: Age less than 18
[12:10 AM, 11/23/2020] Vinod Sir: Python os module:
[12:10 AM, 11/23/2020] Vinod Sir: Python - OS Module

It is possible to automatically perform many operating system tasks. The OS module in Python provides functions for creating and removing a directory (folder), fetching its contents, changing and identifying the current directory, etc.
[12:11 AM, 11/23/2020] Vinod Sir: Creating Directory (Folder):

We can create a new directory using the mkdir() function from the OS module.
>>> import os
>>>os.mkdir("d:\\tempdir")

A new directory corresponding to the path in the string argument of the function will be created. If we open D drive in Windows Explorer, we should notice tempdir folder created.
[12:12 AM, 11/23/2020] Vinod Sir: Changing the Current Working Directory

We must first change the current working directory to a newly created one before doing any operations in it. This is done using the chdir() function.
>>> import os
>>>os.chdir("d:\\tempdir")

There is a getcwd() function in the OS module using which we can confirm if the current working directory has been changed or not.
>>>os.getcwd()
'd:\\tempdir'

Directory paths can also be relative. If the current directory is set to D drive and then to tempdir without mentioning the preceding path, then also the current working directory will be changed to d:\tempdir.
>>>os.chdir("d:\\")
>>>os.getcwd()
'd:\\'
>>>os.chdir("tempdir")
>>>os.getcwd()
'd:\\tempdir'

In order to set the current directory to the parent directory use "..…
[12:12 AM, 11/23/2020] Vinod Sir: Removing a Directory

The rmdir() function in the OS module removes the specified directory either with an absolute or relative path. However, we can not remove the current working directory. Also, for a directory to be removed, it should be empty. For example, tempdir will not be removed if it is the current directory. We have to change the current working directory and then remove tempdir.
>>>os.chdir("tempdir")
>>>os.getcwd()
'd:\\tempdir'
>>>os.rmdir("d:\\tempdir")
PermissionError: [WinError 32] The process cannot access the file because it is being used by another process: 'd:\\tempdir'
>>>os.chdir("..")
>>>os.rmdir("tempdir")
[12:12 AM, 11/23/2020] Vinod Sir: List Files and Sub-directories

The listdir() function returns the list of all files and directories in the specified directory.
>>>os.listdir("c:\python37")
['DLLs', 'Doc', 'fantasy-1.py', 'fantasy.db', 'fantasy.py', 'frame.py', 'gridexample.py', 'include', 'Lib', 'libs', 'LICENSE.txt', 'listbox.py', 'NEWS.txt', 'place.py', 'players.db', 'python.exe', 'python3.dll', 'python36.dll', 'pythonw.exe', 'sclst.py', 'Scripts', 'tcl', 'test.py', 'Tools', 'tooltip.py', 'vcruntime140.dll', 'virat.jpg', 'virat.py']

If we don't specify any directory, then list of files and directories in the current working directory will be returned.
>>>os.listdir()
['.config', '.dotnet', 'python']
[12:19 AM, 11/23/2020] Vinod Sir: OS Path module in Python:
[12:19 AM, 11/23/2020] Vinod Sir: OS Path module in Python

This module contains some useful functions on pathnames. The path parameters are either strings or bytes . These functions here are used for different purposes such as for merging, normalizing and retrieving path names in python . All of these functions accept either only bytes or only string objects as their parameters. The result is an object of the same type, if a path or file name is returned. As there are different versions of operating system so there are several versions of this module in the standard library.
[12:20 AM, 11/23/2020] Vinod Sir: os.path.basename(path) : It is used to return the basename of the file . This function basically return the file name from the path given.
[12:20 AM, 11/23/2020] Vinod Sir: # basename function 
import os 
out = os.path.basename("/baz/foo") 
print(out)
[12:21 AM, 11/23/2020] Vinod Sir: os.path.dirname(path) : It is used to return the directory name from the path given. This function returns the name from the path except the path name.
[12:21 AM, 11/23/2020] Vinod Sir: # dirname function 
import os 
out = os.path.basename("/baz/foo") 
print(out)
[12:22 AM, 11/23/2020] Vinod Sir: Output:

'/baz'
[12:22 AM, 11/23/2020] Vinod Sir: output:foo
[12:24 AM, 11/23/2020] Vinod Sir: os.path.isabs(path) : It specifies whether the path is absolute or not. In Unix system absolute path means path begins with the slash(‘/’) and in Windows that it begins with a (back)slash after chopping off a potential drive letter.

# isabs function  
import os 
out = os.path.isabs("/baz/foo") 
print(out) 

Output:

True
[12:24 AM, 11/23/2020] Vinod Sir: s.path.isdir(path) : This function specifies whether the path is existing directory or not.

# isdir function  
import os 
out = os.path.isdir("C:\\Users") 
print(out) 

Output:
[12:25 AM, 11/23/2020] Vinod Sir: os.path.isfile(path) : This function specifies whether the path is existing file or not.
# isfile function  
import os 
out = os.path.isfile("C:\\Users\foo.csv") 
print(out) 

Output:

True

'''