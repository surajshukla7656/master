import os

# os.mkdir('nextpython/new_directory')                                                  # creates new directory     

# os.rmdir('new_directory')                                                                           # deletes existing and empty directory 

a=os.path.basename('/home/surajshukla7656/Documents/Python/nextpython/advanced_python/os_module')   # return os_module
print(a)

print(os.getcwd())                                                                                  # return absolute path of  current working directory

# os.chdir('/home/surajshukla7656/Documents/Python/nextpython/new_directory')                         # change working directory

print(os.getcwd())

a=os.listdir()                                                                                       # return list of files/directories present in the working directory
print(a)

a=os.listdir('/home/surajshukla7656/Documents/Python/nextpython')

a=os.path.dirname('/home/surajshukla7656/Documents/Python/nextpython/new_directory')                 # return  /home/surajshukla7656/Documents/Python/nextpython
print(a)

a=os.path.isabs('/home/surajshukla7656/Documents/Python/nextpython')                                 # return True
print(a)

a=os.path.isdir('/home/surajshukla7656/Documents/Python/nextpython')                                 # return True
print(a)

a=os.path.isfile('/home/surajshukla7656/Documents/Python/nextpython')                                # return False
print(a)

a=os.path.exists('/home/surajshukla7656/Documents/Python/nextpython')
print(a)

a=os.remove('nextpython/new_directory/.py')                                                            # remove file
print(a)