with open('/home/surajshukla7656/Documents/Python/nextpython/advanced_python/text_file_handling/basics.txt','r') as f:

    # a=f.read()                                 # return whole file as string 
    # print(a)                                            

    # a=f.read(5)                                # return 5 characters
    # print(a)

    # a=f.readline()                             # return a line from cursor 
    # print(a)

    # a=f.readline(5)                            # return 5 characters
    # print(a)

    # a=f.readlines()                            # return list of strings of line
    # print(a)

    # a=f.readlines(23)                          # return list of lines(string) upto which the specified character lies
    # print(a)

    # print(f.readable())                          # return True

    # print(f.writable())                          # return False

    a=f.tell()
    print(a)
    
    pass