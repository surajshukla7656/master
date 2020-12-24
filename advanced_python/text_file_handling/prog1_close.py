f=open('/home/surajshukla7656/Documents/Python/nextpython/advanced_python/text_file_handling/basics.txt','r')

print(f.closed)         # return False

f.close()

print(f.closed)         # return True

with open('/home/surajshukla7656/Documents/Python/nextpython/advanced_python/text_file_handling/basics.txt','r') as f:

    print(f.closed)                     # return False

print(f.closed)                         # return True                           