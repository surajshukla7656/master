# ------------------reading file ----------------->
f=open("<filename>")
print(f.read())
print(f'cursorPosition{f.tell()}') # to find the position of cursor
f.seek(0) # to change the postion of the cursor


f.readline() #reads single lines

f.readlines() #creates a list containing all lines of the  file as an element
            

#name,closed (data descriptor)

print(f.name)  #gives the name of the file
print(f.closed) #checks the file closed or not

f=open(r'<fullpathaddress>') # r---> refers to read only to python

for line in f.readlines():
    print(line,end="")


#general method of opening file

with open("file.txt") as f:
    data=f.read()
    print(data)

#reading or writing

# w - use to write , old data deleted , creates new file when file does not exist
# a - use to write extra , does not delete old data , also creates a new file if it does not exist 
# r+ - read and write mode

# read and write to another file
with open("file.txt","r") as rf:
    with open("file2.txt") as f:
        f.write(rf.read())

        