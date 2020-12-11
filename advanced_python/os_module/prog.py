'''
os.path.basename(path) # It is used to return the basename of the file . This function basically return the file name from the path given.



It is possible to automatically perform many operating system tasks. The OS module in Python provides functions for creating and removing a directory (folder), fetching its contents, changing and identifying the current directory, etc.

We can create a new directory using the mkdir() function from the OS module.
>>> import os
>>>os.mkdir("d:\\tempdir")

A new directory corresponding to the path in the string argument of the function will be created. If we open D drive in Windows Explorer, we should notice tempdir folder create
Changing the Current Working Directory

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
 Removing a Directory

The rmdir() function in the OS module removes the specified directory either with an absolute or relative path. However, we can not remove the current working directory. Also, for a directory to be removed, it should be empty. For example, tempdir will not be removed if it is the current directory. We have to change the current working directory and then remove tempdir.
>>>os.chdir("tempdir")
>>>os.getcwd()
'd:\\tempdir'
>>>os.rmdir("d:\\tempdir")
PermissionError: [WinError 32] The process cannot access the file because it is being used by another process: 'd:\\tempdir'
>>>os.chdir("..")
>>>os.rmdir("tempdir")
List Files and Sub-directories

The listdir() function returns the list of all files and directories in the specified directory.
>>>os.listdir("c:\python37")
['DLLs', 'Doc', 'fantasy-1.py', 'fantasy.db', 'fantasy.py', 'frame.py', 'gridexample.py', 'include', 'Lib', 'libs', 'LICENSE.txt', 'listbox.py', 'NEWS.txt', 'place.py', 'players.db', 'python.exe', 'python3.dll', 'python36.dll', 'pythonw.exe', 'sclst.py', 'Scripts', 'tcl', 'test.py', 'Tools', 'tooltip.py', 'vcruntime140.dll', 'virat.jpg', 'virat.py']

If we don't specify any directory, then list of files and directories in the current working directory will be returned.
>>>os.listdir()
['.config', '.dotnet', 'python']
OS Path module in Python
OS Path module in Python

This module contains some useful functions on pathnames. The path parameters are either strings or bytes . These functions here are used for different purposes such as for merging, normalizing and retrieving path names in python . All of these functions accept either only bytes or only string objects as their parameters. The result is an object of the same type, if a path or file name is returned. As there are different versions of operating system so there are several versions of this module in the standard library.
os.path.basename(path) : It is used to return the basename of the file . This function basically return the file name from the path given.
# basename function 
import os 
out = os.path.basename("/baz/foo") 
print(out)
os.path.dirname(path) : It is used to return the directory name from the path given. This function returns the name from the path except the path name.
# dirname function 
import os 
out = os.path.basename("/baz/foo") 
print(out)


os.path.isabs(path) : It specifies whether the path is absolute or not. In Unix system absolute path means path begins with the slash(‘/’) and in Windows that it begins with a (back)slash after chopping off a potential drive letter.

# isabs function  
import os 
out = os.path.isabs("/baz/foo") 
print(out) 

Output:

True
 os.path.isdir(path) : This function specifies whether the path is existing directory or not.

# isdir function  
import os 
out = os.path.isdir("C:\\Users") 
print(out) 

Output:
 os.path.isfile(path) : This function specifies whether the path is existing file or not.
# isfile function  
import os 
out = os.path.isfile("C:\\Users\foo.csv") 
print(out) 

Output:

True'''