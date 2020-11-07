#File Handling

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

Syntax:

f = open("demofile.txt")
The code above is the same as:

f = open("demofile.txt", "rt")
Because "r" for read, and "t" for text are the default values, you do not need to specify them.

'''

#Python File Methods

''''

Method          	Description
close()	            Closes the file
detach()	        Returns the separated raw stream from the buffer
fileno()	        Returns a number that represents the stream, from the operating system's perspective
flush()         	Flushes the internal buffer
isatty()	        Returns whether the file stream is interactive or not
read()      	    Returns the file content
readable()      	Returns whether the file stream can be read or not
readline()	        Returns one line from the file
readlines()	        Returns a list of lines from the file
seek()	            Change the file position
seekable()	        Returns whether the file allows us to change the file position
tell()          	Returns the current file position
truncate()	        Resizes the file to a specified size
writable()	        Returns whether the file can be written to or not
write()            	Writes the specified string to the file
writelines()	    Writes a list of strings to the file

'''