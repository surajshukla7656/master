# note - opening a file with w  always erases the intial data of file 
with open('/home/surajshukla7656/Documents/Python/nextpython/advanced_python/text_file_handling/basics.txt','w') as f:

    # a=f.write('my name suraj shukla\n i read in 12 class')              # return no of characters(also counts - \n)
    # print(a)

    l=['gagan','suraj','abhay']
    a=f.writelines(l)                                                     # return None
    print(a)

    # print(f.writable())                                                 # return True

    # print(f.readable())                                                 # return False
    pass

with open('nextpython/advanced_python/text_file_handling/basics','x') as f:

    # print(f.writable())                                   # return True --- x allows write in a file

    # print(f.write('my name is suraj'))                    # return 16(no of characters)

    # print(f.readable())                                   # return False
    pass