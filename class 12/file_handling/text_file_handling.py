# from a file
file1 = open('abc.txt', 'r')

contents = file1.read(10)

print(contents)

file1.close()

# Python program to read only first 10 characters
# from a file
file1 = open('abc.txt', 'r')

line1 = file1.readline()

print(line1, end='')

line2 = file1.readline()

print(line2, end='')

file1.close()

# Python program to read all lines
# in a list from a text file
# using readlines()
f = open('abc.txt', 'r')

lines = f.readlines()

for line in lines:
    print(line, end='')

f.close()


# Python program that reads text
# after second character into a list
f = open('abc.txt', 'r')
print(f.read(2))

# Now read after second character
lines = f.readlines()
print("The remaining text:")
for line in lines:
    print(line, end='')
f.close()

# Python program to write text to a file
fp = open('poem.txt', 'w')
fp.write('Twinkle, twinkle, little star,\n')
fp.write('How I wonder what you are!\n')
fp.write('Up above the world so high,\n')
fp.write('Like a diamond in the sky.\n')
fp.close()
print('Data written to the file successfully.')

# Python program to append text to a file
f = open('poem.txt', 'a')     # append mode
f.write('\n')
f.write('When the blazing sun is gone,\n')
f.write('When he nothing shines upon,\n')
f.write('Then you show your little light,\n')
f.write('Twinkle, twinkle, all the night.\n')
f.close()
print('Data written to the file successfully.')

# Python program that adds numeric data
# to a text file using conversion function str()
fobj = open('test.txt', 'w')
roll_no = 12526
name = 'Badshah'
marks_in_CS = 69
fobj.write(str(roll_no))  # numeric data converted into string
fobj.write('\n')
fobj.write(name)
fobj.write('\n')
fobj.write(str(marks_in_CS)) # numeric data converted into string
fobj.write('\n')
print("Data written to the file successfully.")
fobj.close()

# Python program to illustrate the use of
# writelines() method for writing members
# of a list to a text file
f = open('subjects.txt', 'w')

sub_list = ['Computer Science\n', 'Physics\n', 
    'Chemistry\n', 'Mathemetics\n', 'English Language\n']

f.writelines(sub_list)
f.close()

# Reopen the file for reading
f = open('subjects.txt', 'r')
lines = f.readlines()

print('The content of the file:')
for line in lines:
    print(line, end='')

f.close()
# Python program to illustrate with statement
# with statement automatically closes a file
# when we stop using it

with open('python1.txt', 'w') as fobj:
    fobj.write('Python is an interpreted programming language\n')
    fobj.write('It is high-level, general-purpose programming language.\n')
    fobj.write('It was created by by Guido van Rossum\n')
    fobj.write('Python was first released in 1991\n')
    print('Is file closed? ', fobj.closed) # file still in use,
                                            # so not closed
print('Is file closed now? ', fobj.closed)  # file is closed
print(fobj.close())     # file has already been closed