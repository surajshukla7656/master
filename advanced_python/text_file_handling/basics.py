'''
The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)

'''



#Python File Methods

'''

Method          	            checklist            Description                                                                                  
close()	                            ##               Closes the file                                                                              
detach()	                        #                Returns the separated raw stream from the buffer                                                                         
fileno()	                        #                Returns a number that represents the stream, from the operating system's perspective             
flush()         	                #                Flushes the internal buffer                                                                      
isatty()	                        #                Returns whether the file stream 14. write a program to sort a list                                          
read(characters)      	            ##               Returns the file content                                                                         
readable()      	                ##               Returns whether the file stream can be read or not                                               
readline()	                        ##               Returns one line from the file                                                                   
readlines()	                        ##               Returns a list of lines from the file                                                            
seek(new_position)       	        ##               Change the file position                                                                         
seekable()	                        ##               Returns whether the file allows us to change the file position                                   
tell()          	                ##               Returns the current file position                                                                
truncate(size)    	                ##               Resizes the file to a specified size                                                             
writable()	                        ##               Returns whether the file can be written to or not                                                
write(str)            	            ##               Writes the specified string to the file                                                          
writelines(list)	                ##               Writes a list of strings to the file                                                             

'''

##### opening of file #####

### simple method

# f = open("basics.txt")                          # by default 'rt' mode 

# f = open("basics.txt", "rt")

# f.close()

### using with keyword

# with open('advanced_python/file_handling_text/basics.txt') as f:

#     print(f.closed)            # returns False

# print(f.closed)                # returns True --- with closes file automatically when we exit its block


### read

# with open('advanced_python/file_handling_text/basics.txt','r') as f:

#     print('readable-',f.readable())          # returns True if file is readable

#     print('read-',f.read())                  # reading whole file

#     print('read(5)-',f.read(5))              # reading first five characters of file --- here it will return nothing as the cursor lies at the end of the file

#     print('tell-',f.tell())                  # tells the position of cursor in the form of index --- return position index

#     print('seek-',f.seek(0))                 # to move the cursor at the top --- return new position index

#     print('read(5)-',f.read(5))              # reading first five characters of file

#     l1=f.readline()                          # return single line --- depends on previous cursor position
  
#     print('readline',l1)

#     l=f.readlines()                          # returns list of all lines of the file ---  depends on previous cursor position

#     print('readlines',l)  

    

### write 

# with open('advanced_python/file_handling_text/basics.txt','w') as f:

#     print('writable-',f.writable())                                        # returns True if file is writable

#     print('write',f.write('my name is surajshukla\n'))                     # only allowed string --- return number of characters written --- overwrites into the file --- or creates a new file if not exist --- Error if no argument is given

#     l_write=['i read in 12 class\n','my aim is to be scientist\n','i am doing hard']

#     print(f.writelines(l_write))                                           # merges the strings into one line without any space --- returns None --- Error if no argument is given


### remaining

with open('advanced_python/file_handling_text/basics.txt','a') as f2:
    
    print(f2.tell())                                         # returns last character index as append mode is used

    print('seekable-',f2.seekable())                         # returns True if seekable

    print(f2.truncate())                                     # delete the content of file next to that position if specified otherwise current position will be used by default

    